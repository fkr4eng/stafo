import os, sys
import re
from ipydex import IPS, Container
from jinja2 import Environment, FileSystemLoader
import subprocess
import copy
import deepdiff
import sympy as sp
from sympy.parsing.latex import parse_latex, parse_latex_lark
from sympy.external import import_module
from sympy.parsing.sympy_parser import T
from numbers import Real
import pyirk as p
import datetime as dt
from string import ascii_letters

from .stafo_logging import logger
lark = import_module("lark")
if lark:
    from lark import Transformer, Token, Tree
else:
    logger.error("lark parser not found!")

from .utils import BASE_DIR, CONFIG_PATH, render_template, get_nested_value, set_nested_value, ParserError
import stafo.utils as u

ma_path = os.path.join(os.path.abspath(os.path.join(os.path.dirname(p.__file__), "../../..", "irk-data", "ocse")), "math1.py")
ct_path = os.path.join(os.path.abspath(os.path.join(os.path.dirname(p.__file__), "../../..", "irk-data", "ocse")), "control_theory1.py")
ag_path = os.path.join(os.path.abspath(os.path.join(os.path.dirname(p.__file__), "../../..", "irk-data", "ocse")), "agents1.py")



def get_md_lines(fpath) -> list[str]:
    with open(fpath, "rt", encoding="utf-8") as f:
        raw = f.read()
    lines = raw.split("\n")
    return lines


class ConversionManager:
    @u.timing
    def __init__(self, statements_fpath: str, force_key_tuple: tuple=None, num_keys=1000, load_irk_modules=["ct", "ma"]):
        self.statements_fpath = statements_fpath
        self.lines = get_md_lines(statements_fpath)
        self.entity_order = []
        self.eq_reference_dict = {}
        self.ds = {}

        self.load_irk_modules = load_irk_modules

        if "ma" in load_irk_modules:
            self.ma = p.irkloader.load_mod_from_path(ma_path, prefix="ma", reuse_loaded=True)
        if "ct" in load_irk_modules:
            self.ct = p.irkloader.load_mod_from_path(ct_path, prefix="ct", reuse_loaded=True)
        if "ag" in load_irk_modules:
            self.ag = p.irkloader.load_mod_from_path(ag_path, prefix="ag", reuse_loaded=True)

        self.irk_module_names = u.MyDict({"builtins": "p",
                            "control_theory": "ct",
                            "math": "ma",
                            "agents": "ag"})
        self.default_language = "de" # todo this needs to be set for each document
        self.entity_matching_report = ""

        self.exsiting_labels_dict = p.get_label_to_item_dict()

        if force_key_tuple is None:
            self.get_keys(num_keys)
        # in case of unittest, dynamically created keys are hard to test for, so you can pass some predefined ones
        else:
            self.item_keys, self.relation_keys = force_key_tuple

        self.stop_at_line = 124

    def sp_to_us(self, s):
        """space to underscore"""
        return s.replace(" ", "_")

    ####################################################################################################################
    # helper functions
    ####################################################################################################################

    def strip(self, s):
        if isinstance(s, list):
            for i, v in enumerate(s):
                s[i] = self.strip(v)
            return s
        elif isinstance(s, tuple):
            new = []
            for i, v in enumerate(s):
                new.append(self.strip(v))
            return tuple(new)
        elif isinstance(s, str):
            return s.replace("'", "").replace('"', '').replace(".", "").replace(":", "").rstrip()
        else:
            raise TypeError(s)

    def strip_formal_eq(self, s):
        """problem examples:
        'sigma' + 'imaginary unit' * 'omega'
        s^i * Y(s)

        """
        s = s.replace('"', "'")
        # s = s.replace("^", "**") # replace power operator
        symbol_pattern = re.compile(r"'.+?'")
        def repl_func(matchobj):
            return matchobj.group(0).replace(" ", "_").replace("-", "_")
        return self.strip(re.sub(symbol_pattern, repl_func, s))


    def strip_math(self, s):
        if isinstance(s, list):
            for i, v in enumerate(s):
                s[i] = self.strip(v)
            return s
        elif isinstance(s, tuple):
            new = []
            for i, v in enumerate(s):
                new.append(self.strip(v))
            return tuple(new)
        elif isinstance(s, str):
            return s.replace("\\", "").replace('$', '')
        else:
            raise TypeError(s)

    def get_keys(self, num_keys):
        """
        generate pyirk keys
        """
        self.item_keys = [p.generate_new_key("I") for i in range(num_keys)]
        self.relation_keys = [p.generate_new_key("R") for i in range(num_keys)]

    def get_indent(self, line:str):
        """get indentation (number of spaces) of string"""
        if line == "":
            return 0
        indent_pattern = re.compile(r" +?(?=-)")
        indent_res = re.findall(indent_pattern, line)
        if indent_res:
            indent = len(indent_res[0])
        else:
            indent = 0
        return indent

    def get_sub_content(self, content):
        """return the lines that have the same (or more) indentation as the first line in content"""
        assert isinstance(content, list), f"content has to be list of str"
        og_indent = self.get_indent(content[0])
        for i, line in enumerate(content):
            if self.get_indent(line) < og_indent:
                return content[:i]
        return content

    def get_rel_dict_key_interpreter(self):
        """create a dict for the relations that can be addressed by pyirk keys (R1)
        to get the long (and possibly different) literal key in self.d["relations"]"""
        rel_dict = {}
        for k,v in self.d["relations"].items():
            rel_dict[v["key"]] = k
        return rel_dict

    def get_item_dict_key_interpreter(self):
        """create a dict for the items that can be addressed by pyirk keys (I1234)
        to get the long (and possibly different) literal key in self.d["items"]"""
        return self.get_local_item_dict_key_interpreter(self.d)

    def get_local_item_dict_key_interpreter(self, d):
        """create a dict for the items that can be addressed by pyirk keys (I1234)
        to get the long (and possibly different) literal key in d["items"]
        this is used for the local dict inside scopes
        """
        rel_dict = {}
        for k,v in d["items"].items():
            rel_dict[v["key"]] = k
        return rel_dict

    ####################################################################################################################
    # init formal natural language parser
    ####################################################################################################################
    @u.timing
    def step1_init(self):

        self.applicable_to_key = "R78"
        # {items:
            # {"set":
            #   {"key": I1234, "R2": ..., "R4": ...},
            # "finite":
            #   {...}
            # },
        # relations: {}
        # }
        self.d = {
            "items": {
                "set": {
                    "key": "I13",
                    "R1": "mathematical set",
                    "prefix": "p"
                    },
                },
            # todo: some of them have custom keys (as given by llm), some are copied from p.builtins. automate?
            "relations": {
                "has label": {
                    "key": "R1",
                    "R1": "has label",
                    "R22": True,
                    "prefix": "p",
                },
                "has english label": {
                    "key": "R1__en",
                    "R1": "has label  en",
                    "R22": True,
                    "prefix": "p",
                },
                "has german label": {
                    "key": "R1__de",
                    "R1": "has label  de",
                    "R22": True,
                    "prefix": "p",
                },
                "has the verbal description": {
                    "key": "R2",
                    "R1": "has description",
                    "R22": True, # todo I would disagree that this should be functional
                    "prefix": "p",
                },
                "is a subclass of": {
                    "key": "R3",
                    "R1": "is subclass of",
                    "R22": True,
                    "prefix": "p",
                },
                "is an instance of": {
                    "key": "R4",
                    "R1": "is instance of",
                    "R22": True,
                    "prefix": "p",
                },
                "has defining formula": {
                    "key": "R6",
                    "R1": "has defining mathematical relation",
                    "R22": True,
                    "prefix": "p",
                },
                "has domain of argument 1": {
                    "key": "R8",
                    "R1": "has domain of argument 1",
                    "prefix": "p",
                },
                "has domain of argument 2": {
                    "key": "R9",
                    "R1": "has domain of argument 2",
                    "prefix": "p",
                },
                "has range of result": {
                    "key": "R11",
                    "R1": "has range of result",
                    "prefix": "p",
                },
                "is applicable to": {
                    "key": self.applicable_to_key, # todo
                    "R1": "is applicable to",
                    "prefix": "p",
                },
                "is a subproperty of": {                # this is the dict key the way it occurs in document
                    "key": "R17",                       # this is the irk key
                    "R1": "is subproperty of",          # this is the label in irk
                    "prefix": "p",
                },
                "is functional": {
                    "key": "R22",
                    "R1": "is functional",
                    "R22": True,
                    "prefix": "p",
                },
                "has the definition": {
                    "key": "R37",
                    "R1": "has definition",
                    "R22": True,
                    "prefix": "p",
                },
                "has the associated LaTeX notation": {
                    "key": "R24",
                    "R1": "has LaTeX string",
                    "R22": True, # Todo does it have to be functional?
                    "prefix": "p",
                },
                "has the alternative associated LaTeX notation": {
                    "key": "R82",
                    "R1": "has alternative latex string",
                    "prefix": "p",
                },
                "is a secondary instance of": {
                    "key": "R30",
                    "R1": "is secondary instance of",
                    "prefix": "p",
                },
                "has the property": {
                    "key": "R16",
                    "R1": "has property",
                    "prefix": "p",
                },
                "does not have the property": {
                    "key": "R61",
                    "R1": "does not have property",
                    "prefix": "p",
                },
                "has the alternative label": {
                    "key": "R77",
                    "R1": "has alternative label",
                    "prefix": "p",
                    "render": "R77__has_alternative_label",
                },
                "has the alternative german label": {
                    "key": "R77__de",
                    "R1": "has alternative label  de",
                    "prefix": "p",
                    "render": "R77__has_alternative_label__de",
                },
                "has the alternative english label": {
                    "key": "R77__en",
                    "R1": "has alternative label  en",
                    "prefix": "p",
                    "render": "R77__has_alternative_label__en",
                },
                "is associated to": {
                    "key": "R58",
                    "R1": "wildcard relation",
                    "prefix": "p",
                },
                "has explanation": {
                    "key": "R81",
                    "R1": "has explanation",
                    "prefix": "p",
                },
                "is secondary subclass of": {
                    "key": "R46",
                    "R1": "is secondary subclass of",
                    "prefix": "p",
                },
                "is secondary instance of": {
                    "key": "R30",
                    "R1": "is secondary instance of",
                    "prefix": "p",
                },
                "has title": {
                    "key": "R8434",
                    "R1": "has title",
                    "R22": True,
                    "prefix": "ag",
                },
                "has authors": {
                    "key": "R8433",
                    "R1": "has authors",
                    "prefix": "ag",
                },
                "has year": {
                    "key": "R8435",
                    "R1": "has year",
                    "R22": True,
                    "prefix": "ag",
                },
                "has family name": {
                    "key": "R7781",
                    "R1": "has family name",
                    "R22": True,
                    "prefix": "ag",
                },
                "has given name": {
                    "key": "R7782",
                    "R1": "has given name",
                    "prefix": "ag",
                },
                "has google scholar author ID": {
                    "key": "R3476",
                    "R1": "has google scholar author ID",
                    "R22": True,
                    "prefix": "ag",
                },
                "cites": {
                    "key": "R8440",
                    "R1": "cites",
                    "prefix": "ag",
                },

            }}
        """
            # todo:
            "is associate with",
            "There is an example:",
            "There is special terminology:"
            "alternative verbal description?
        """
        for key, value in self.d["relations"].items():
            if not "render" in self.d["relations"][key].keys():
                if value["prefix"] != "p":
                    prefix = value["prefix"] + "__"
                else:
                    prefix = ""
                self.d["relations"][key]["render"] = f'{prefix}{value["key"]}__{value["R1"].replace(" ", "_")}'


        self.comment_pattern = re.compile(r"- //")
        self.new_section_pattern = re.compile(r"New.+?section")
        self.class_pattern = re.compile(r"(?<=There is a class)(?::? )(.+)")                 # sometimes : is forgotten
        self.property_pattern = re.compile(r"(?<=There is a property)(?::? )(.+)")
        self.relation_pattern = re.compile(r"(?<=There is a relation)(?::? )(.+)")
        self.general_operator_pattern = re.compile(r"(?<=There is a general operator)(?::? )(.+)")
        self.unary_operator_pattern = re.compile(r"(?<=There is a unary operator)(?::? )(.+)")
        self.binary_operator_pattern = re.compile(r"(?<=There is a binary operator)(?::? )(.+)")
        self.type_of_arg_1_pattern = re.compile(r"(?<=The type of argument1 of )(.+?)(?: is )(.+)")
        self.type_of_arg_2_pattern = re.compile(r"(?<=The type of argument2 of )(.+?)(?: is )(.+)")
        self.type_of_result_pattern = re.compile(r"(?<=The result type of )(.+?)(?: is )(.+)")
        self.amend_definition_pattern = re.compile(r"(?<=Amend definition of )(.+)")
        self.equation_pattern = re.compile(r"There is an equation") # omit : at eol since llm sometimes forgets it
        self.math_rel_pattern = re.compile(r"There is a mathematical relation")
        self.equivalence_pattern = re.compile(r"There is an equivalence-statement")
        self.if_then_pattern = re.compile(r"There is an if-then-statement")
        self.general_statement_pattern = re.compile(r"There is a general statement")
        self.explanation_pattern = re.compile(r"There is an explanation")
        self.for_pattern = re.compile(r"(?<=For all )('?.+?'?) from ('?.+?'?) to ('?.+?'?)(?::?)")

        self.replace_definition_pattern = re.compile(r"(?<=replace )(.+?)(?: by )(.+?)(?=\.$|$)")

        self.equation_pattern_dict = {
            "full_source": re.compile(r"(?<=- full source code)(?::? )(.+?)(?=\.$|$)"),
            "rel_sign": re.compile(r"(?<=- relation sign)(?::? )(.+?)(?=\.$|$)"),
            "lhs_source": re.compile(r"(?<=- source code of left hand side)(?::? )(.+?)(?=\.$|$)"),
            "rhs_source": re.compile(r"(?<=- source code of right hand side)(?::? )(.+?)(?=\.$|$)"),
            "lhs_formal": re.compile(r"(?<=- formalized left hand side)(?::? )(.+?)(?=\.$|$)"),
            "rhs_formal": re.compile(r"(?<=- formalized right hand side)(?::? )(.+?)(?=\.$|$)"),
            "reference": re.compile(r"(?<=- reference)(?::? )(.+)")
        }
        self.explanation_pattern_dict = {
            "related": re.compile(r"(?<=- related to)(?::? )(.+?)(?=\.$|$)"),
            "verbal": re.compile(r"(?<=- verbal summary)(?::? )(.+?)(?=\.$|$)"),
        }

    ####################################################################################################################
    # parse formal natural language
    ####################################################################################################################
    @u.timing
    def step2_parse_fnl(self):
        """iterate lines, add items and relations to dictionary
        first process lines that add items and some with special patterns, later process general relations (s p o)"""
        self.current_snippet = ""
        for i, line in enumerate(self.lines):

            # continue on comment
            comment = re.findall(self.comment_pattern, line)
            if len(comment) > 0:
                snippet = re.findall(r"snippet\(\d+\)", line)
                manual_snippet = re.findall(r"manually added ?\(\d+\)", line)
                if len(snippet) > 0:
                    self.current_snippet = snippet[0]
                elif len(manual_snippet) > 0:
                    self.current_snippet = manual_snippet[0]
            elif line == "":
                continue
            # indeted lines should be processed somewhere down below
            elif line.startswith(" "):
                logger.debug(f"line {i} skipped: {line}")
                pass
            # existing relations
            else:
                self.d = self.process_line(self.d, i, line)
        # IPS()

    def process_line(self, d:dict, i:int, line:str, skip_entity_order=False, *args, **kwargs):
        """process the line given

        Args:
            d (dict): current dictionary to add entries to
            i (int): line_number
            line (str): line
            skip_entity_order (bool): this is set for items in subscopes, that will not be defined globally

        Returns:
            dict: current dict d
        """

        # first deal with comments
        comment = re.findall(self.comment_pattern, line)
        if len(comment) > 0:
            return d
        else:
            line = line.split("//")[0].rstrip()

        # second check for language indicator
        lang_pat = re.compile(r"(?<=@)\w\w")
        res = re.findall(lang_pat, line)
        if res:
            language = res[0]
            line = line.split("@")[0]
        else:
            language = self.default_language


        new_section = re.findall(self.new_section_pattern, line)
        new_class = re.findall(self.class_pattern, line)
        new_property = re.findall(self.property_pattern, line)
        new_relation = re.findall(self.relation_pattern, line)
        new_general_operator = re.findall(self.general_operator_pattern, line)
        new_unary_operator = re.findall(self.unary_operator_pattern, line)
        new_binary_operator = re.findall(self.binary_operator_pattern, line)
        type_of_arg_1 = re.findall(self.type_of_arg_1_pattern, line)
        type_of_arg_2 = re.findall(self.type_of_arg_2_pattern, line)
        type_of_result = re.findall(self.type_of_result_pattern, line)
        amend_definition = re.findall(self.amend_definition_pattern, line)
        equation = re.findall(self.equation_pattern, line)
        math_rel = re.findall(self.math_rel_pattern, line)
        equivalence = re.findall(self.equivalence_pattern, line)
        if_then = re.findall(self.if_then_pattern, line)
        general_statement = re.findall(self.general_statement_pattern, line)
        explanation = re.findall(self.explanation_pattern, line)
        for_loop = re.findall(self.for_pattern, line)


        # debug
        if i == self.stop_at_line:
            44
        if len(new_section) > 0:
            return d
        # new class?
        elif len(new_class) > 0:
            self.add_new_item(d, self.strip(new_class[0]), language, {"R4": 'p.I2["Metaclass"]'}, skip_entity_order=skip_entity_order)
        # new property?
        elif len(new_property) > 0:
            self.add_new_item(d, self.strip(new_property[0]), language, {"R4": 'p.I54["mathematical property"]'}, skip_entity_order=skip_entity_order)
        # new relation?
        elif len(new_relation) > 0:
            self.add_new_rel(d, self.strip(new_relation[0]), language)
        elif len(new_general_operator) > 0:
            self.add_new_item(d, self.strip(new_general_operator[0]), language, {"R3": 'p.I6["mathematical operation"]'}, skip_entity_order=skip_entity_order)
        elif len(new_unary_operator) > 0:
            self.add_new_item(d, self.strip(new_unary_operator[0]), language, {"R4": 'p.I7["mathematical operation with arity 1"]'}, skip_entity_order=skip_entity_order)
        elif len(new_binary_operator) > 0:
            self.add_new_item(d, self.strip(new_binary_operator[0]), language, {"R4": 'p.I8["mathematical operation with arity 2"]'}, skip_entity_order=skip_entity_order)
        elif len(type_of_arg_1) > 0:
            # todo R8, R9, R11 should just be in general relation parsing instead of here
            arg1, arg2 = self.strip(type_of_arg_1[0])
            if arg2 not in self.d["items"].keys():
                logger.info(f"unknown type: {arg2}")
            if arg1 in self.d["items"].keys():
                self.add_relation_inplace(d["items"][arg1], "R8", self.build_reference(arg2))
            elif arg1 in self.d["relations"].keys():
                self.add_relation_inplace(d["relations"][arg1], "R8", self.build_reference(arg2))
            else:
                raise KeyError()
        elif len(type_of_arg_2) > 0:
            arg1, arg2 = self.strip(type_of_arg_2[0])
            if arg2 not in self.d["items"].keys():
                logger.info(f"unknown type: {arg2}")
            if arg1 in self.d["items"].keys():
                self.add_relation_inplace(d["items"][arg1], "R9", self.build_reference(arg2))
            elif arg1 in self.d["relations"].keys():
                self.add_relation_inplace(d["relations"][arg1], "R9", self.build_reference(arg2))
            else:
                raise KeyError()
        elif len(type_of_result) > 0:
            arg1, arg2 = self.strip(type_of_result[0])
            if arg2 not in self.d["items"].keys():
                logger.info(f"unknown type: {arg2}")
            if arg1 in self.d["items"].keys():
                self.add_relation_inplace(d["items"][arg1], "R11", self.build_reference(arg2))
            elif arg1 in self.d["relations"].keys():
                self.add_relation_inplace(d["relations"][arg1], "R11", self.build_reference(arg2))
            else:
                raise KeyError()
        elif len(amend_definition) > 0:
            arg1 = self.strip(amend_definition[0])
            process_next_line = True
            i_plus = 1
            while process_next_line:
                rarg1, rarg2 = self.strip(re.findall(self.replace_definition_pattern, self.lines[i+i_plus])[0])
                for k, v in self.d["items"][arg1].items():
                    if v == self.build_reference(rarg1):
                        d["items"][arg1][k] = self.build_reference(rarg2)
                i_plus += 1
                if not self.lines[i+i_plus].startswith(" "):
                    # indentation ended
                    process_next_line = False
        # equation or mathematical relation
        elif len(equation) > 0 or len(math_rel) > 0:
            if len(equation) > 0:
                type = "equation"
                item_name = f"equation_{i}"
            else:
                type = "mathematical relation"
                item_name = f"math_relation_{i}"
            lines = self.get_sub_content(self.lines[i+1:])
            key = self.item_keys.pop()
            eq_dict = {
                "type": type,
                "key": key,
                "snip": self.current_snippet
                }
            for l in lines:
                for name, pattern in self.equation_pattern_dict.items():
                    res = re.findall(pattern, l)
                    if res:
                        if name == "reference":
                            self.eq_reference_dict[self.strip(res[0])] = {"key": key, "statement_name": self.new_item_name}
                        eq_dict[name] = res[0]
            d["items"][item_name] = eq_dict

        # statements
        elif len(equivalence) > 0 or len(if_then) > 0 or len(general_statement) > 0:
            name_given = False
            if len(equivalence) > 0:
                additional_context = {"R4": 'p.I17["equivalence proposition"]', "comments": []}
                new_item_name = f"eq stm "
            elif len(if_then) > 0:
                additional_context = {"R4": 'p.I15["implication proposition"]', "comments": []}
                new_item_name = f"it stm "
            elif len(general_statement) > 0:
                additional_context = {"R4": 'p.I14["mathematical proposition"]', "comments": []}
                new_item_name = f"gen stm "
            additional_content = self.get_sub_content(self.lines[i+1:])
            temp_dict = {"items": {}, "relations": {}}
            # note: statement name only allowed as first line in statement to prevent mid parsing name changes
            name = re.findall(r"statement name: (.+?)(?=\.$|$)", self.lines[i+1])
            if name:
                assert name_given == False, "multiple name assignments for statement is not supported"
                new_item_name += f"{self.strip(name[0])}"
                name_given = True
            new_item_name +=  f"l.{i}"
            for ii, l in enumerate(additional_content):
                full_source = re.findall(self.equation_pattern_dict["full_source"], l)
                if len(full_source) > 0:
                    additional_context["comments"].append(full_source[0])
                    continue
                # todo depricated source code of scopes
                # source_pre = re.findall(r"source code of premise: (.+?)(?=\.$|$)", l)
                # source_ass = re.findall(r"source code of assertion: (.+?)(?=\.$|$)", l)
                # if source_pre: additional_context["source_pre"] = source_pre[0]
                # if source_ass: additional_context["source_ass"] = source_ass[0]
                formal = re.findall(r"(?<=formalized )(set|pre|ass)", l)
                if formal:
                    # in order for new relations in assertion to relate to the subject created in setting, the dict
                    # is passed from one scope to the next. In order to still differentiate "dict_ass - dict_set",
                    # the temp_dict is copied
                    temp_dict = copy.deepcopy(temp_dict)
                    # pass this item name down the recursion chain to the point where equations are added so we can find them later
                    self.new_item_name = new_item_name + "__" + f"formal_{formal[0]}"
                    temp_dict = self.recurse_nested_statements(additional_content[ii+1:], i+ii+2, temp_dict)
                    additional_context[f"formal_{formal[0]}"] = temp_dict
            # now differentiate between the dicts
            formal_keys = [key for key in additional_context.keys() if "formal" in key]
            dict_list = [additional_context[key] for key in formal_keys]
            if len(dict_list) > 1:
                diff_list = []
                for index in range(len(dict_list)-1):
                    # see https://zepworks.com/deepdiff/current/optimizations.html#threshold-to-diff-deeper-label
                    # this SEEMS to prevent new dict items from being classified as values changed which fucks up
                    # the current workings of self.get_diffed_dict. Also this seems to work more intuitively
                    diff_list.append(deepdiff.DeepDiff(dict_list[index], dict_list[index+1], threshold_to_diff_deeper=0))
                for index, diff in enumerate(diff_list):
                    additional_context[formal_keys[index+1]] = self.get_diffed_dict(diff)

            d = self.add_new_item(d, new_item_name, language, additional_context, skip_entity_order=skip_entity_order)
            # this should not be used any other way, but just to be sure, reset this
            self.new_item_name = None
        elif len(explanation) > 0:
            additional_content = self.get_sub_content(self.lines[i+1:])
            for ii, l in enumerate(additional_content):
                res = re.findall(self.explanation_pattern_dict["related"], l)
                if res: related_to = self.strip(res[0])
                res= re.findall(self.explanation_pattern_dict["verbal"], l)
                if res: verbal_sum = self.strip(res[0])
            self.d["items"][related_to][self.d["relations"]["has explanation"]["key"]] = verbal_sum
        elif len(for_loop) > 0:
            index_var, start, stop = self.strip(for_loop[0])
            additional_content = self.get_sub_content(self.lines[i+1:])
            temp_dict = {"items": {}, "relations": {}}
            temp_dict = self.recurse_nested_statements(additional_content, i, temp_dict)
            key = self.item_keys.pop()
            for_dict = {
                "key": key,
                "snip": self.current_snippet,
                "items": temp_dict["items"],
                "index_var": index_var,
                "start": start,
                "stop": stop,
                }
            d["items"][f"for_loop_{i}"] = for_dict
        else:
            for k, v in self.d["relations"].items():
                # relations of structure: arg1 rel arg2
                # todo if two relations are similar, eg. 'has element' and 'has element type' this might fail
                if k in line and f"'{k}" in line:
                    rel = f"'{k}'"
                    string = line
                else:
                    rel = k
                    string = self.strip(line)

                res = re.findall(f"(?<=- )(.+?)(?: {rel}:? )(.+?)(?=\\.$|$)", string)
                if len(res) > 0:
                    arg1, arg2 = self.strip(res[0])
                    arg2 = self.build_reference(arg2, d)
                    # first check for some special relation that require special attention
                    # todo having this explicite relation name here is very unelegant, pls change
                    if k == "is associated to" or k == "hat Gleichungsreferenz" or k == "has defining formula":
                        # this relation should be symmetric so we check for both cases
                        # this is used to relate equation to items, we check if this is the case and modify subj/obj
                        key_to_local_item_dict = self.get_local_item_dict_key_interpreter(d)
                        # if arg1 is the reference obj, we need to find the correspondig item and add the relation
                        if arg1 in self.eq_reference_dict.keys():
                            eq_key = self.eq_reference_dict[arg1]["key"]
                            stm_name, scope = self.eq_reference_dict[arg1]["statement_name"].split("__")
                            # we are still in the same scope as the equation -> trivial
                            if eq_key in key_to_local_item_dict.keys():
                                arg1 = key_to_local_item_dict[eq_key]
                            # we try to ref a eq from outside its scope -> hard
                            # todo this might fail if statements are nested
                            else:
                                inter = self.get_local_item_dict_key_interpreter(self.d["items"][stm_name][scope])
                                arg1 = inter[eq_key]
                        # if arg2 is the ref obj. we just put the key as the statment obj -> will surely exist in namespace :)
                        if arg2 in self.eq_reference_dict.keys():
                            arg2 = self.eq_reference_dict[arg2]["key"]
                    # instance of
                    if v["key"] == "R4":
                        self.add_new_item(d, arg1, language, {"R3": None, "R4": arg2}, skip_entity_order=skip_entity_order)
                    # subclass of
                    elif v["key"] == "R3":
                        self.add_new_item(d, arg1, language, {"R3": arg2, "R4": None}, skip_entity_order=skip_entity_order)
                    # alternative label
                    elif "R77" in v["key"]:
                        if arg1 in d["items"]:
                            tag = "items"
                        elif arg1 in d["relations"]:
                            tag = "relations"
                        else:
                            raise ParserError(f"{arg1} is neider item nor relation in d")

                        # try to match alternative label with existing KG
                        existing_item = self.get_existing_item(arg2)
                        # automatically created items don't count
                        if existing_item and "a" in existing_item.short_key:
                            existing_item = None
                        if existing_item:
                            key = existing_item.short_key
                            prefix = self.irk_module_names[existing_item.base_uri.split('/')[-1]]
                            self.entity_matching_report += f"matched '{arg1}' with {prefix}.{key}[{existing_item.R1}]\n"
                            # now we need to replace the old key from the item declaration order with the existing key
                            self.entity_order.remove(d[tag][arg1]["key"])
                            self.entity_order.append(key)
                            d[tag][arg1]["key"] = key
                            d[tag][arg1]["R1"] = existing_item.R1.value
                            d[tag][arg1]["prefix"] = prefix
                            # add the alternative label in the correct language
                            if existing_item.__getattr__(f"R1__has_label__{language}") is None:
                                # d[tag][arg1][f"R77__{language}"] = arg1
                                self.add_relation_inplace(d[tag][arg1], f"R77__{language}", arg1)
                            # remove default R4 typing and possible duplicate types
                            r4_label = d[tag][arg1]["R4"].split('"')[1]
                            if "Metaclass" in d[tag][arg1]["R4"] or (existing_item.R4 and r4_label == existing_item.R4.R1.value) or (existing_item.R3 and r4_label == existing_item.R3.R1.value):
                                del d[tag][arg1]["R4"]

                        else:
                            # previously only different language tag added
                            if not "R1" in d[tag][arg1].keys() and language == self.default_language:
                                d[tag][arg1]["R1"] = arg1
                            else:
                                self.add_relation_inplace(d[tag][arg1], v["key"], arg2)
                    else:
                        if not (arg1 in self.d["items"].keys() or arg1 in d["items"].keys() or arg1 in self.d["relations"]):
                            self.add_new_item(d, arg1, language, skip_entity_order=skip_entity_order)
                            logger.info(f"dummy item {arg1} added")
                        if arg1 in d["items"]:
                            self.add_relation_inplace(d["items"][arg1], v["key"], arg2)
                        elif arg1 in d["relations"]:
                            self.add_relation_inplace(d["relations"][arg1], v["key"], arg2)
                        # todo: keep an eye out for this change, why would a scope reference something outside as a subject?
                        elif arg1 in self.d["items"]:
                            self.add_relation_inplace(self.d["items"][arg1], v["key"], arg2)
                        elif arg1 in self.d["relations"]:
                            self.add_relation_inplace(self.d["relations"][arg1], v["key"], arg2)
                        else:
                            raise ParserError("why would a scope reference something outside as a subject? Maybe the relation should change sub and obj?")

                    break
                # relations of structure arg1 rel.
                res = re.findall(r"(?<=- )(.+?)(?: " + k + r"""(?: |'|"|\.|:|$))""", line)
                if len(res) > 0:
                    arg1 = self.strip(res[0])
                    # functional
                    if v["key"] == "R22":
                        if arg1 in d["relations"]:
                            d["relations"][arg1][v["key"]] = True
                        else:
                            raise KeyError(f"why is {arg1} not in d, maybe self.d?")
                        break
                    # definition
                    elif v["key"] == "R37":
                        # resolve if this is def for property or concept or something else?
                        raise NotImplementedError("This is so old and prob wrong, esp. recursion see other example")
                    else:
                        logger.warning(f"maybe? not processed line {i}: {line}")

            else:
                logger.warning(f"not processed line {i}: {line}")

        return d

    def get_r1_key(self, language, force_suffix=False):
        if language != self.default_language or force_suffix:
            r1_key = f"R1__{language}"
        else:
            r1_key = "R1"
        return r1_key

    # @u.timing
    def add_new_item(self, d, label, language, additional_relations:dict={}, skip_entity_order=False):
        prefix = False
        # check if item already exists in KG
        existing_item = self.get_existing_item(label)
        # todo find a save way to match different languages, .lower() has problems
        # automatically created items don't count
        if existing_item and "a" in existing_item.short_key:
            existing_item = None
        if existing_item:
            key = existing_item.short_key
            prefix = self.irk_module_names[existing_item.base_uri.split('/')[-1]]
            self.entity_matching_report += f"matched '{label}' with {prefix}.{key}[{existing_item.R1}]\n"
        else:
            key = self.item_keys.pop()

        if label not in d["items"].keys():
            r1_key = self.get_r1_key(language)
            d["items"][label] = {"key": key, r1_key: label, "snip": self.current_snippet, "prefix": prefix}
            # also add R1 key for internal referencing, even though it might not be the desired language
            if "R1" not in d["items"][label].keys():
                d["items"][label]["R1"] = label
        else:
            key = d["items"][label]["key"]
        for k, v in additional_relations.items():
            if isinstance(v, str) and len(v) > 0:
                try:
                    irk_label = v.split('"')[1] # todo this should be try-except-ed
                    #! why are we doing this? This way I cant add string values -> Those are not added here but later
                except Exception as e:
                    pass
                v_item = p.ds.get_item_by_label(irk_label)
                # prevent duplication in R3/R4 hierarchy while still supporting new relations for existing items
                if d["items"][label]["prefix"] and v_item and k in ["R3", "R4"]:
                    continue
            self.add_relation_inplace(d["items"][label], k, v)
            if v == None:
                if k in d["items"][label].keys():
                    del d["items"][label][k]
        if not skip_entity_order and key not in self.entity_order:
            self.entity_order.append(key)
        return d

    def add_new_rel(self, d, label, language, additional_relations:dict={}):
        prefix = False
        # check if relation already exists in KG
        existing_rel = p.ds.get_item_by_label(label.lower())
        if existing_rel:
            key = existing_rel.short_key
            prefix = self.irk_module_names[existing_rel.base_uri.split('/')[-1]]
            self.entity_matching_report += f"matched '{label}' with {prefix}.{key}[{existing_rel.R1}]\n"
        else:
            key = self.relation_keys.pop()

        if label not in d["relations"].keys():
            r1_key = self.get_r1_key(language)
            d["relations"][label] = {
                "key": key,
                r1_key: label,
                "render": f"""{key}__{self.sp_to_us(label)}""",
                "snip": self.current_snippet,
                "prefix": prefix}
        else:
            key = d["relations"][label]["key"]
        for k, v in additional_relations.items():
            self.add_relation_inplace(d["relations"][label], k, v)
        if key not in self.entity_order:
            self.entity_order.append(key)
        return d

    def add_relation_inplace(self, d:dict, key:str, value:str):
        """add a relation between subject and object to a given dict (inplace)

        Args:
            d (dict): the dict in which the subject resides
            key (str): relation key (e.g. R16)
            value (str): object, in general the result of self.build_reference
        """
        # try type conversion in case of literals (numbers) -> will be pr
        try:
            value = int(value)
        except:
            try:
                value = float(value)
            except:
                pass

        self.rel_interpr = self.get_rel_dict_key_interpreter()
        if key in self.rel_interpr.keys():
            relation = self.d["relations"][self.rel_interpr[key]]

            # relation is functional: only one object, might be overwriting old one
            if "R22" in relation.keys() and relation["R22"] == True:
                d[key] = value
            # relation is not functional: make list or append to it
            else:
                if key in d.keys():
                    assert type(d[key]) == list, f"{d[key]} should be a list."
                    d[key].append(value)
                else:
                    if isinstance(value, list):
                        # this is (only?) used in the memristor example when building the dict directly without fnl
                        d[key] = value
                    else:
                        d[key] = [value]

        # key is probably a special key such as 'comment' or 'formal_set'
        else:
            assert not key.startswith("R"), f"is {key} maybe a relation key that should be in d[relations]?"
            d[key] = value

    def recurse_nested_statements(self, content, line_no:int, temp_dict=None):
        """parse the content of nested definition statements recursively.
        Goal format:
        {"OR_1":
            {items:
                {"AND":
                    {items:
                        {statement1, statement2}
                    }
                }
                statement3
            }
        }
        most outer list should have only one element by definition
        """
        num_lines = len(content)
        indent = self.get_indent(content[0])
        i = 0
        op_count = 0
        while i < num_lines:
            line = content[i]
            # if line is more indented it will be processed in subroutine
            if self.get_indent(line) == indent:
                op_pattern = re.compile(r"(OR|AND|NOT)")
                operator = re.findall(op_pattern, line)
                if operator:
                    sub_content = self.get_sub_content(content[i+1:])
                    res = self.recurse_nested_statements(sub_content, line_no+i+1, temp_dict=copy.deepcopy(temp_dict))
                    # skip next lines that were processed in subroutine
                    i += len(sub_content)
                    # dict diff, only add new part to opKey
                    dict_diff = deepdiff.DeepDiff(temp_dict, res)
                    diff = self.get_diffed_dict(dict_diff)

                    temp_dict["items"][f"{operator[0]}_{op_count}"] = diff

                    op_count += 1
                else:
                    if temp_dict is not None:
                        temp_dict = self.process_line(copy.deepcopy(temp_dict), line_no+i, line, skip_entity_order=True)
                        # I think this is the same as before: inplace without deepcopy
                    else:
                        raise ValueError("temp_dict should be preconfigured")

            elif self.get_indent(line) < indent:
                # this means that the context was chosen too large
                break
            else:
                # print(f"skipping: {line}")
                pass
            i += 1
        return temp_dict

    def get_existing_item(self, label):
        if label in self.exsiting_labels_dict.keys():
            return self.exsiting_labels_dict[label]
        else:
            return None

    def build_reference(self, arg2, local_dict={}):
        """return dual readable version of entity if possible (might be literal): I1234["something"]
        arg2 is FNL name
        """
        # todo add functionality that this also takes a key as argument
        if arg2 in self.d["items"].keys():
            arg2v = self.d["items"][arg2]
            key = arg2v['key']
            if arg2v["prefix"]:
                arg2 = f"""{arg2v["prefix"]}.{key}["{arg2v['R1']}"]"""
            else:
                arg2 = f"""{key}["{arg2v['R1']}"]"""


        elif arg2 in self.d["relations"].keys():
            arg2v = self.d["relations"][arg2]
            key = arg2v['key']
            if arg2v["prefix"]:
                arg2 = f"""{arg2v["prefix"]}.{key}["{arg2v['R1']}"]"""
            else:
                arg2 = f"""{key}["{arg2v['R1']}"]"""
        # if we are inside a scope and arg2 references a local variable, arg2 will not appear in self.d,
        # in this case, we just need to remove potential spaces to create the reference cm.bla_bla to the local variable
        elif local_dict:
            if arg2 in local_dict["items"].keys():
                arg2 = arg2.replace(" ", "_")
        return arg2

    def get_diffed_dict(self, diff:deepdiff.DeepDiff):
        """return the difference dict between to dict. Note: currently only works for addition "info(dict1)<info(dict2)"

        Args:
            diff (deepdiff.DeepDiff): diff object

        Raises:
            KeyError: _description_

        Returns:
            dict: difference dictionary
        """
        dbg = 0 # a counter to make sure every change in dicts is considered, since only some cases are implemented
        current_dict = {"items": {}, "relations": {}}
        if "iterable_item_added" in diff.keys():
            for ikey, ivalue in diff["iterable_item_added"].items():
                key_pattern = re.compile(r"(?<=\[').+?(?='\])")
                res = re.findall(key_pattern, ikey)
                # in case e.g. assertion adds multiple properties, then we need to make a list to store them all
                try:
                    prev = get_nested_value(current_dict, res)
                    prev.append(ivalue)
                except KeyError:
                    prev = [ivalue]
                set_nested_value(current_dict, res, prev)
            dbg += 1

        if "dictionary_item_added" in diff.keys():
            for ikey in diff["dictionary_item_added"]:
                key_pattern = re.compile(r"(?<=\[').+?(?='\])")
                res = re.findall(key_pattern, ikey)
                set_nested_value(current_dict, res, get_nested_value(diff.t2, res))
            dbg += 1

        if "dictionary_item_removed" in diff.keys():
            # since we start with an empty dict anyways, we dont need to do anything here
            dbg += 1

        # old: so far this only happens in snippet 81, with 3 equations in premise and 3 equations in assertion
        if "values_changed" in diff.keys():
            raise DeprecationWarning("since the introduction of kwarg threshold_to_diff_deeper=0, this should not occur anymore.")
            for ikey, ivalue in diff["values_changed"].items():
                key_pattern = re.compile(r"(?<=\[').+?(?='\])")
                res = re.findall(key_pattern, ikey)
                set_nested_value(current_dict, res, diff["values_changed"][ikey]["new_value"])
            dbg += 1
        if dbg != len(diff.keys()):
            raise KeyError("apparently some change between the dicts was not considered. please investigate diff.keys()")
        return current_dict

    ####################################################################################################################
    # rendering
    ####################################################################################################################
    @u.timing
    def render(self) -> str:
        """
        :returns: path of rendered module
        """
        self.rel_interpr = self.get_rel_dict_key_interpreter()
        self.item_interpr = self.get_item_dict_key_interpreter()
        self.key_to_name = dict(self.rel_interpr)
        self.key_to_name.update(self.item_interpr)
        entity_declaration = ""
        output = ""
        count = 0

        for key in self.entity_order:
            name = self.key_to_name[key]
            if key.startswith("I"):
                tag = "items"
            elif key.startswith("R"):
                tag = "relations"
            else:
                raise TypeError()
            v = self.d[tag][name]
            if v["prefix"]:
                # remove all duplicate relations for matched entities
                v = self.prune_dict(v)
            else:
                entity_declaration += f'{key} = p.create_{tag[:-1]}(R1__has_label="{v["R1"]}")\n'
            context = self.built_simple_context(v)
            context["name"] = self.build_reference(name)
            res = render_template(f"basic_entity_template.py", context)
            output += res + "\n\n"
            count += 1
            if "R4" in v.keys() and (v["R4"] == 'p.I15["implication proposition"]' or v["R4"] == 'p.I17["equivalence proposition"]' or v["R4"] == 'p.I14["mathematical proposition"]'):
                context = {"id": self.build_reference(name), "rd": 1}
                if "snip" in v.keys():
                    context["snip"] = v["snip"]
                else: context["snip"] = ""
                if "comments" in v.keys():
                    context["comments"] = v["comments"]

                if "formal_set" in v.keys():
                    context["setting"] = self.get_statement_context_recursively(v, v[f"formal_set"])
                elif "source_set" in v.keys():
                    context["setting"] = [f'cm1.create_expression({v["source_set"]})']

                if "formal_pre" in v.keys():
                    context["premise"] = self.get_statement_context_recursively(v, v[f"formal_pre"])
                elif "source_pre" in v.keys():
                    context["premise"] = [f'cm1.create_expression({v["source_pre"]})']

                if "formal_ass" in v.keys():
                    context["assertion"] = self.get_statement_context_recursively(v, v[f"formal_ass"])
                elif "source_ass" in v.keys():
                    context["assertion"] = [f'cm1.create_expression({v["source_ass"]})']
                res = render_template("statement_template.py", context)
                output += res + "\n\n"

        pyirk_context = {"uri_name": f"auto_import_{os.path.split(self.statements_fpath)[-1].split('.')[0]}",
                        #  "ct_path": ct_path,
                         "irk_module_names": self.irk_module_names,
                         "entity_declaration": entity_declaration,
                         "content": output}

        for mod in self.load_irk_modules:
            pyirk_context[f"{mod}_path"] = getattr(self, mod).__file__

        res = render_template("pyirk_template.py", pyirk_context)

        fpath = "output.py"
        with open(fpath, "wt", encoding="utf-8") as f:
            f.write(res)
        logger.info(f"{count} new entities written to {fpath}.")
        t = dt.datetime.now().strftime("_%Y_%m_%d__%H_%M_%S")
        os.makedirs("match_history", exist_ok=True)
        with open(f"match_history/matched_entities_{t}.txt", "wt", encoding="utf-8") as f:
            f.write(self.entity_matching_report)
        return fpath

    def prune_dict(self, value_dict):
        matched_item = p.ds.get_item_by_label(value_dict["R1"])
        existing_rel_keys = [rel.split("#")[-1] for rel in matched_item.get_relations().keys()]
        del_keys = []
        for k, v in value_dict.items():
            if "R1" == k:
                continue
            if k in existing_rel_keys:
                del_keys.append(k)
        for k in del_keys:
            del value_dict[k]
        return value_dict

    def built_simple_context(self, value_dict):
        """return context for template. works for most items and relations."""
        keys_that_want_literals = ["R1", "R2", "R24", "R77", "R77__en", "R77__de", "R81", "R82", "R3476", "R7781", "R7782", "R8434"]
        # todo declare this at the top
        context = {"key": value_dict["key"], "rel": [], "extra": []}
        if "snip" in value_dict.keys():
            context["snip"] = value_dict["snip"]
        else: context["snip"] = ""
        if "comments" in value_dict.keys():
            context["comments"] = value_dict["comments"]
        else: context["comments"] = ""
        for key, value in value_dict.items():
            if key.startswith("R"):
                # first some exceptions
                if key == "R6":
                    # the object of this relation is a reference string that appears in the 'reference' key of some equation item
                    # todo find this equation
                    pass
                elif (key == "R4" or key == "R3"):
                    if "p.I2[" in value:
                        self.entity_matching_report += f'Unmatched entity: {self.build_reference(value_dict["R1"])}\n'
                    if ("p.I6" in value or "p.I7" in value or "p.I8" in value or "p.I9" in value):
                        # operators need custom call method
                        context["extra"].append(f'{self.build_reference(value_dict["R1"])}.add_method(p.create_evaluated_mapping, "_custom_call")')

                # add correct amount of quotation marks
                if key in keys_that_want_literals:
                    # value is literal -> need extra quotation marks ""
                    quotes = '"'
                else:
                    quotes = ""

                # handle functional relations and non-functional with single object -> no list (R8__=I000[".."])
                if not type(value) == list or len(value) == 1:
                    # R22 rels are not lists, for easier processing, put them in a list
                    if type(value) == list:
                        value = value[0]
                    res = re.findall(r"[R|I]\d+", str(value))
                    if not quotes and len(res) == 0:
                        # then maybe the object of rel was set before the item was introduced (order in FNL)
                        if value in self.d["items"].keys():
                            value = self.build_reference(value)
                    context["rel"].append(f'{self.d["relations"][self.rel_interpr[key]]["render"]}={quotes}{value}{quotes}')
                # handle multiple objects -> list (R8__=[I000[".."], I111[".."]])
                else:
                    # we need to manually construct a string here instead of a list, since we might want python objects
                    # and not strings of python objects inside that list: ['p.12[..]'] would be bad
                    l = []
                    for v in value:
                        res = re.findall(r"[R|I]\d+", str(v))
                        # if v is an item, then we nee
                        if res:
                            l.append(str(v))
                        else:
                            ref = self.build_reference(v)
                            if ref == v:
                                # this means, that there is no reference and the origi-> quote the string
                                l.append(f'"{v}"')
                            else:
                                l.append(f'{ref}')

                    string = f"[{', '.join(l)}]"
                    context["rel"].append(f'{self.d["relations"][self.rel_interpr[key]]["render"]}={string}')
        # sort the relations in ascending number oder
        context["rel"].sort(key=lambda x: int(re.findall(r"(?<=R)\d+(?=__)", x)[0]))
        # get rid of R1, since we use the entity.update method
        while context["rel"] and "R1__" in context["rel"][0]:
            del context["rel"][0]
        return context

    def get_statement_context_recursively(self, statement_item, subdict:dict, recursion_depth=1):
        # output
        out = []
        # insertion index makes sure that item creation happens before relations are added, that reference said items
        insertion_index = 0
        for key, value in subdict["items"].items():
            # if key == "other":
            if "equation" in key or "math_relation" in key:
                if value["type"] in ["equation", "mathematical relation"]:
                    res = self.render_math_relation(statement_item, value, recursion_depth)
                    for l in res.split("\n"):
                        # adapt equation to context manager
                        if len(l) > 0 and not "snippet" in l:
                            out.insert(insertion_index, l)
                else:
                    raise TypeError()
            elif "OR" in key or "AND" in key or "NOT" in key:
                res = self.get_statement_context_recursively(statement_item, subdict["items"][key], recursion_depth+1)
                context = {
                    "content": res,
                    "logic_operator": key.split("_")[0],
                    "rd": recursion_depth,
                    "new_rd": recursion_depth + 1,
                    "indent": " " * 4 * recursion_depth,
                    }
                out.append(render_template("and_or_not_template.py", context))
            elif "for_loop" in key:
                res = self.get_statement_context_recursively(statement_item, subdict["items"][key], recursion_depth)
                if value["start"].isnumeric():
                    start = int(value["start"])
                else:
                    start = f"""cm{recursion_depth}.{value["start"]}"""
                if value["stop"].isnumeric():
                    stop = int(value["stop"])
                else:
                    stop = f"""cm{recursion_depth}.{value["stop"]}"""
                context = {
                    "content": res,
                    "indent": " " * 4 * recursion_depth,
                    "start": start,
                    "stop": stop,
                    "index_var": f"""cm{recursion_depth}.{value["index_var"]}""",
                    }
                out.append(render_template("integer_range_template.py", context))
            else:
                key = self.strip_math(key).replace(" ", "_")
                if "R4" in value.keys():
                    # todo decide uq_instance_of vs instance_of
                    out.insert(insertion_index, f'cm{recursion_depth}.new_var({key}=p.instance_of({value["R4"]}))')
                    insertion_index += 1
                    # Note: if there is no R4 relation, the item must be already existing in cm.
                    # todo find a way to verify the existance
                for kk, vv in value.items():
                    number = re.findall(r"(?<=R)\d+", kk)
                    if number and int(number[0]) > 4: # just exclude R1-R4 here
                        if not isinstance(vv, list):
                            vv = [vv]
                        for vvv in vv:
                            # some exceptions when not to add cm.
                            # in case of literals (numbers)
                            if isinstance(vvv, Real):
                                obj_str = f"{vvv}"
                            # in case of equation references (global item names)
                            # todo this is suboptimal. if the same name exists in global namespace and scope, the global one is used
                            # todo bc. it is hard to know here, whats already been defined in e.g. settings scopes above
                            elif re.findall(r"I\d+", vvv):
                                obj_str = f"{vvv}"
                            else:
                                # todo this cm1 is not clean since new variables might be defined in subscopes
                                obj_str = f"cm1.{vvv}"
                            # todo this cm1 is not clean since new variables might be defined in subscopes
                            out.append(f'cm{recursion_depth}.new_rel(cm1.{key}, {self.build_reference(self.rel_interpr[kk])}, {obj_str})')
        return out

    def render_math_relation(self, statement_item, eq_dict, recursion_depth):
        context = {"key": eq_dict["key"], "rel": [], "rd": recursion_depth}
        if "snip" in eq_dict.keys():
            context["snip"] = eq_dict["snip"]
        else: context["snip"] = ""
        if "comments" in eq_dict.keys():
            context["comments"] = eq_dict["comments"]

        if eq_dict["type"] == "equation":
            context["rsgn"] = '"=="'
        elif eq_dict["type"] == "mathematical relation":
            context["rsgn"] = f'"{eq_dict["rel_sign"]}"'



        #! TODO WIP
        if "lhs_formal" in eq_dict.keys() and "rhs_formal" in eq_dict.keys():
            context["lhs_formal"] = self.replace_expr(eq_dict["lhs_formal"])
            context["rhs_formal"] = self.replace_expr(eq_dict["rhs_formal"])
        elif "lhs_source" in eq_dict.keys() and "rhs_source" in eq_dict.keys():
            try:
                what = "lhs_source"
                context["lhs_formal"] = self.process_latex(statement_item, eq_dict["lhs_source"])
                what = "rhs_source"
                context["rhs_formal"] = self.process_latex(statement_item, eq_dict["rhs_source"])
            except Exception as e:
                logger.warning(f"rendering failed for {eq_dict[what]} due to {type(e)}: {e}")
                context["lhs_source"] = eq_dict["lhs_source"]
                context["rhs_source"] = eq_dict["rhs_source"]
        else:
            try:
                res = self.process_latex(statement_item, eq_dict["full_source"], full=True)
                if hasattr(res, "__len__"):
                    context["lhs_formal"] = res[0]
                    context["rhs_formal"] = res[1]
                else:
                    context["full_source"] = res

            except Exception as e:
                logger.warning(f"rendering failed for {eq_dict[what]} due to {type(e)}: {e}")
                context["full_source"] = eq_dict["full_source"]
        res = render_template("math_relation_template.py", context)
        return res

    def process_latex(self, statement_item, latex_og, full=False):
        """process latex input and return string conforming with pyirk notation

        Args:
            statement_item (dict): the statement hierarchically above the latex snippet
            latex_og (str): latex snippet
            full (bool, optional): Flag, set to True if evaluating full_source. Defaults to False.

        Returns:
            str: pyrik string
        """
        self.sp_to_irk_map = {
            sp.Add: lambda *args: "(" + "+".join(args) + ")",
            sp.Mul: lambda *args: "(" + "*".join(args) + ")",
            sp.Pow: lambda *args: "(" + "**".join(args) + ")",
            sp.Sum: """ma.I5441["sum over index"]""",
            sp.Integral: """ma.I5442["general integral"]""",
            sp.Tuple: lambda *args: tuple(args),
            sp.Derivative: lambda *args: f"""ma.derivative({", ".join(u.flatten(args))})"""
        }

        # add local variables to lookup
        lookup = copy.deepcopy(self.d["items"])
        # todo this needs to be recursive if we talk about nested statements
        for formal in ["formal_set", "formal_pre", "formal_ass"]:
            if formal in statement_item.keys():
                lookup.update(statement_item[formal]["items"])

        # strip
        latex = latex_og.replace('$', '')
        latex = re.sub(r"^\\[(]", "", latex)
        latex = re.sub(r"\\[)]$", "", latex)

        # substitute all custom expressions with variables, so lark can parse them.
        # lark does not recognize multi-char-variables
        # we need to replace each variable with a single character var name
        # latex = "\\sum_{'i'=1}^'n' ('element of sequence'('c', 'i') * 'element of sequence'('b', 'i'))"
        string_with_vars_removed = re.sub(r"'.+?'", "", latex)
        open_vars = list(set(ascii_letters) - set(string_with_vars_removed))
        var_map = u.OneToOneMapping()
        def repl_func(matchobj):
            long_var = self.strip(matchobj.group(0))
            if not long_var in var_map.a.keys():
                var_map.add_pair(long_var, open_vars.pop())
            return var_map.a[long_var]
        latex = re.sub(r"'.+?'", repl_func, latex)

        only_term = True
        if full:
            rel_signs = ["<=", ">=", "<", ">", "=="] # todo change '=' to '==' to distinguish sum{i=1} = x
            for rs in rel_signs:
                if rs in latex:
                    only_term = False
                    res = []
                    for term in latex.split(rs):
                        res.append(self.convert_latex_to_irklike_str(term, lookup, var_map))

        if only_term:
            res = self.convert_latex_to_irklike_str(latex, lookup, var_map)

        return res

    def clean_latex_var(self, latex):
        l = self.strip(latex)
        # \mathcal, \mathrm
        ignore_commands = ["\\\\mathcal", "\\\\mathrm"]
        pat = re.compile(f"(?:{'|'.join(ignore_commands)})" + r"{(.+?)}")
        l = re.sub(pat, lambda mo: mo.group(1), l)

    def convert_latex_to_irklike_str(self, latex, item_lookup, var_map):
        # 1. convert to sympy
        sp_expr = parse_latex_lark(latex)
        if len(sp_expr.free_symbols) > 5:
            # latex code like "func(var)" will be interpreted as f*u*n*c(v*a*r) if not properly ticked '
            logger.warning(f"equation {latex} was rendered to {sp_expr} with a lot of symbols, is this intentional?")
        # ambiguous result
        if isinstance(sp_expr, Tree):
            # todo this is an easy fix, but might prove troublesome in the future, beware of the warning
            sp_expr = sp_expr.children[0]
            logger.warning(f"Warning: lark result not unique, using first option: {sp_expr} for {latex}")

        # 2. traverse tree
        res = self.convert_sympy_to_irklike_str(sp_expr, item_lookup, var_map)
        return res

    def convert_sympy_to_irklike_str(self, sp_expr, item_lookup, var_map):
        def _get_irk_for_sp(sp_expr, args):
            # Symbols
            if isinstance(sp_expr, sp.Symbol):
                if sp_expr.name in var_map.b.keys():
                    og_var_name = var_map.b[sp_expr.name]
                else:
                    og_var_name = sp_expr.name
                if og_var_name in self.d["items"]:
                    res = self.build_reference(og_var_name)
                else:
                    res = "cm1." + self.build_reference(og_var_name, local_dict={"items": item_lookup})
                return res
            # callable custom Funktions e.g. f(x)
            elif isinstance(type(sp_expr), sp.core.function.UndefinedFunction):
                # this typing is a little weird
                # f(x) -type-> f -type-> sp.core.function.UndefinedFunction
                sp_expr = type(sp_expr)
                if sp_expr.name in var_map.b.keys():
                    og_var_name = var_map.b[sp_expr.name]
                else:
                    og_var_name = sp_expr.name
                if og_var_name in self.d["items"]:
                    function_type = self.build_reference(og_var_name)
                else:
                    function_type = "cm1." + self.build_reference(og_var_name, local_dict={"items": item_lookup})
                return f"""{function_type}({", ".join(args)})"""
            # numbers
            elif isinstance(sp_expr, (int, float, complex, sp.Number)):
                if sp_expr == 0:
                    return """ma.I5000["scalar zero"]"""
                elif sp_expr == 1:
                    return """ma.I5001["scalar one"]"""
                else:
                    return str(u.number_type_convert(sp_expr))
            # callable generic function e.g. add
            else:
                sp_type = type(sp_expr)
                try:
                    irk_type = self.sp_to_irk_map[sp_type]
                except KeyError:
                    msg = f"For {sp_type} there is no IRK-type defined yet"
                    raise NotImplementedError(msg)

                if sp_type == sp.Sum:
                    # sympy syntax: sp.Sum(expr, (index_var, start, stop))
                    args = (args[0], args[1][0], f"""ma.I5440["limits"]({", ".join(args[1][1:])})""")
                elif sp_type == sp.Integral:
                    # sympy syntax: sp.Integral(expr, (index_var, start, stop))
                    # limits are specified
                    if len(args[1]) > 1:
                        args = (args[0], args[1][0], f"""ma.I5440["limits"]({", ".join(args[1][1:])})""")
                        irk_type = """ma.I5443["definite integral"]"""
                    # no limits are given
                    else:
                        args = (args[0], args[1][0])
                        irk_type = """ma.I5444["indefinite integral"]"""

                if type(irk_type) == str:
                    return f"""{irk_type}({", ".join(args)})"""
                else:
                    return irk_type(*args)

        def _get_args_for_sp(sp_expr):
            return sp_expr.args

        tt = u.TreeTraverser(apply_func=_get_irk_for_sp, get_args_func=_get_args_for_sp)
        res = tt.run(sp_expr)
        return res



    def replace_expr(self, expr):
        try:
            parsed_expr = sp.parse_expr(expr)
        except:
            logger.info(f"sympy parsing failed for {expr}, defering to lookup")
            return self.get_expr_from_lookup(expr)
        repl_list, subs_list = [], []
        repl_list, subs_list = self._get_repl_list_rec(parsed_expr, repl_list, subs_list)
        for old, new in repl_list:
            parsed_expr = parsed_expr.replace(old, new)
        # again sp.N is annoying
        if len(subs_list) > 0:
            parsed_expr = parsed_expr.subs(subs_list)
        return parsed_expr

    def _get_repl_list_rec(self, parsed_expr, repl_list:list=[], subs_list:list=[]):
        """create a list of replacements: new functions and variables with their names as needed for the string in pyirk.
        this differentiates between local (context) names (cm.local_var) and global names (I1234["Operator1"])
        """
        # replace operators
        if hasattr(parsed_expr, "func") and isinstance(parsed_expr.func, sp.core.function.UndefinedFunction):
            func = parsed_expr.func
            if func.name in self.d["items"].keys():
                repl_list.append((func, sp.Function(self.build_reference(func.name))))
            # before pasring, the spaces in the names were removed (for sympy), now check if this is applicable here
            elif func.name.replace("_", " ") in self.d["items"].keys():
                repl_list.append((func, sp.Function(self.build_reference(func.name.replace("_", " ")))))
            else:
                repl_list.append((func, sp.Function(f"cm1.{func.name}")))
        # replace free variables
        elif isinstance(parsed_expr, sp.Symbol):
            if parsed_expr.name in self.d["items"].keys():
                subs_list.append((parsed_expr, sp.Symbol(self.build_reference(parsed_expr.name))))
            # before pasring, the spaces in the names were removed (for sympy), now check if this is applicable here
            elif parsed_expr.name.replace("_", " ") in self.d["items"].keys():
                subs_list.append((parsed_expr, sp.Symbol(self.build_reference(parsed_expr.name.replace("_", " ")))))
            else:
                subs_list.append((parsed_expr, sp.Symbol(f"cm1.{parsed_expr.name}")))
        # this is necessary, since sp.N is some existing function and the Symbol 'N' maps onto that function, which has no args
        if hasattr(parsed_expr, "args"):
            for subexpr in parsed_expr.args:
                # traverse the tree
                repl_list, subs_list = self._get_repl_list_rec(subexpr, repl_list, subs_list)
                # elif isinstance(subexpr, sp.Symbol):
                #     subs_list.append((subexpr, sp.var(f"cm.{subexpr.name}")))
        return repl_list, subs_list

    def get_expr_from_lookup(self, eq):
        # this is not a static dict, since it needs dynamic references
        if eq == 's**i * F(s) - sum(j=0, i-1, s**(i-1-j) * f**(j)(+0))':
            s = self.build_reference("s")
            dt = self.build_reference("höhere Zeitableitung")
            return f"""{s}**cm1.i * cm1.F({s}) - ma.I5441["sum over index"]({s}**(cm1.i-1-cm1.j) * {dt}(cm1.f, cm1.j)(0), cm1.j, ma.I5440["limits"](0, cm1.i-1))"""
        else:
            logger.warning("expression lookup failed")
            return '"' + eq + '"'

@u.timing
def main(statements_fpath: str, force_key_tuple=None):
    convm = ConversionManager(statements_fpath, force_key_tuple)
    convm.step1_init()
    convm.step2_parse_fnl()
    mod_fpath = convm.render()
    return mod_fpath
