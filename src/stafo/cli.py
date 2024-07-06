import argparse

from ipydex import IPS, activate_ips_on_exception
from . import core

activate_ips_on_exception()


def main():

    parser = argparse.ArgumentParser()

    # default will be changed to true later
    parser.add_argument(
        "-d", "--dev-mode", help=f"toogle development mode", choices=("true", "false"), default="true"
    )

    parser.add_argument(
        "-asn", "--auto-snippet-numbering",
        help=f"process LaTeX source file to automatically enumerate snippets", metavar="TEX_FILE",
        default=None
    )

    args = parser.parse_args()

    dev_mode = (args.dev_mode == "true")

    if (tex_file := args.auto_snippet_numbering) is not None:
        core.auto_tex_snippet_numbering(tex_file)
    else:
        core.main(dev_mode=dev_mode)
