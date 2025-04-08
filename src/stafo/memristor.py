import pyirk as p
import os, sys
import re
from ipydex import IPS
from scholarly import scholarly
import google.generativeai as genai
import json


from .utils import BASE_DIR, CONFIG_PATH, render_template
from .core import llm_api
from .statement_to_kg import ConversionManager

def main():
    CM = ConversionManager(os.path.join(BASE_DIR, "data/memristor/empty.md"), num_keys=1000, load_irk_modules=["ag"])
    CM.step1_init()
    # step 1
    # parse Bibliography and return Authors and Titles
    paper_path = os.path.join(BASE_DIR, "data/memristor/2024/2024_bib.md")
    temp_path = os.path.join(BASE_DIR, "data/memristor/temp/tmp.json")
    CM.current_snippet = os.path.split(paper_path)[-1]

    with open(paper_path, "rt", encoding="utf-8") as f:
        content = f.read()

    use_scholarly = False


    for line in content.split("\n"):
        if line.startswith("-"):

            message = f"read the bib entry and generate a json file with the fields: citation_number, author, title, year, journal and fills those if possible. If there are multiple authors, return a list. Dont write ````json, just clean json code. Bib entry: {line}"
            res = llm_api(message)
            print(res)
            with open(temp_path, "wt", encoding="utf-8") as f:
                f.write(res)

            with open(temp_path, "rt", encoding="utf-8") as f:
                info = json.load(f)

            if use_scholarly:
                pubs = scholarly.search_pubs(info["title"] + " " + info["author"])
                pub = next(pubs)
                info["author"] = pub["bib"]["author"]
            else:
                pub = {"author_id": ["" for a in info["author"]]}


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
            CM.add_new_item(CM.d, info["title"][:20], "en", {
                "R4": 'ag.I6591["source document"]',
                "R8434": info["title"],
                "R8435": info["year"],
                "R8433": info["author"],
                })
            CM.render()

            # IPS()
            # sys.exit()
