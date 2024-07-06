import argparse

from ipydex import IPS, activate_ips_on_exception
from . import core

activate_ips_on_exception()


def main():

    parser = argparse.ArgumentParser()

    # default will be changed to true later
    parser.add_argument(
        "-d", "--dev-mode", help=f"toogle development mode", choices=("true", "false"), default="false"
    )

    parser.add_argument(
        "-asn", "--auto-snippet-numbering",
        help=f"process LaTeX source file to automatically enumerate snippets", metavar="TEX_FILE",
        default=None
    )

    parser.add_argument(
        "-i", "--interactive-mode",
        help=f"start interactive mode", metavar=("TEX_FILE", "STATEMENT_FILE"),
        nargs=2,
    )

    args = parser.parse_args()

    dev_mode = (args.dev_mode == "true")

    src_fpath: str
    if (src_fpath := args.auto_snippet_numbering) is not None:
        if src_fpath.endswith(".tex"):
            core.auto_tex_snippet_numbering(src_fpath)
        elif src_fpath.endswith(".md"):
            core.auto_md_snippet_numbering(src_fpath)
        else:
            msg = f"unexpected file extension of {src_fpath}"
            raise ValueError(msg)

    elif args.interactive_mode:
        tex_fpath, statement_fpath = args.interactive_mode
        core.interactive_mode(dev_mode, tex_fpath, statement_fpath)
    else:
        core.main(dev_mode=dev_mode)
