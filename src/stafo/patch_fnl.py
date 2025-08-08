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


new_nl_content = ""
for i in range(1, 51):
    res = re.findall(f"(- // snippet\({i}(i?)\).+?)(?=- // snippet)", nl_content, re.DOTALL)
    snippet = res[0][0]
    new_nl_content += snippet
    if "i" in res[0][1]:
        continue
    if "new section" in snippet.lower():
        continue
    context = {
        "fnl_statements": new_nl_content,
        "current_snippet": snippet,
    }
    message = render_template("prompt03_patch_old_fnl_template.md", context)
    res = llm_api(message)
    new_nl_content += res + "\n"
with open(os.path.join(os.path.split(nl_fnl_path)[0], "nl_fnl_copy.md"), "wt", encoding="utf-8") as f:
    f.write(new_nl_content)

1