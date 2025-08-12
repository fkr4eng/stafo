from rapidfuzz import fuzz, process, utils
from rapidfuzz.distance import Indel, JaroWinkler
import subprocess
import pyirk as p
from ipydex import IPS
import os
import re, regex
import numpy as np


from stafo.utils import BASE_DIR, CONFIG_PATH, render_template, del_latex_aux_files
from stafo.preprocessor import clean_tex_linebreaks

# paths
fnl_fpath = os.path.join(BASE_DIR, "data", "nichtlinear", "processed", "formalized_statements_nl.md")
module_fpath = os.path.join(BASE_DIR, "output.py")
# latex_fpath = os.path.join(BASE_DIR, "html", "kapitel_2_1.tex")
latex_fpath = os.path.join(BASE_DIR, "html", "nl_latex_copy.tex")
output_dir = os.path.join(BASE_DIR, "html", "res")


clean_tex_linebreaks(latex_fpath)
with open(latex_fpath, "rt", encoding="utf-8") as f:
    tex_source = f.read()

nl = p.irkloader.load_mod_from_path(module_fpath, "nl", "nonlinear")

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

relevant_words = re.findall(r"(?<=\{\\em ).+?(?=\})", tex_source, re.DOTALL) # DOTALL to manage arbitrary linebreaks in tex
relevant_words = [rw.replace("\n", " ") for rw in relevant_words]

# convert latex to html
cwd = os.getcwd()
fpath_head, fpath_tail = os.path.split(latex_fpath)
os.chdir(fpath_head)
os.makedirs(output_dir, exist_ok=True)
res = subprocess.run(["make4ht", fpath_tail, "--output-dir", output_dir, '"mathjax"'])
if res.returncode == 0:
    print("conversion finished.")
else:
    print("conversion failed!")
os.chdir(cwd)
# delete aux files
del_latex_aux_files(fpath_head, fpath_tail)

# load html
html_fpath = os.path.join(fpath_head, output_dir, fpath_tail.replace(".tex", ".html"))
with open(html_fpath, "rt", encoding="utf-8") as f:
    html_source = f.read()

# cleanup html
## converter leaves weird line breaks and unnecessary span elements that interfere with tooltip replacement
html_source = html_source.replace("<span \nclass", "<span class")
## html looks like this: <span class="some">Mat</span><span class="some">rix</span> which needs to be corrected
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

## remove duplicate whitespaces
html_source = re.sub(r" +", " ", html_source)

# add tooltip style
with open(os.path.join(fpath_head, "tt_style.html"), "rt", encoding="utf-8") as f:
    style = f.read()
html_source = html_source.replace("<head>", "<head>\n" + style)

# add tooltip
pattern = regex.compile(r"""
(?(DEFINE)                              # Define span pattern
  (?P<SPAN>
    <span\b[^>]*>                      # any opening <span ...>
      (?:
        [^<]+                          # text nodes
        | (?&SPAN)                     # nested <span>...</span> (recursion)
        | <(?!/span)[^>]+>             # any other opening tag (NOT a closing </span>)
      )*
    </span>
  )
)
<span\b[^>]*\bid=['"]textcolor\d+['"][^>]*>  # target opening tag with the given id
  (
    [^<]+
    | (?&SPAN)                              # allow nested spans (uses the DEFINEd group)
    | <(?!/span)[^>]+>
  )*
</span>
<span\b[^>]*\bid=['"]textcolor\d+['"][^>]*>  # target opening tag with the given id
  (
    [^<]+
    | (?&SPAN)                              # allow nested spans (uses the DEFINEd group)
    | <(?!/span)[^>]+>
  )*
</span>
""", regex.VERBOSE | regex.IGNORECASE)
def repl_func(matchobj):
    try:
        clean_tex = re.sub(r" +", " ", matchobj.group(0).replace("\n", " "))
        label = re.findall(r"(?<=label:).+?(?=<|$)", clean_tex, re.DOTALL)
        assert len(label) >= 1, f"label not found in {matchobj}"
        label = label[-1].replace("\n", " ").replace("'", "").replace('"', "").replace("’", "")
        item = p.ds.get_item_by_label(label)
        assert item is not None, f"no item found for label {label, matchobj}"
        short_key = item.short_key
        context = {"word": matchobj.group(2),
                "short_key": short_key,
        }
        tt = render_template("html_tooltip_template.html", context)
    except Exception as e:
        print(e)
        tt = matchobj.group(0) # to show whats not working
        # tt = matchobj.group(2) # during operation
    return tt

html_source = regex.sub(pattern, repl_func, html_source)


with open(html_fpath, "wt", encoding="utf-8") as f:
    f.write(html_source)

# visualize latex, FNL, pyirk at the same time
with open(module_fpath, "rt", encoding="utf-8") as f:
    module_source = f.read()
with open(fnl_fpath, "rt", encoding="utf-8") as f:
    fnl_source = f.read()

context = {"snippets": []}
max_num_snippets = int(re.findall(r"\\snippet\{(\d+)i?\}", tex_source)[-1])
for i in range(1, max_num_snippets):
    html_snip = re.findall(
        r'<p class="\w+?" ?> *<span class="cmbx-10">snippet '+str(i)+r'i?</span>.+?(?=<p class="\w+?" ?> *<span class="cmbx-10">snippet)',
        html_source,
        re.DOTALL)
    if len(html_snip) != 1:
        print(f"snippet {i} not found in latex, skipping")
        continue
    else:
        html_snip = html_snip[0]
    # maybe get rid of "snippet"
    html_snip = re.sub(r'<span class="cmbx-10">snippet '+str(i)+r'i?</span>', "", html_snip)

    fnl_snip = re.findall(f"- // snippet\({i}i?\).+?(?=- // snippet)", fnl_source, re.DOTALL)
    if len(fnl_snip) == 1:
        fnl_snip = fnl_snip[0]
    else:
        print(f"fnl snippet {i} not found")
        fnl_snip = ""
    module_snip = re.findall(f'# snippet\({i}i?\).+?(?=\Z|# snippet\({i+1})', module_source, re.DOTALL)
    if len(module_snip) == 1:
        module_snip = module_snip[0]
    else:
        print(f"module snippet {i} not found")
        module_snip = ""
    context["snippets"].append(
        {
            "snippet": i,
            "tex": html_snip,
            "fnl": fnl_snip,
            "pyirk": module_snip
        }
    )
res = render_template("markup_complete_template.py", context)
with open(os.path.join(output_dir, "Nichtlinear.html"), "wt", encoding="utf-8") as f:
    f.write(res)

if False:
    s = p.ds.get_item_by_label("snippet(16)")
    rels = list(s.get_inv_relations().keys())

    vm = p.visualization.vm
    for rel in rels:
        if "contains" in p.ds.get_entity_by_uri(rel).R1.value:
            vm.REL_BLACKLIST.append(rel)
    # this takes a lot of time
    vm.create_interactive_graph(output_dir=output_dir, skip_auto_items=True, skip_existing=False)

IPS()