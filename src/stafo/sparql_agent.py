"""
LLM-based SPARQL Query Generation from Natural Language over Federated Knowledge Graphs https://arxiv.org/pdf/2410.06062
FIRESPARQL: A LLM-based Framework for SPARQL Query Generation over Scholarly Knowledge Graphs https://arxiv.org/abs/2508.10467


GPT-5.1 Instant: cannot reliably retrieve uncommon item ids from wikidata -> hallucinates numbers

Proposed workflow
- Question in natural language
- use llm to disect question, extract relevant nouns and verbs
- let LLM reason what other relation / aux items are needed
- embed extractions
- find relevant entities in KG
- supply these to LLM, let create sparql
- validate sparql


"""
import sys, os
from google import genai
from google.genai import types
import re, regex
try:
    # available in python >=3.11
    import tomllib
except ModuleNotFoundError:
    # this is for python3.10
    import tomli as tomllib
import pandas as pd
import time
import numpy as np
from sentence_transformers import SentenceTransformer, util
import torch

import pyirk as p

from stafo.utils import BASE_DIR, CONFIG_PATH
from stafo.core import llm_api
from stafo.stafo_logging import sparql_logger as logger


with open(CONFIG_PATH, "rb") as fp:
    config_dict = tomllib.load(fp)


class SparqlAgent():
    def __init__(self, load_irk_modules: list[dict]=[]):
        # parameters
        self.embedding_model = SentenceTransformer("all-MiniLM-L6-v2")
        self.generation_model = "gemini-2.5-flash"
        self.embedding_csv_path = "pyirk_embeddings.csv"
        self.llm_log_path = "llm_log.txt"
        self.min_sim_score = 0.6
        self.score_interval = 0.9
        self.max_iterations = 3

        # init
        if load_irk_modules:
            for load_dict in load_irk_modules:
                assert isinstance(load_dict, dict), "load_irk_modules takes list of dicts. dicts must have keys path, module_name, prefix"
                if "uri" in load_dict.keys():
                    mod = p.irkloader.load_mod_from_uri(load_dict["uri"], prefix=load_dict["prefix"], reuse_loaded=True)
                elif "path" in load_dict.keys():
                    nl = p.irkloader.load_mod_from_path(load_dict["path"], prefix=load_dict["prefix"], reuse_loaded=True)


        self.client = genai.Client(api_key=config_dict["gemini_api_key"])
        if os.path.isfile(self.embedding_csv_path):
            self.df = pd.read_csv(self.embedding_csv_path)
        else:
            yn = input("No embedding for pyirk entities found. Create it now? [y/n]")
            if yn == "y":
                self.setup_embeddings()
            else:
                sys.exit()

        self.config = types.GenerateContentConfig(
            tools=[self.get_similar_entity, self.get_entity_info],
            automatic_function_calling=types.AutomaticFunctionCallingConfig(
                disable=False,
                maximum_remote_calls=30,
            ),
        )

    def setup_embeddings(self):

        pyirk_entities_path = "pyirk_entities.yaml"

        # since this is embedded we dont need uris
        pyirk_entities = p.core.export_entities(pyirk_entities_path, uris=False)
        data = list(pyirk_entities.values())

        embeddings = self.embedding_model.encode(data)

        self.df = pd.DataFrame(embeddings)
        self.df.insert(0, "uri", pyirk_entities.keys())
        self.df.to_csv(os.path.join(BASE_DIR, self.embedding_csv_path), index=False)

    def generate_sparql_from_question(self, question, verbose=False):
        logger.info("#################################################################################################")
        logger.info(f"Question:\n{question}")
        contents = [
            types.Content(
                role="model",
                parts=[types.Part(
                    text="You are a helpful semantic assistent. You have access to a knowledge graph with nodes and edges. "
                    "Your Task is to write a SPARQL query answering the user question. "
                    "You have tools at your disposal. First, analyze the user input and extract relevant concepts or phrases that could be modeled in the graph. "
                    "Use the tools to find the corresponding entities in the graph. If you think you need additional concepts to model the question, "
                    "try to find them in the graph as well using the tools. Always start with the tool 'get_similar_entity'. "
                    "An Uri looks like this: base:/module#I1234. Only use URIs you get from tool calls! "
                    "Afterwards, create SPARQL code answering the user Question. "
                    # "If you find that you are missing information or cannot complete the task, describe your problem in detail."
            )]),
            types.Content(
                role="user",
                parts=[types.Part(
                    text=f"User Question:\n{question}"
                )]
            )
        ]

        logger.info(f"Prompt:\n{contents}")
        response = self.client.models.generate_content(
            model=self.generation_model,
            contents=contents,
            config=self.config,
        )
        verbose_response = self.get_calling_history(response)
        logger.info(f"Response:\n{verbose_response}")
        if verbose:
            print(verbose_response)

        with open(self.llm_log_path, "at") as f:
            f.write("\n#########################################################\n")
            f.write(f"Question: {question}\n")
            f.write(f"Answer:\n{verbose_response}")

        return response

    def get_calling_history(self, response: genai.types.GenerateContentResponse):
        out = "Output: " + response.text + "\n"
        for call in response.automatic_function_calling_history:
            p0 = call.parts[0]
            if fn_call := p0.function_call:
                out += f"Function to call: {fn_call.name}\n"
                out += f"Arguments: {fn_call.args}\n"
                out += "-------\n"
            elif fn_response := p0.function_response:
                out += f"Function response for: {fn_response.name}\n"
                out += f"Response: {fn_response.response}\n"
                out += "-------\n"
        return out

    def get_similar_entity(self, phrase: str) -> str:
        """find entities in the knowledge graph similar to the given phrase in the embedding space

        Args:
            phrase (str): some word or phrase

        Returns:
            list[str]: list of uris corresponding to entities in the knowledge graph
        """
        # embed phrase
        embedding = np.float64(self.embedding_model.encode(phrase))
        # calc similarity with embedded pyirk entities
        scores = self.embedding_model.similarity(embedding, torch.tensor(self.df[self.df.columns[1:]].to_numpy())).numpy().flatten()
        # find results >=95% as good as best
        max_score = np.max(scores)
        # if max_score > self.min_sim_score:
        res = list(self.df.index[np.where(scores > max_score*self.score_interval)[0]].values)
        # combine uri and name
        output = ""
        for r in res:
            uri = self.df["uri"][r]
            output += f"uri: {uri}, label: {p.ds.get_entity_by_uri(uri).R1.value}\n"
        return output

    def cleanup_uri(self, uri):
        """llm will not conform to pyirk uri standards and e.g. the label

        Args:
            uri (str): wrong (but recognizable) uri
        Returns:
            str: correct uri
        """
        res = re.findall(r"\w+:/\w+#[I|R]\d+", uri)
        if len(res) == 1:
            return res[0]
        else:
            raise ValueError(f"Uri {uri} is wrong!")

    def _entity_info(self, entity):
        info = f"{entity.uri}: {entity.R1.value}"
        if entity.R2:
            info += f"\ndescription: {entity.R2.value}"
        info += "\nRelations:\n"
        info += repr(entity.get_relations())
        info += repr(entity.get_inv_relations())
        return info

    def get_entity_info(self, uri: str) -> str:
        """return basic information about a given entity in the graph. May be a node or an edge.

        Args:
            uri (str): uri of the entity

        Returns:
            str: information about the entity
        """
        print(f"Tool Call: get_entity_info(node_uri={uri})")
        uri = self.cleanup_uri(uri)
        try:
            entity = p.ds.get_entity_by_uri(uri)
            return self._entity_info(entity)
        except:
            return "Entity not found"

    def extract_sparql(self, response: genai.types.GenerateContentResponse):
        """find the sparql code in the answer of the llm. maybe there are ticks ``` or additional explanations."""
        pattern = regex.compile(r"""
        (?(DEFINE)                              # Define BRACKET pattern
        (?P<BRACKET>
            \{                                  # any opening {
            (?:
                [^{]+                           # text nodes
                | (?&BRACKET)                   # nested {} (recursion)
            )*
            \}
        )
        )
        SELECT .+? (?&BRACKET)
        """, regex.DOTALL | regex.VERBOSE | regex.IGNORECASE)
        res = regex.search(pattern, response.text)
        if res is not None:
            logger.info(f"sparql extracted:\n{res.group(0)}")
            query = res.group(0)
            unique_prefixes = set(re.findall(r"irk:/(.+?)#", query))
            for up in unique_prefixes:
                prefix = re.findall(r"\w+", up)[0] + ":" # cut off ocse/0.2 -> ocse
                query = re.sub(f"irk:/{up}#", prefix, query)
                query = f"PREFIX {prefix} <irk:/{up}#>\n" + query

            logger.info(f"query with correct prefixes:\n{query}")
            return query
        else:
            logger.info(f"no sparql found in {response.text}")
            raise ValueError(f"No valid SPARQL found in {response.text}")

    def execute_sparql(self, sparql: str):
        logger.info(f"executing sparql code")
        p.ds.rdfgraph = p.rdfstack.create_rdf_triples()
        try:
            res = p.ds.rdfgraph.query(sparql)
            assert res != [], "SPARQL code was valid, but query did not return any results, Try again!"
            logger.info("success")
        except Exception as e:
            logger.info(f"Error:\n{e}")
            return False, e
        res2 = p.aux.apply_func_to_table_cells(p.rdfstack.convert_from_rdf_to_pyirk, res)
        # todo right format
        return True, res2

    def rework_sparql(self, question, response, result):
        contents = [
            types.Content(
                role="model",
                parts=[types.Part(
                    text="You are a helpful SPARQL assistent. Your task is to correct a given SPARQL query answering the users question. "
                    "You will also have access to the extracted nodes and edges of the corresponding knowledge graph. "
                    "You also will see the error message produced by running the given Query. "
                    "Rewrite the SPARQL query without errors, so that it can be used to answer the user question. "
                    "Only use URIs you got from tools or from the calling history."
                    # "If you find that you are missing information or cannot complete the task, describe your problem in detail."
            )]),
            types.Content(
                role="user",
                parts=[types.Part(
                    text=f"User Question:\n{question}\n"
                    f"Wrong SPARQL query and calling history:\n{self.get_calling_history(response)}\n"
                    f"Error Message when running the SPARQL code:\n{result}"
                )]
            )
        ]
        logger.info("Rework SPARQL")
        logger.info(f"Prompt:\n{contents}")
        response = self.client.models.generate_content(
            model=self.generation_model,
            contents=contents,
            config=self.config
        )
        logger.info(f"Response:\n{response.text}")

        return response

    def process_sparql_result(self, question, response_data, sparql_result: list):
        contents = [
            types.Content(
                role="model",
                parts=[types.Part(
                    text="You are a helpful SPARQL assistent. Your task is to answer the user question with the help of a knowledge graph. "
                    "You are provided with the result of a sparql query. And the data leading up the query. "
                    "Utilize only the provided information to answer the question."
                    # "If you find that you are missing information or cannot complete the task, describe your problem in detail."
            )]),
            types.Content(
                role="user",
                parts=[types.Part(
                    text=f"User Question:\n{question}\n"
                    f"SPARQL query and calling history:\n{self.get_calling_history(response_data)}\n"
                    f"Result:\n{sparql_result}"
                )]
            )
        ]
        logger.info("interpret SPARQL")
        logger.info(f"Prompt:\n{contents}")
        response = self.client.models.generate_content(
            model=self.generation_model,
            contents=contents,
            # config=self.config
        )
        logger.info(f"Response:\n{response.text}")

        return response


    def run(self, question):

        response = self.generate_sparql_from_question(question, verbose=True)
        for i in range(self.max_iterations):
            sparql = self.extract_sparql(response)
            success, sparql_result = self.execute_sparql(sparql)
            if success:
                # todo run another loop? how to evaluate the answer?
                return self.process_sparql_result(question, response, sparql_result)
            else:
                response = self.rework_sparql(question, response, sparql_result)


        return sparql_result


if __name__ == "__main__":
    ct_load_dict = {"uri": "irk:/ocse/0.2/control_theory", "prefix": "ct", "module_name": "control_theory"}
    ma_load_dict = {"uri": "irk:/ocse/0.2/math", "prefix": "ma", "module_name": "math"}
    nl_load_dict = {"path": os.path.join(BASE_DIR, "output.py"), "prefix": "nl", "module_name": "nl"}


    sa = SparqlAgent([ct_load_dict, ma_load_dict, nl_load_dict])
    # sa.setup_embeddings()
    res = sa.run("whats the connection between an equation and an inequation")


# todo space out llm call, avoid rate limit
# todo local llm?

