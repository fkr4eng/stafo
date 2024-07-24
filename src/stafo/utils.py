import os
from pathlib import Path
from jinja2 import Environment, FileSystemLoader


# TODO: this assumes package to be installed with pip install -e .
BASE_DIR = Path(__file__).parents[2].as_posix()
TEMPLATE_DIR = os.path.join(BASE_DIR, "data", "templates")
TESTA_DATA_DIR = os.path.join(BASE_DIR, "tests", "testdata")

# config file starts with .git_config to prevent nextcloud synchronizing it to (unencrypted) cloud
CONFIG_PATH = os.path.join(BASE_DIR, ".git_config.toml")


def render_template(template: str, context: dict):
    """
    :param template:    path to template file relative to TEMPLATE_DIR
    :param context:     dict containing the data which should be inserted into the template
    """
    jin_env = Environment(
        loader=FileSystemLoader(TEMPLATE_DIR),
    )

    template_doc = jin_env.get_template(template)

    res = template_doc.render(context=context)

    return res
