import os
from typing import Dict, List
from pathlib import Path
import re

try:
    # available in python >=3.11
    import tomllib
except ModuleNotFoundError:
    # this is for python3.10
    import tomli as tomllib

import time

#! pip install google-generativeai
import google.generativeai as genai

from .utils import BASE_DIR, CONFIG_PATH, render_template

from ipydex import IPS, activate_ips_on_exception

activate_ips_on_exception()


SNIPPET_LATEX_MACRO_PATTERN = r"\\snippet{(.*?)}"
SNIPPET_MD_COMMENT_PATTERN = r"- // snippet\((.*?)\)"

class Container:
    pass

with open(CONFIG_PATH, "rb") as fp:
    config_dict = tomllib.load(fp)

# https://github.com/google-gemini/generative-ai-python
genai.configure(api_key=config_dict["gemini_api_key"])
model = genai.GenerativeModel('gemini-1.5-pro-latest')

# - It would be useful if you also would generate comments to explain your "chain of thought".


class MainManager:
    """
    Main class for this script to prevent global variables
    """

    def __init__(
            self,
            dev_mode: bool,
            tex_fpath: str = None,
            statement_fpath: str = None,
            snapshot_fpath: str = None,
            interactive_mode: bool = False,
        ) -> None:

        self.dev_mode = dev_mode
        self.interactive_mode = interactive_mode
        self.tex_source = None
        self.statement_source = None
        self.snapshot_fpath = None

        self.processed_latex_source = None
        self.last_llm_result = None
        self.token_counter = 0
        self.tex_snippet_list = None
        self.token_count_cache: Dict[str, int] = {}

        # will refer to the currently processed snippet
        self.snippet_object: LatexSourceSnippet = None

        self.llm_config = genai.GenerationConfig(temperature=0)

        # prepare the paths
        self.tex_fpath = os.path.join(BASE_DIR, "data", "chunk_full_source.tex") if tex_fpath is None else tex_fpath
        self.annotated_tex_fpath = self.tex_fpath.replace(".tex", "_annotated.tex")
        self.statement_fpath = \
            os.path.join(BASE_DIR, "data", "formalized_statements0.md") if statement_fpath is None else statement_fpath
        self.snapshot_fpath = \
            os.path.join(BASE_DIR, "snapshots", "math") if snapshot_fpath is None else snapshot_fpath
        os.makedirs(self.snapshot_fpath, exist_ok=True)

        self.get_data()

    def get_data(self):

        with open(self.tex_fpath, "rt", encoding="utf-8") as fp:
            self.tex_source = fp.read()

        with open(self.statement_fpath, "rt", encoding="utf-8") as fp:
            self.statement_source = fp.read()

        # note: first snippet should be empty and last snippet is irrelevant (thus excluded)
        self.tex_snippet_list = nonconsuming_regex_split(SNIPPET_LATEX_MACRO_PATTERN, self.tex_source)[0:-1]
        assert self.tex_snippet_list[0].strip() == ""

        # for the statements the last snippet is relevant
        self.statement_snippet_list = nonconsuming_regex_split(SNIPPET_MD_COMMENT_PATTERN, self.statement_source)
        # assert self.statement_snippet_list[0].strip() == ""

        # indices of latex_snippets now correspond to enumeration in the source
        # e.g. latex_snippets[2] starts with "% snippet(2)"

        # initialize iteration process:
        self.start_snippet_idx = len(self.statement_snippet_list)  # the first snippet which is not included
        self.processed_latex_source = "".join(self.tex_snippet_list[:self.start_snippet_idx])


    def make_snapshot(self, source, snippet_number):
        snapshot_file_names = os.listdir(self.snapshot_fpath)
        if len(snapshot_file_names) == 0:
            fname = f"sn{snippet_number}_0.md"
        else:
            if f"sn{snippet_number}" in snapshot_file_names[-1]:
                n = int(snapshot_file_names[-1].split("_")[-1].split(".")[0]) + 1
                fname = f"sn{snippet_number}_{n}.md"
            else:
                fname = f"sn{snippet_number}_0.md"

        fullpath = os.path.join(self.snapshot_fpath, fname)
        with open(fullpath, "wt", encoding="utf-8") as fp:
            fp.write(self.statement_source)
        print(f"Snapshot {fullpath} written")

    def do_next_query_iteration(self):
        self.continue_mode = False

        # look for "// please continue" or "// pc" in last nonempty line
        last_line = self.statement_snippet_list[-1].strip().split("\n")[-1].strip()

        if last_line in ("// please continue", "// pc"):
            if last_line == "// pc":
                self.statement_snippet_list[-1] = self.statement_snippet_list[-1].replace("\n// pc", "\n// please continue")
                self.statement_source = "".join(self.statement_snippet_list)

            self.continue_mode = True
            i = len(self.statement_snippet_list) - 1
        else:
            i = len(self.statement_snippet_list)

        return self.iteration_step(i)

    def iteration_step(self, i):

        new_latex_source = self.tex_snippet_list[i]

        look_ahead_latex_source = self.get_look_ahead_latex_source(i)
        context = self.create_context(new_latex_source, look_ahead_latex_source)
        message = render_template("prompt01_template_german.md", context)

        # do not make an llm-call if snippet should be ignored
        self.snippet_object = LatexSourceSnippet(new_latex_source)

        tokens = self.count_tokens(message)
        self.token_counter += tokens
        print(f"processing snippet {i:02d}, {tokens} tokens ({self.dev_mode=})")
        if self.interactive_mode:
            print(new_latex_source)

        response = self.tracked_model_response(message, generation_config=self.llm_config)

        # make snapshot before and after response
        self.make_snapshot(self.statement_source, self.start_snippet_idx-1)
        self.statement_source = "\n".join((self.statement_source, response.text))
        self.make_snapshot(self.statement_source, self.start_snippet_idx)

        if self.interactive_mode:
            print(f"Response:\n\n{response.text}")
            with open(self.statement_fpath, "wt", encoding="utf-8") as fp:
                fp.write(self.statement_source)
            print(f"{self.statement_fpath} written")

        # this should be joined via the empty string to recreate the original latex code
        self.processed_latex_source = "".join((self.processed_latex_source, new_latex_source))

        print("Now adapt fnl, before latex is annoated.")
        IPS()
        # todo case for ignored snippet
        # reload statement_source
        with open(self.statement_fpath, "rt", encoding="utf-8") as fp:
            self.statement_source = fp.read()

        # postprocess latex code to make annotations
        context2 = {
            "fnl_statements": self.statement_source,
            "fnl_current": response.text,
            "latex_og": "".join(self.tex_snippet_list[:i]),
            "latex_current": new_latex_source,
        }
        message2 = render_template("prompt02_annotate_latex_template.md", context2)
        response2 = self.tracked_model_response(message2, generation_config=self.llm_config)

        context3 = {
            "fnl_statements": self.statement_source,
            "fnl_current": response.text,
            "latex_og": "".join(self.tex_snippet_list[:i]),
            "latex_current": response2.text,
        }
        message3 = render_template("prompt02b_annotate_equations_template.md", context3)
        response3 = self.tracked_model_response(message3, generation_config=self.llm_config)

        def repl_func(mo):
            # wrong annotations by llm
            if not (mo.group(1).startswith("$") or mo.group(1).startswith("\\begin") or mo.group(1).startswith("\\[")):
                return mo.group(1)
            # having equation inside arg does not work -> add arg behind equation (llm perfoms way worse if this is the task)
            else:
                # group3 = re.sub(r"(?=[^$])\\sum_\{.+?\}\^.+? ", lambda x: f"${x.group(0)}$", mo.group(3))
                # todo find solution for this
                return mo.group(1) + "\\eqnote{concepts:" + mo.group(2) + "}{statement:" + mo.group(3) + "}"

        new_latex_content = re.sub(r"\\eqnote\{(.+?)\}\{concepts:(.+?)\}\{statement:(.+?)\}", repl_func, response3.text, flags=re.DOTALL)



        IPS()
        with open(self.annotated_tex_fpath, "rt", encoding="utf-8") as f:
            annotated_tex = f.read()

        annotated_tex = annotated_tex.replace("\end{document}", new_latex_content + "\n\end{document}")

        with open(self.annotated_tex_fpath, "wt", encoding="utf-8") as f:
            f.write(annotated_tex)


        # write the message for debugging

        tmp_fname = f"tmp{i:02d}.md"
        with open(tmp_fname, "wt", encoding="utf-8") as fp:
            fp.write(message)
            print(f"{tmp_fname} written")

    def main(self):
        """
        Unsupervised iteration over snippets
        """

        for i in range(self.start_snippet_idx, len(self.tex_snippet_list)):
            j = i - self.start_snippet_idx
            if j >= 5:
                break
            self.iteration_step(i)

        with open(f"final_response_list.md", "wt", encoding="utf-8") as fp:
            fp.write(self.statement_source)
            fp.write(f"\n\n- // {self.token_counter} tokens were transmitted")

    def get_look_ahead_latex_source(self, i: int) -> str:
        # number of look-ahead-snippets
        N = 2

        # note: this slice does not result in an IndexError even if i+1 would be too big
        # the result is just an empty list
        rest: list = self.tex_snippet_list[i+1:i + 1+ N]
        if len(rest) < N:
            rest.append("\n\n% This is the end of the LaTeX code of this section.")

        result = "".join(rest)
        return result

    def create_context(self, new_latex_source: str, look_ahead_latex_source: str) -> dict:
        # first remove todos from statement source, otherwise llm will annotate todos instead of solving them
        pattern = re.compile(r"// ?(?:todo|TODO).+$", re.MULTILINE)
        statement_source = re.sub(pattern, "", self.statement_source)

        context = {
            "processed_latex_source": self.processed_latex_source,
            "resulting_statements": statement_source,
            "new_latex_source": new_latex_source,
            "look_ahead_latex_source": look_ahead_latex_source,
            "continue_mode": self.continue_mode,
        }

        return context

    def count_tokens(self, message: str) -> int:

        # speed up the process
        cached_result = self.token_count_cache.get(message)
        if cached_result is not None:
            return cached_result

        if self.dev_mode:
            res = 1000
        else:
            res = model.count_tokens(message).total_tokens

        self.token_count_cache[message] = res
        return res



    def tracked_model_response(self, message, **kwargs):
        """
        if ignore_flag:
            return the already known answer ("ignored content")
        if not in dev_mode:
            track the number of tokens we send to the model

        always:
            return an object with a .text attribute containing the model response
            (faked in case of dev_mode)
        """
        tokens = self.count_tokens(message)
        track_line = f'{time.strftime("%Y-%m-%d %H:%M:%S")}, {tokens}\n'

        res = Container()

        if self.snippet_object.ignore_flag:
            res.text = f"- // snippet({self.snippet_object.snippet_delimiter_inner_content})\n- // ignored content"
        elif not self.dev_mode:
            with open("_token_tracking.txt", "a") as fp:
                fp.write(track_line)
            res = model.generate_content(message, generation_config=self.llm_config)
        else:
            res.text = f"- // snippet({self.snippet_object.snippet_delimiter_inner_content})\n- response text\n- response text\n"

        return res

    def llm_task(self):
        self.get_data()
        task_pattern = re.compile(r"- // llm:?(.+)")
        res = re.findall(task_pattern, self.statement_source)
        if len(res) == 0:
            print("no llm command (- // llm: do something) found.")
        elif len(res) == 1:
            context = {
                "statements": self.statement_source
            }
            message = render_template("task_template.md", context)
            response = model.generate_content(message, generation_config=self.llm_config)
            self.statement_source = "\n".join((self.statement_source, response.text))
            print(f"Response:\n\n{response.text}")
            # IPS()
            with open(self.statement_fpath, "wt", encoding="utf-8") as fp:
                fp.write(self.statement_source)
            print(f"{self.statement_fpath} written")
        elif len(res) > 1:
            raise NotImplementedError("No support for mutiple commands.")
        self.statement_source

def llm_api(message):
    return model.generate_content(message, generation_config=genai.GenerationConfig(temperature=0)).text

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


class SourceSnippet:

    # classvariable undefined for this abstract class
    PATTERN = None
    MARKER = None
    def __init__(self, snippet_source):
        self.snippet_source = snippet_source
        self.process()

    def process(self):
        """
        parses the source snippet and determines the relevant instance variables
        """
        # ensure we are not using the abstract base class
        assert self.PATTERN is not None
        matches = list(re.finditer(self.PATTERN, self.snippet_source))
        assert len(matches) == 1
        match, = matches
        self.snippet_delimiter_inner_content = match.group(1)
        # \snippet{XXi} or \snippet{123i} should be ignored -> only placeholder statements should be generated
        self.ignore_flag = self.snippet_delimiter_inner_content.endswith("i")
        self.ignore_char = "i" if self.ignore_flag else ""

        i0, i1 = match.span()

        self.start_part = self.snippet_source[:i0]
        self.end_part = self.snippet_source[i1:]


class MDSourceSnippet(SourceSnippet):
    PATTERN = SNIPPET_MD_COMMENT_PATTERN
    MARKER = "- // snippet({k}{ignore_char})"


class LatexSourceSnippet(SourceSnippet):
    PATTERN = SNIPPET_LATEX_MACRO_PATTERN
    MARKER = "\\snippet{{{k}{ignore_char}}}"


def auto_md_snippet_numbering(src_fpath):
    """
    Process a markdown source file and enumerate all snippets consecutively.
    """

    with open(src_fpath, "rt", encoding="utf-8") as fp:
        src = fp.read()

    parts: List[str] = nonconsuming_regex_split(SNIPPET_MD_COMMENT_PATTERN, src)

    assert len(parts) > 0
    results = iterate_over_parts(parts[1:], source_snippet_type=MDSourceSnippet)
    save_result(src_fpath, old_src=src, new_source="".join(results))


def auto_tex_snippet_numbering(src_fpath):
    """
    Process a LaTeX source file and enumerate all snippets consecutively.

    e.g.
    \\snippet{XX} -> \\snippet{123}
    """
    with open(src_fpath, "rt", encoding="utf-8") as fp:
        src = fp.read()

    parts: List[str] = nonconsuming_regex_split(SNIPPET_LATEX_MACRO_PATTERN, src)


    part0 = parts[0].strip()
    if not (part0.startswith(r"\snippet{") or part0 == ""):
        msg = f"unexpected first part of LaTeX source: {part0[:30]}"
        raise ValueError(msg)

    assert len(parts) > 0

    results = iterate_over_parts(parts[1:], source_snippet_type=LatexSourceSnippet)
    save_result(src_fpath, old_src=src, new_source="".join(results))


def iterate_over_parts(parts, source_snippet_type: type) -> List[str]:
    """
    Used in auto_tex/md_snippet_numbering
    """
    results = []
    for k, part in enumerate(parts, start=1):
        # create an instance of the appropriate type
        sn = source_snippet_type(part)

        enumerated_snippet_marker = source_snippet_type.MARKER.format(k=k, ignore_char=sn.ignore_char)
        new_snippet = f"{sn.start_part}{enumerated_snippet_marker}{sn.end_part}"
        results.append(new_snippet)

    return results


def save_result(src_fpath: str, old_src: str, new_source: str):
    basepath, ext = os.path.splitext(src_fpath)

    backup_fpath = f"{basepath}_backup{ext}"
    with open(backup_fpath, "wt", encoding="utf-8") as fp:
        fp.write(old_src)
    print(f"\nFile written: {backup_fpath}")

    with open(src_fpath, "wt", encoding="utf-8") as fp:
        fp.write(new_source)
    print(f"\nFile written: {src_fpath}")


def interactive_mode(dev_mode, tex_fpath, statement_fpath, snapshot_fpath):
    """
    In this mode the user is assumend to review the new statements from the currently
    processed snippet.
    """

    mm = MainManager(dev_mode, tex_fpath, statement_fpath, snapshot_fpath, interactive_mode=True)
    mm.do_next_query_iteration()

def llm_command(dev_mode, statement_fpath):
    mm = MainManager(dev_mode, tex_fpath=None, statement_fpath=statement_fpath, snapshot_fpath=None, interactive_mode=True)
    mm.llm_task()

def evaluate_token_tracking(fpath: str):
    try:
        import pandas as pd
    except ImportError:
        print("Error: This function needs pandas to be installed.")
        exit()
    df = pd.read_csv(fpath, names=["timestamp", "tokens"])

    token_sum = sum(df["tokens"])
    print(f"Cumulated query tokens: {token_sum}")

    try:
        from matplotlib import pyplot as plt
    except ImportError:
        print("Error: This function needs matplotlib to be installed.")
        exit()

    plt.plot(df["tokens"])
    plt.xlabel("query index")
    plt.ylabel("query size (tokens)")
    plt.savefig("_token_tracking.png")
    plt.show()
