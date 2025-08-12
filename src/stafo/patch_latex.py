import os
import re
import pyirk as p
import google.generativeai as genai

from stafo.utils import BASE_DIR, CONFIG_PATH, render_template
from stafo.core import llm_api

from ipydex import IPS, activate_ips_on_exception


nl_latex_path = os.path.join(BASE_DIR, "data", "nichtlinear", "processed", "kapitel2.tex")
nl_fnl_path = os.path.join(BASE_DIR, "data", "nichtlinear", "processed", "formalized_statements_nl.md")
with open(nl_fnl_path, "rt", encoding="utf-8") as f:
    nl_content = f.read()
with open(nl_latex_path, "rt", encoding="utf-8") as f:
    latex_content = f.read()

new_latex_content = ""
new_nl_content = ""
for i in range(1, 51):
    print(i)
    res1 = re.findall(f"(- // snippet\({i}(i?)\).+?)(?=- // snippet)", nl_content, re.DOTALL)
    fnl_snippet = res1[0][0]
    res2 = re.findall(r"(\\snippet\{" + str(i) + r"i?\})(.+?)(?=\\snippet)", latex_content, re.DOTALL)
    latex_snippet = res2[0][1]
    new_nl_content += fnl_snippet
    if "i" in res1[0][1] or "new section" in fnl_snippet.lower():
        new_latex_content += latex_snippet + "\n"
        print("skipping", i)
        continue


    context = {
        "fnl_statements": new_nl_content,
        "fnl_current": fnl_snippet,
        "latex_og": new_latex_content,
        "latex_current": latex_snippet,
    }
    message = render_template("prompt02_annotate_latex_template.md", context)
    res = llm_api(message)
    new_latex_content += res + "\n"


prelim = ["\\newcommand{\setref}[2]{\\textcolor{red}{#1}\\textcolor{green}{#2}}"]
context = {
    "preliminaries": prelim,
    "content": new_latex_content,
}
res = render_template("latex_template.py", context)

with open(os.path.join(BASE_DIR, "html", "nl_latex_copy.tex"), "wt", encoding="utf-8") as f:
    f.write(res)

1