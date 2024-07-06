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

    args = parser.parse_args()

    dev_mode = (args.dev_mode == "true")
    core.main(dev_mode=dev_mode)
