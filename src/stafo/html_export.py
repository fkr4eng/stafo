from rapidfuzz import fuzz, process, utils
from rapidfuzz.distance import Indel, JaroWinkler
import subprocess
import pyirk as p
from ipydex import IPS
import os
import re, regex
import numpy as np


from stafo.utils import BASE_DIR, CONFIG_PATH, render_template, cleanup_after_latex
from stafo.preprocessor import clean_tex_linebreaks

fpath = os.path.join(BASE_DIR, "html", "kapitel_2_1.tex")
clean_tex_linebreaks(fpath)
output_dir = os.path.join(BASE_DIR, "html", "res")
with open(fpath, "rt", encoding="utf-8") as f:
    tex_source = f.read()

nl = p.irkloader.load_mod_from_path("output.py", "nl", "nonlinear")

relevant_items = []
all_items = p.ds.items
for uri, item in all_items.items():
    if "agents" in uri or "control_theory" in uri:
        continue
    # get rid of automatically created items
    if "a" in item.short_key:
        continue
    # get rid of stuff from statements
    if item.get_relations("R20"):
        continue
    # get rid of statements for now
    if p.is_instance_of(item, p.I14, strict=False):
        continue
    relevant_items.append(item)


item_label_list = []
for item in relevant_items:
    item_label_list.append([item, item.R1.value])
    for literal in item.get_relations("R77", return_obj=True):
        item_label_list.append([item, literal.value])
item_label_list = np.array(item_label_list)

relevant_words = re.findall(r"(?<=\{\\em ).+?(?=\})", tex_source, re.DOTALL) # due to arbitrary linebreaks in tex
relevant_words = [rw.replace("\n", " ") for rw in relevant_words]

# convert latex to html
cwd = os.getcwd()
fpath_head, fpath_tail = os.path.split(fpath)
os.chdir(fpath_head)
os.makedirs(output_dir, exist_ok=True)
res = subprocess.run(["make4ht", fpath_tail, "--output-dir", output_dir, '"mathjax"'])
if res.returncode == 0:
    print("conversion finished.")
else:
    print("conversion failed!")
os.chdir(cwd)
# delete aux files
cleanup_after_latex(fpath_head, fpath_tail)

# load html
html_fpath = os.path.join(fpath_head, output_dir, fpath_tail.replace(".tex", ".html"))
with open(html_fpath, "rt", encoding="utf-8") as f:
    html_source = f.read()

# cleanup html
## converter leaves weird line breaks and unnecessary span elements that interfere with tooltip replacement
html_source = html_source.replace("<span \nclass", "<span class")

def repl_func(matchobj):
    res = ""
    for i in range(1,6):
        res += matchobj.group(i)
    return res.replace("\n", " ")
old_html = ""
i = 0
while old_html != html_source:
    i += 1
    old_html = html_source
    html_source = re.sub(r'(<span \n?class=)(?P<classname>.+?)(>.+?)</span>(\n?)<span \n?class=(?P=classname)>(.+?</span>)', repl_func, html_source)
    if old_html == html_source:
        print("done")
    else:
        print(i)
html_source = html_source.replace(" ", " ")

# add tooltip style
with open(os.path.join(fpath_head, "tt_style.html"), "rt", encoding="utf-8") as f:
    style = f.read()
html_source = html_source.replace("<head>", "<head>\n" + style)

# add tooltip
## replace long words first to avoid partial replacements
for word in sorted(relevant_words, key=len, reverse=True):
    # https://rapidfuzz.github.io/RapidFuzz/Usage/distance/Indel.html#normalized-similarity
    res = process.extractOne(word, item_label_list[:,1], scorer=JaroWinkler.normalized_similarity, processor=utils.default_process, score_cutoff=0.8)
    if res:
        context = {"word": word,
                # "tooltip": repr(item_label_list[res[2],0]).replace("<", "&lt").replace(">", "&gt")
                "tooltip": f'<iframe src="{item_label_list[res[2],0].short_key}.html"></iframe>',
                "link": f"{item_label_list[res[2],0].short_key}.html",
        }
        tt = render_template("html_tooltip_template.html", context)

        # use regex for variable length lookbehind assertion. avoid replacing the label of I123["label"]
        # be careful with labels in equations, they will not render if replaced with tooltip
        # prevent double replacement
        html_source = regex.sub(r'(?<!class="tooltip">|\["|\\label \{[^\}]+?)'+word+r'(?!<span class="tooltiptext">|"\])', tt, html_source)
        # html_source = html_source.replace(word, tt)

with open(html_fpath, "wt", encoding="utf-8") as f:
    f.write(html_source)

if False:
    # this takes a lot of time
    p.visualization.create_interactive_graph(output_dir=output_dir, skip_auto_items=True, skip_existing=True)

IPS()