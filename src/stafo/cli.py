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
        help=f"start interactive mode", metavar=("SOURCE_FILE", "STATEMENT_FILE", "SNAPSHOT_FOLDER"),
        nargs=3,
    )

    parser.add_argument(
        "-llm", "--llm-command",
        help=f"execute // llm: request in statement file", metavar="STATEMENT_FILE",
    )

    parser.add_argument(
        "-c", "--convert-statements-to-kg",
        help=f"convert markdown statements to pyirk code", metavar="STATEMENT_FILE",
    )

    parser.add_argument(
        "-tt", "--evaluate-token-tracking",
        help=f"evaluate the token-tracking csv file", metavar="TRACKING_FILE",
    )

    parser.add_argument("--dbg", help="start debug routine", default=None, action="store_true")

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

    elif (tracking_file := args.evaluate_token_tracking) is not None:
        core.evaluate_token_tracking(fpath=tracking_file)

    elif args.interactive_mode:
        tex_fpath, statement_fpath, snapshot_path = args.interactive_mode
        core.interactive_mode(dev_mode, tex_fpath, statement_fpath, snapshot_path)
    elif (statement_file := args.convert_statements_to_kg) is not None:
        from . import statement_to_kg
        statement_to_kg.main(statement_file)
    elif args.llm_command:
        core.llm_command(dev_mode, statement_fpath=args.llm_command)
    elif args.dbg:
        IPS()
    else:
        core.main(dev_mode=dev_mode)
