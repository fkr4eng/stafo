import os
from pathlib import Path
from jinja2 import Environment, FileSystemLoader
import sympy as sp
from functools import wraps
from time import time
try:
    # this will be part of standard library for python >= 3.11
    import tomllib
except ModuleNotFoundError:
    import tomli as tomllib

# TODO: this assumes package to be installed with pip install -e .
BASE_DIR = Path(__file__).parents[2].as_posix()
TEMPLATE_DIR = os.path.join(BASE_DIR, "data", "templates")
TESTA_DATA_DIR = os.path.join(BASE_DIR, "tests", "testdata")

# config file starts with .git_config to prevent nextcloud synchronizing it to (unencrypted) cloud
CONFIG_PATH = os.path.join(BASE_DIR, ".git_config.toml")

if os.path.isfile(CONFIG_PATH):
    with open(CONFIG_PATH, "rb") as fp:
        config_data = tomllib.load(fp)

else:
    config_data = {}


class ParserError(Exception):
    pass

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

class TreeTraverser:
    def __init__(self, apply_func, get_args_func):
        self.apply_func = apply_func
        self.get_args_func = get_args_func

    def run(self, node):
        args = [self.run(arg) for arg in self.get_args_func(node)]
        return self.apply_func(node, args)

def number_type_convert(n):
    if isinstance(n, sp.Number):
        if isinstance(n, sp.Integer):
            return int(n)
        elif isinstance(n, sp.Float):
            return float(n)
        elif isinstance(n, sp.core.numbers.Infinity):
            return """ma.I4291["infinity"]"""
        else:
            raise NotImplementedError(f"sympy type {type(n)} not supported")
    else:
        return n

def flatten(iterable):
    ret = []
    _unpack(ret, iterable)
    return ret

def _unpack(ret, iterable):
    if isinstance(iterable, (tuple, list)):
        for i in iterable:
            _unpack(ret, i)
    else:
        return ret.append(iterable)

class MyDict(dict):
    def __missing__(self, key):
        print(f"warning: {key} was not found, return 'ut' instead")
        return "ut"


def ensure_list(obj):
    """
    Converts `None` to empty list, otherwise converts any sequence to list.

    Motivation: define an empty list as default value for an argument is error-prone.
    Reason: empty list is created once when the function-object is created but not when it is called.
    Recommended way is to use `None` as default value. However, later in the code we only want to handle
    list-instances.
    """
    if obj is None:
        return []
    else:
        return list(obj)



def timing(f):
    @wraps(f)
    def wrap(*args, **kw):
        ts = time()
        result = f(*args, **kw)
        te = time()
        print('func:%r args:[%r, %r] took: %2.4f sec' % \
          (f.__name__, repr(args)[:20], repr(kw)[:20], te-ts))
        return result
    return wrap


class OneToOneMapping(object):
    def __init__(self, a_dict: dict = None, **kwargs):
        if a_dict is None:
            self.a = dict(**kwargs)
            self.b = dict([(v, k) for k, v in kwargs.items()])
        else:
            # handle the case where we do not map strings
            assert len(kwargs) == 0

            # make a copy
            self.a = dict(a_dict)
            self.b = dict([(v, k) for k, v in a_dict.items()])

        # assert 1to1-property
        assert len(self.a) == len(self.b)

    def add_pair(self, key_a, key_b):
        if key_a in self.a:
            msg = f"key_a '{key_a}' does already exist."
            raise KeyError(msg)

        if key_b in self.b:
            msg = f"key_b '{key_b}' does already exist."
            raise KeyError(msg)

        self.a[key_a] = key_b
        self.b[key_b] = key_a

        # assert 1to1-property
        assert len(self.a) == len(self.b)

    def remove_pair(self, key_a=None, key_b=None, strict=True):
        try:
            if key_a is not None:
                key_b = self.a.pop(key_a)
                self.b.pop(key_b)
            elif key_b is not None:
                key_a = self.b.pop(key_b)
                self.a.pop(key_a)
            else:
                msg = "Both keys are not allowed to be `None` at the the same time."
                raise ValueError(msg)
        except KeyError:
            if strict:
                raise
            # else -> pass


def cleanup_after_latex(folder_path, filename):
    del_files = [".4ct", ".4tc", ".aux", ".css", ".dvi", ".html", ".idv", ".lg", ".log", ".tmp", ".xref"]
    for ending in del_files:
        os.remove(os.path.join(folder_path, filename.split(".")[0] + ending))