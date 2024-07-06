import os
from pathlib import Path
import re
import tomllib
import time
from jinja2 import Environment, FileSystemLoader

#! pip install google-generativeai
import google.generativeai as genai

from ipydex import IPS, activate_ips_on_exception

activate_ips_on_exception()


# TODO: this assumes package to be installed with pip install -e .
BASE_DIR = Path(__file__).parents[2].as_posix()
TEMPLATE_DIR = os.path.join(BASE_DIR, "data")

# config file starts with .git_config to prevent nextcloud synchronizing it to (unencrypted) cloud
CONFIG_PATH = os.path.join(BASE_DIR, ".git_config.toml")

class Container:
    pass

with open(CONFIG_PATH, "rb") as fp:
    config_dict = tomllib.load(fp)

# https://github.com/google-gemini/generative-ai-python
genai.configure(api_key=config_dict["gemeni_api_key"])
model = genai.GenerativeModel('gemini-1.5-pro-latest')

# - It would be useful if you also would generate comments to explain your "chain of thought".

def render_template(template: str, context: dict):
    """
    :param template:    path to template file relative to TEMPLATE_DIR
    :param context:     dict containing the data which should be inserted into the template
    """
    jin_env = Environment(
        loader=FileSystemLoader(TEMPLATE_DIR),
    )

    template_doc = jin_env.get_template(template)

    res = template_doc.render(context=context)

    return res


class MainManager:
    """
    Main class for this script to prevent global variables
    """

    def __init__(self, dev_mode: bool) -> None:

        self.dev_mode = dev_mode
        self.chunk_full_source = None
        self.resulting_statements = None

        self.processed_latex_source = None
        self.last_llm_result = None
        self.token_counter = 0

        self.llm_config = genai.GenerationConfig(temperature=0)

        self.get_data()

    def get_data(self):

        tex_path = os.path.join(BASE_DIR, "data", "chunk_full_source.tex")
        formalized_statements_path = os.path.join(BASE_DIR, "data", "formalized_statements0.md")

        with open(tex_path) as fp:
            self.chunk_full_source = fp.read()

        with open(formalized_statements_path) as fp:
            self.resulting_statements = fp.read()

    def main(self):

        # note: first snippet should be empty and last snippet is irrelevant (thus excluded)
        latex_snippets = nonconsuming_regex_split(r"% snippet\(.*?\)", self.chunk_full_source)[0:-1]
        assert latex_snippets[0].strip() == ""

        # indices of latex_snippets now correspond to enumeration in the source
        # e.g. latex_snippets[2] starts with "% snippet(2)"

        # initialize process:
        start_snippets_idx = 6  # the first snippet which is not included
        self.processed_latex_source = "".join(latex_snippets[:start_snippets_idx])


        for i in range(start_snippets_idx, len(latex_snippets)):
            j = i - start_snippets_idx
            if j >= 5:
                break
            new_latex_source = latex_snippets[i]
            context = self.create_context(new_latex_source)
            message = render_template("prompt01_template.md", context)

            tokens = model.count_tokens(message).total_tokens
            self.token_counter += tokens
            print(f"processing snippet{i:02d}, {tokens} tokens ({self.dev_mode=})")

            response = self.tracked_model_response(message, generation_config=self.llm_config)
            self.resulting_statements = "".join((self.resulting_statements, response.text))
            self.processed_latex_source = "".join((self.processed_latex_source, new_latex_source))

            with open(f"tmp{i:02d}.md", "w") as fp:
                fp.write(message)

            break

        with open(f"final_response_list.md", "w") as fp:
            fp.write(self.resulting_statements)
            fp.write(f"\n\n- // {self.token_counter} tokens were transmitted")

    def create_context(self, new_latex_source: str) -> dict:

        context = {
            "processed_latex_source": self.processed_latex_source,
            "resulting_statements": self.resulting_statements,
            "new_latex_source": new_latex_source,
        }

        return context


    def tracked_model_response(self, message, **kwargs):
        """
        if not in dev_mode:
            track the number of tokens we send to the model

        always:
            return an object with a .text attribute containing the model response
            (faked in case of dev_mode)
        """
        tokens = model.count_tokens(message).total_tokens
        track_line = f'{time.strftime("%Y-%m-%d %H:%M:%S")}, {tokens}\n'

        if not self.dev_mode:
            with open("_token_tracking.txt", "a") as fp:
                fp.write(track_line)
            res = model.generate_content(message, generation_config=self.llm_config)
        else:
            res = Container()
            res.text = f"\n\n-// snippet({0})\n- response text\n- response text"

        return res


# split without consuming the delimiter

def nonconsuming_regex_split(pattern, string):
    matches = list(re.finditer(pattern, string))

    starts = [0]
    ends = []

    for match in matches:
        i = match.start()
        starts.append(i)
        ends.append(i)
    ends.append(len(string))

    parts = []
    for i1, i2 in zip(starts, ends):
        parts.append(string[i1: i2])

    return parts


# this function is intended to be called from cli.py
def main(dev_mode):
    mm = MainManager(dev_mode)
    mm.main()
    # IPS(print_tb=False)
