import pyirk as p
import os, sys
import re
from ipydex import IPS, Container
from scholarly import scholarly
import google.generativeai as genai
import json
import pandas as pd
import cachewrapper as cw


from .utils import BASE_DIR, CONFIG_PATH, render_template
from .core import llm_api
from .statement_to_kg import ConversionManager

llm_cache_path = "llm_cache.pcl"

def main():
    CM = ConversionManager(os.path.join(BASE_DIR, "data/memristor/formalized_statements.md"), num_keys=1000, load_irk_modules=["ag"])
    CM.step1_init()
    CM.step2_parse_fnl()
    CM.current_snippet = "mem"
    # step 1
    # parse Bibliography and return Authors and Titles

    compare_publication_folders = ["2019", "2024"]
    publist = ""

    for name in compare_publication_folders:
        publist += "\n"
        bib_path = os.path.join(BASE_DIR, f"data/memristor/{name}/bib.md")
        table_path = os.path.join(BASE_DIR, f"data/memristor/{name}/table.md")
        meta_path = os.path.join(BASE_DIR, f"data/memristor/{name}/meta.json")

        temp_path = os.path.join(BASE_DIR, f"data/memristor/temp/tmp.json")
        CM.current_snippet = name

        citation_dict = {}

        # read table
        ########################################################################
        with open(table_path, "rt", encoding="utf-8") as f:
            df = pd.read_csv(f, delimiter="|")
        d = {}
        for head in df.columns:
            d[head] = head.strip()
        df = df.rename(columns=d, errors="raise")

        # drop useless columns left of source
        for colname in df.columns:
            if "Source" in colname:
                break
            else:
                df = df.drop(columns=[colname])

        # drop separation row
        df = df.drop(index=0)

        # extract citation numbers
        _relevant_citations = []
        for cite in df["Source"]:
            if "," in cite:
                _relevant_citations.extend(cite.split(","))
            else:
                _relevant_citations.append(cite)
        # convert to int
        relevant_citations = []
        for i, rc in enumerate(_relevant_citations):
            try:
                relevant_citations.append(int(rc))
            except ValueError:
                # this happens when in the source column the entry looks like this: "219,"
                pass

        # create publication entry
        with open(meta_path, "rt") as f:
            meta_infos = json.load(f)
        pub_dict = {"R4": 'ag.I6591["source document"]'}
        if meta_infos["author"]:
            pub_dict["R8433"] = meta_infos["author"]
        if meta_infos["title"]:
            pub_dict["R8434"] = meta_infos["title"]
        if meta_infos["year"]:
            pub_dict["R8435"] = meta_infos["year"]
        og_pub_id = "publication: " + meta_infos["title"]
        CM.add_new_item(CM.d, og_pub_id, "en", pub_dict)




        # parse citations
        ########################################################################
        with open(bib_path, "rt", encoding="utf-8") as f:
            content = f.read()

        use_scholarly = False

        llm_container = Container()
        llm_container.llm_api = llm_api
        cached_llm_container = cw.CacheWrapper(llm_container)

        for i, line in enumerate(content.split("\n")):
            if i < 120:
                # continue
                pass
            if i == 129:
                pass
            if line.startswith("-"):

                message = f"read the bib entry and generate a json file with the fields: citation_number, author, title, \
                    year, journal and fills those if possible. The data type of the field author is always a list \
                    (it might only have one entry or even zero entries). Dont write ````json, just clean json code. \
                    Bib entry: {line}"

                if os.path.isfile(llm_cache_path):
                    cached_llm_container.load_cache(llm_cache_path)
                res = cached_llm_container.llm_api(message)
                cached_llm_container.save_cache(llm_cache_path)

                print(res)
                if "`json" in res:
                    res = res.replace("`json", "").replace("`", "")
                info = json.loads(res)

                # skip if dict is empty for some reason (probably bad bib file)
                if not info:
                    continue
                # skip if citation is not in table
                if info["citation_number"] not in relevant_citations:
                    continue

                # get coauthors
                if use_scholarly:
                    pubs = scholarly.search_pubs(info["title"] + " " + info["author"])
                    pub = next(pubs)
                    info["author"] = pub["bib"]["author"]
                else:
                    # get rid of et al
                    if 'et al.' in info["author"]:
                        info["author"].remove('et al.')
                    # ensure compatibility with scholarly
                    pub = {"author_id": ["" for a in info["author"]]}

                # create new author item
                if not isinstance(info["author"], list): info["author"] = [info["author"]]
                for author, author_id in zip(info["author"], pub["author_id"]):
                    if not author in CM.d["items"].keys():
                        if use_scholarly and author_id:
                            auth = scholarly.search_author_id(author_id)
                            message = f"read the following name and generate json code with the fields: title, family_name, given_name and fills those if possible. Dont write ````json, just clean json code. {auth['name']}"
                            res = llm_api(message)
                            name_json = json.loads(res)
                            CM.add_new_item(CM.d, author, "en", {
                                "R4": 'ag.I7435["human"]',
                                "R7781": name_json["family_name"],
                                "R7782": name_json["given_name"],
                                "R3476": author_id,
                                })
                        else:
                            CM.add_new_item(CM.d, author, "en", {"R4": 'ag.I7435["human"]', "R7781": author})

                # create new publication item
                pub_dict = {"R4": 'ag.I6591["source document"]', "citation_number": info["citation_number"]}
                if info["author"]:
                    pub_dict["R8433"] = info["author"]
                if info["title"]:
                    pub_dict["R8434"] = info["title"]
                else:
                    continue
                if info["year"]:
                    pub_dict["R8435"] = info["year"]
                pub_id = "publication: " + info["title"]
                CM.add_new_item(CM.d, pub_id, "en", pub_dict)

                # add citation to examined publication
                CM.add_relation_inplace(CM.d["items"][og_pub_id], "R8440", pub_id)


                publist += line + "\n"
                citation_dict[info["citation_number"]] = pub_id

                # save dict
                with open(temp_path, "wt", encoding="utf-8") as f:
                    json.dump(CM.d, f)

        CM.render()

        # with open(table_path, "rt", encoding="utf-8") as f:
        #     table_content = f.read()
        # col_heads = []
        # works_col = None

        # header_line = 0
        # for i, line in enumerate(table_content.split("\n")):
        #     # header
        #     if i == header_line:
        #         col_heads = line.split("|")
        #         for i, h in enumerate(col_heads):
        #             col_heads[i] = h.strip()
        #             if "work(s)" in h.lower():
        #                 works_col = i

        #         for h in col_heads[works_col+1:]:
        #             label = "has " + h
        #             CM.add_new_rel(CM.d, label, "en")

        #     # a real line, not the separation line of the header
        #     elif line.count("-") < 20:
        #         content = line.split("|")
        #         for i, entry in enumerate(content[works_col+1:]):
        #             rel_key = 0

    # with open("publist.txt", "wt", encoding="utf-8") as f:
    #     f.write(publist)