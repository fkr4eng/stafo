import os
import re
import pyirk as p
import google.generativeai as genai

from stafo.utils import BASE_DIR, CONFIG_PATH, render_template
from stafo.core import llm_api

from ipydex import IPS, activate_ips_on_exception


nl_latex_path = os.path.join(BASE_DIR, "html", "nl_latex.tex")
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
    res2 = re.findall(r"(\\snippet\{" + str(i) + r"i?\})(.+?)(?=\Z|\\snippet)", latex_content, re.DOTALL)
    snip_str = res2[0][0]
    latex_snippet = res2[0][1]
    new_nl_content += fnl_snippet
    if "i" in res1[0][1] or "new section" in fnl_snippet.lower():
        new_latex_content += snip_str + "\n" + latex_snippet + "\n"
        print("skipping", i)
        continue


    context = {
        "fnl_statements": new_nl_content,
        "fnl_current": fnl_snippet,
        "latex_og": new_latex_content,
        "latex_current": latex_snippet,
    }
    message = render_template("prompt02b_annotate_equations_template.md", context)
    res = llm_api(message)
    new_latex_content += snip_str + "\n" + res + "\n"

def repl_func(mo):
    # wrong annotations by llm
    if not (mo.group(1).startswith("$") or mo.group(1).startswith("\\begin") or mo.group(1).startswith("\\[")):
        return mo.group(1)
    # having equation inside arg does not work -> add arg behind equation (llm perfoms way worse if this is the task)
    else:
        # group3 = re.sub(r"(?=[^$])\\sum_\{.+?\}\^.+? ", lambda x: f"${x.group(0)}$", mo.group(3))
        # todo find solution for this
        return mo.group(1) + "\\eqnote{concepts:" + mo.group(2) + "}{statement:" + mo.group(3) + "}"

new_latex_content = re.sub(r"\\eqnote\{(.+?)\}\{concepts:(.+?)\}\{statement:(.+?)\}", repl_func, new_latex_content, flags=re.DOTALL)

prelim = [
    "\\newcommand{\\setref}[2]{\\textcolor{red}{#1}\\textcolor{green}{#2}}",
    "\\newcommand{\\snippet}[1]{\\textbf{snippet #1}\\\\}",
    "\\newcommand{\\eqnote}[2]{\\textcolor{orange}{#1}\\textcolor{magenta}{#2}}"
]
context = {
    "preliminaries": prelim,
    "content": new_latex_content,
}
res = render_template("latex_template.py", context)

with open(os.path.join(BASE_DIR, "html", "nl_latex_copy.tex"), "wt", encoding="utf-8") as f:
    f.write(res)

IPS()