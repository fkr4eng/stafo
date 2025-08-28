from rapidfuzz import fuzz, process, utils
from rapidfuzz.distance import Indel, JaroWinkler
import subprocess
import pyirk as p
from ipydex import IPS
import os
import re, regex
import numpy as np
import pickle
import shutil

from stafo.utils import BASE_DIR, CONFIG_PATH, render_template, del_latex_aux_files
from stafo.preprocessor import clean_tex_linebreaks

# paths
fnl_fpath = os.path.join(BASE_DIR, "data", "nichtlinear", "processed", "formalized_statements_nl.md")
module_fpath = os.path.join(BASE_DIR, "output.py")
latex_nl_fpath = os.path.join(BASE_DIR, "data", "nichtlinear", "processed", "kapitel2_annotated.tex")
latex_fpath = os.path.join(BASE_DIR, "html", "nl_latex_copy.tex")
output_dir = os.path.join(BASE_DIR, "html", "res")

# copy latest annotated latex file to working dir
shutil.copy(latex_nl_fpath, latex_fpath)


def create_html():
    clean_tex_linebreaks(latex_fpath)
    with open(latex_fpath, "rt", encoding="utf-8") as f:
        tex_source = f.read()
    print("loading irk module ...")
    nl = p.irkloader.load_mod_from_path(module_fpath, "nl", "nonlinear", reuse_loaded=True)
    print("done")
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

    tex_source = re.sub(r"\\ref\{eq:", r"\\eqref{eq:", tex_source)
    if "bibliography" not in tex_source:
        tex_source = re.sub(r"\\end\{document\}", r"aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa\n\\bibliographystyle{abbrv}\n\\bibliography{dynamic}\n\\end{document}", tex_source)

    with open(latex_fpath, "wt", encoding="utf-8") as f:
        f.write(tex_source)


    # convert latex to html
    cwd = os.getcwd()
    fpath_head, fpath_tail = os.path.split(latex_fpath)
    os.chdir(fpath_head)
    os.makedirs(output_dir, exist_ok=True)
    res = subprocess.run(["make4ht", fpath_tail, "--output-dir", output_dir, '"mathjax"', "--config", "config.cfg"])
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
    html_source_og = html_source # for debugging
    # cleanup html
    ## converter leaves weird line breaks and unnecessary span elements that interfere with tooltip replacement
    html_source = html_source.replace("<span \nclass", "<span class")
    ## html looks like this: <span class="some">Mat</span><span class="some">rix</span> which needs to be corrected
    def repl_func_cleanup(matchobj):
        res = ""
        for i in range(1,6):
            res += matchobj.group(i)
        return res.replace("\n", " ")
    old_html = ""
    i = 0
    while old_html != html_source:
        i += 1
        old_html = html_source
        html_source = re.sub(r'(<span \n?class=)(?P<classname>[^>]+?)(>[^<]+?)</span>([ \n]*)<span \n?class=(?P=classname)>([^<]+?</span>)', repl_func_cleanup, html_source)
        if old_html == html_source:
            print("done")
        else:
            print(i)

    ## remove duplicate whitespaces
    html_source = re.sub(r" +", " ", html_source)

    with open("fnl_dict.pcl", "rb") as f:
        fnl_dict = pickle.load(f)

    # add tooltip style
    # todo depricated
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
    def add_tt_concept(word, t):
        word = word.replace("\n", " ").replace("'", "").replace('"', "").replace("’", "")
        item = get_item_by_name(word)
        if item is not None:
            short_key = item.short_key
            context = {"word": word, "short_key": short_key, "inner": True}
            t += render_template("html_tooltip_template.html", context) + "&nbsp;"
        else:
            print(f"no item found in {word}")
            t += word + "&nbsp;"
        return t

    def get_item_by_name(name):
        if name in fnl_dict["items"].keys():
            d = fnl_dict["items"][name]
        elif name in fnl_dict["relations"].keys():
            d = fnl_dict["relations"][name]
        else:
            return None
        key = d['key']
        if pre :=d["prefix"]:
            if pre == "p":
                pre = "bi"
        else:
            pre = "nl"
        base_uri = p.ds.uri_prefix_mapping.b[pre]
        uri = base_uri + "#" + key
        item = p.ds.get_entity_by_uri(uri)
        return item

    def repl_statement(mo):
        item = get_item_by_name(mo.group(1))
        if item is not None:
            short_key = item.short_key
            context = {"word": mo.group(1), "short_key": short_key, "inner": True}
            t = render_template("html_tooltip_template.html", context) + "&nbsp;"
        else:
            print(f"no item found in {mo.group(1)}")
            t = mo.group(1) + "&nbsp;"
        return t

    def repl_func(matchobj):
        #! keep in mind: the pattern always matches an empty string as group(1)
        clean_html = re.sub(r" +", " ", matchobj.group(0).replace("\n", " "))
        # label annotation
        if "label" in clean_html:
            try:
                label = re.findall(r"(?<=label:).+?(?=<|$)", clean_html, re.DOTALL)
                assert len(label) >= 1, f"label not found in {matchobj}"
                label = label[-1].replace("\n", " ").replace("'", "").replace('"', "").replace("’", "")
                item = get_item_by_name(label)
                assert item is not None, f"no item found for label {label, matchobj}"
                short_key = item.short_key
                context = {"word": matchobj.group(2),
                        "short_key": short_key,
                        "inner": False,
                }
                tt = render_template("html_tooltip_template.html", context)
            except Exception as e:
                print(e)
                tt = matchobj.group(0) # to show whats not working
                # tt = matchobj.group(2) # during operation
        # equation annotation
        elif "concepts" in clean_html:
            concepts = ""
            gr2 = re.sub(r"  +", " ", matchobj.group(2).replace("\n", " "))
            for word in re.findall(r"’(.+?)’", gr2, re.DOTALL):
                concepts = add_tt_concept(word, concepts)
            gr3 = re.sub(r"  +", " ", matchobj.group(3).replace("\n", " "))
            stm = re.sub(r"’(.+?)’", repl_statement, gr3, flags=re.DOTALL)
            if stm == gr3:
                statement = ""
            else:
                statement = stm

            context = {
                "img_path": os.path.join(BASE_DIR, "html", "info.png"),
                "concepts": concepts,
                "statement": statement
            }
            tt = render_template("html_equation_info_template.html", context)
        else:
            print("ignored content:", matchobj.group(0))
        return tt

    html_source = regex.sub(pattern, repl_func, html_source)

    # put icon and equations on same line
    pat = regex.compile(r"""
    (?(DEFINE)                              # Define span pattern
    (?P<SPAN>
        <span\b[^>]*>                      # any opening <span ...>
        (?:
            [^<]+                          # text nodes
            | (?&SPAN)                     # nested <span>...</span> (recursion)
            | <(?!/span)[^>]+>             # any other opening tag (NOT a closing </span>)
        )*
        </span>
    ))
    <div\ class="mathjax\ equation">
    (?:
        [^<]+
        | <(?!/div)
    )+?</div>[\ \n]*<span\ class="tooltip">
    (?:
        [^<]+
        | (?&SPAN)                              # allow nested spans (uses the DEFINEd group)
        | <(?!/span)[^>]+>
    )*
    </span>                              # allow nested spans (uses the DEFINEd group)
    """, regex.VERBOSE | regex.IGNORECASE | re.DOTALL)
    def div_repl(mo):
        return f"""<div class="horizontal">{mo.group(0)}</div>"""
    html_source = regex.sub(pat, div_repl, html_source)




    with open(html_fpath, "wt", encoding="utf-8") as f:
        f.write(html_source)

    # visualize latex, FNL, pyirk at the same time
    with open(module_fpath, "rt", encoding="utf-8") as f:
        module_source = f.read()
    with open(fnl_fpath, "rt", encoding="utf-8") as f:
        fnl_source = f.read()

    context = {"snippets": [], "css_name": fpath_tail.replace(".tex", ".css")}
    max_num_snippets = int(re.findall(r"\\snippet\{(\d+)i?\}", tex_source)[-1])
    for i in range(1, max_num_snippets+1):
    # for i in range(1, 7):
        # get html snippet
        if i == 17:
            pass
        html_snip = re.findall(
            r'<p class="\w+?" ?> *<span class="cmbx-10">snippet '+str(i)+r'i?</span>.+?(?=<p class="\w+?" ?> *<span class="cmbx-10">snippet|<p class="\w+?" ?> *aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa)',
            html_source,
            re.DOTALL)
        if len(html_snip) != 1:
            print(f"snippet {i} not found in html, skipping")
            continue
        else:
            html_snip = html_snip[0]

        # html converter spits out more </div> than <div> elements
        # remove access ones.
        if html_snip.count("</div>") > html_snip.count("<div"):
            pass

        # get rid of "snippet"
        html_snip = re.sub(r'<span class="cmbx-10">snippet '+str(i)+r'i?</span>', "", html_snip)

        # get fnl snippet
        fnl_snip = re.findall(f"- // snippet\({i}i?\).+?(?=- // snippet)", fnl_source, re.DOTALL)
        if len(fnl_snip) == 1:
            fnl_snip = fnl_snip[0]
        else:
            print(f"fnl snippet {i} not found")
            fnl_snip = ""

        # get module snippet
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
    context["bib"] = re.findall(r"(?<=aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa\n</p>)(.+?)(?=</body>)", html_source, re.DOTALL)[0]

    res = render_template("markup_complete_template.html", context)
    with open(os.path.join(output_dir, "Nichtlinear.html"), "wt", encoding="utf-8") as f:
        f.write(res)
    1

def create_graph():
    nl = p.irkloader.load_mod_from_path(module_fpath, "nl", "nonlinear", reuse_loaded=True)

    s = p.ds.get_item_by_label("snippet(16)")
    rels = list(s.get_relations().keys())

    vm = p.visualization.vm
    for rel in rels:
        if "contains" in p.ds.get_entity_by_uri(rel).R1.value:
            vm.REL_BLACKLIST.append(rel)
    # this takes a lot of time
    vm.create_interactive_graph(output_dir=output_dir, skip_auto_items=True, skip_existing=False, vis_relations=True)
if True:
    create_html()
if False:
    create_graph()
IPS()