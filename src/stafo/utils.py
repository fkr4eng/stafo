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

def set_nested_value(data, keys, value):
    """set a given nested dict with given key sequence and value

    Args:
        data (dict): nested dict
        keys (list): key list
        value (any): value

    Returns:
        dict: nested dict
    """
    current = data
    for key in keys[:-1]:
        if key not in current:
            current[key] = {}  # Create a new dict if the key doesn't exist
        current = current[key]
    current[keys[-1]] = value
    return data

def get_nested_value(data, keys):
    """get a given nested dict with given key sequence

    Args:
        data (dict): nested dict
        keys (list): list of keys

    Returns:
        any: value at the end of key list
    """
    try:
        for key in keys:
            data = data[key]
        return data
    except Exception as e:
        raise e
