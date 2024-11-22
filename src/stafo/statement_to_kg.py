import os, sys
import re
from ipydex import IPS, Container
from jinja2 import Environment, FileSystemLoader
import subprocess
import copy
import deepdiff
import sympy as sp
from sympy.parsing.sympy_parser import T
from numbers import Real

from .utils import BASE_DIR, CONFIG_PATH, render_template, get_nested_value, set_nested_value, ParserError


def get_md_lines(fpath) -> list[str]:
    with open(fpath, "rt", encoding="utf-8") as f:
        raw = f.read()
    lines = raw.split("\n")
    return lines


class ConversionManager:
    def __init__(self, statements_fpath: str):
        self.statements_fpath = statements_fpath
        self.lines = get_md_lines(statements_fpath)
        self.entity_order = []
        self.eq_reference_dict = {}

    def sp_to_us(self, s):
        """space to underscore"""
        return s.replace(" ", "_")


    def step1(self):

        self.applicable_to_key = "R3041"
        # {items:
            # {"set":
            #   {"key": I1234, "R2": ..., "R4": ...},
            # "finite":
            #   {...}
            # },
        # relations: {}
        # }
        self.d = {"items": {},
            # todo: some of them have custom keys (as given by llm), some are copied from p.builtins. automate?
            "relations": {
                "has label": {
                    "key": "R1",
                    "R1": "has label",
                    "R22": True,
                },
                "has the verbal description": {
                    "key": "R2",
                    "R1": "has description",
                },
                "is a subclass of": {
                    "key": "R3",
                    "R1": "is subclass of",
                    "R22": True,
                },
                "is an instance of": {
                    "key": "R4",
                    "R1": "is instance of",
                    "R22": True,
                },
                "has defining formula": {
                    "key": "R6",
                    "R1": "has defining mathematical relation",
                    "R22": True,
                },
                "has domain of argument 1": {
                    "key": "R8",
                    "R1": "has domain of argument 1",
                },
                "has domain of argument 2": {
                    "key": "R9",
                    "R1": "has domain of argument 2",
                },
                "has range of result": {
                    "key": "R11",
                    "R1": "has range of result",
                },
                "is applicable to": {
                    "key": self.applicable_to_key, # todo
                    "R1": "is applicable to",
                },
                "is a subproperty of": {                # this is the dict key the way it occurs in document
                    "key": "R17",                       # this is the irk key
                    "R1": "is subproperty of",          # this is the label in irk
                },
                "is functional": {
                    "key": "R22",
                    "R1": "is functional",
                    "R22": True,
                },
                "has the definition": {
                    "key": "R37",
                    "R1": "has definition",
                    "R22": True,
                },
                "has the associated LaTeX notation": {
                    "key": "R24",
                    "R1": "has LaTeX string",
                },
                "has the alternative associated LaTeX notation": {
                    "key": "R24",
                    "R1": "has LaTeX string",
                },
                "is a secondary instance of": {
                    "key": "R30",
                    "R1": "is secondary instance of",
                },
                "has the property": {
                    "key": "R16",
                    "R1": "has property",
                },
                "does not have the property": {
                    "key": "R61",
                    "R1": "does not have property",
                },
                "has the alternative label": {
                    "key": "R77",
                    "R1": "has alternative label",
                },
                "is associated to": {
                    "key": "R58",
                    "R1": "wildcard relation",
                },
                "has explanation": {
                    "key": "R81",
                    "R1": "has explanation",
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
            self.d["relations"][key]["render"] = f'{value["key"]}__{value["R1"].replace(" ", "_")}'


        self.comment_pattern = re.compile(r"- //")
        self.new_section_pattern = re.compile(r"New.+?section")
        self.class_pattern = re.compile(r"(?<=There is a class)(?::? )(.+)")                 # sometimes : is forgotten
        self.property_pattern = re.compile(r"(?<=There is a property)(?::? )(.+)")
        self.relation_pattern = re.compile(r"(?<=There is a relation)(?::? )(.+)")
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

    #     self.special_char_repl_container = Container()
    #     self.special_char_repl_container.str_chars = ["-", " "]
    #     self.special_char_repl_container.py_chars = [ "__", "_"]
    #     # todo: What about when name has two spaces? -> prevent this!

    # def convert_name_str_to_py(self, name):
    #     for s_ch, p_ch in zip(self.special_char_repl_container.str_chars, self.special_char_repl_container.py_chars):
    #         name = name.replace(s_ch, p_ch)
    #     return name

    # def convert_name_py_to_str(self, name):
    #     for s_ch, p_ch in zip(self.special_char_repl_container.str_chars, self.special_char_repl_container.py_chars):
    #         name = name.replace(p_ch, s_ch)
    #     return name

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
            return s.replace("'", "").replace('"', '').replace(".", "").replace(":", "")
        else:
            raise TypeError(s)

    def strip_formal_eq(self, s):
        """problem examples:
        'sigma' + 'imaginary unit' * 'omega'
        s^i * Y(s)

        """
        s = s.replace('"', "'")
        s = s.replace("^", "**") # replace power operator
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

    def add_new_item(self, d, label, additional_relations:dict={}, auto_keys=False):
        if label not in d["items"].keys():
            key = self.item_keys.pop()
            d["items"][label] = {"key": key, "R1": label, "snip": self.current_snippet}
            for k, v in additional_relations.items():
                self.add_relation_inplace(d["items"][label], k, v)
            if not auto_keys:
                self.entity_order.append(key)
        else:
            print(f"label {label} already existed")
        return d

    def add_new_rel(self, d, label, additional_relations:dict={}):
        if label not in d["relations"].keys():
            key = self.relation_keys.pop()
            d["relations"][label] = {
                "key": key,
                "R1": label,
                "render": f"""{key}__{self.sp_to_us(label)}""",
                "snip": self.current_snippet}
            for k, v in additional_relations.items():
                self.add_relation_inplace(d["items"][label], k, v)
            self.entity_order.append(key)
        else:
            print(f"label {label} already existed")
        return d

    def get_keys(self):
        """
        Get pyirk keys from a file to avoid key collisions with existing entities
        """
        with open(os.path.join(BASE_DIR, "keys.txt"), "rt", encoding="utf-8") as f:
            keys = f.read()
        self.item_keys = re.findall(r"I\d\d\d\d", keys)
        self.relation_keys = re.findall(r"R\d\d\d\d", keys)

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
        l = []
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
                        temp_dict = self.process_line(copy.deepcopy(temp_dict), line_no+i, line, auto_keys=True)
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


    def step2(self):
        """iterate lines, add items and relations to dictionary
        first process lines that add items and some with special patterns, later process general relations (s p o)"""
        self.get_keys()
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
                    self.current_snippet = "m" + manual_snippet[0]
            elif line == "":
                continue
            # indeted lines should be processed somewhere down below
            elif line.startswith(" "):
                # print(f"line {i} skipped: {line}")
                pass
            # existing relations
            else:
                self.d = self.process_line(self.d, i, line)
        # IPS()

    def build_reference(self, arg2, local_dict={}):
        """return dual readable version of entity if possible (might be literal): I1234["something"]"""
        if arg2 in self.d["items"].keys():
            arg2v = self.d["items"][arg2]
            key = arg2v['key']
            if int(key[1:]) < 1000:
                arg2 = f"""p.{key}["{arg2v['R1']}"]"""
            else:
                arg2 = f"""{key}["{arg2v['R1']}"]"""
        elif arg2 in self.d["relations"].keys():
            arg2v = self.d["relations"][arg2]
            key = arg2v['key']
            if int(key[1:]) < 1000:
                arg2 = f"""p.{key}["{arg2v['R1']}"]"""
            else:
                arg2 = f"""{key}["{arg2v['R1']}"]"""
        # if we are inside a scope and arg2 references a local variable, arg2 will not appear in self.d,
        # in this case, we just need to remove potential spaces to create the reference cm.bla_bla to the local variable
        elif local_dict:
            if arg2 in local_dict["items"].keys():
                arg2 = arg2.replace(" ", "_")
        return arg2

    def process_line(self, d:dict, i:int, line:str, auto_keys=False, *args, **kwargs):
        """process the line given

        Args:
            d (dict): current dictionary to add entries to
            i (int): line_number
            line (str): line

        Returns:
            dict: current dict d
        """
        comment = re.findall(self.comment_pattern, line)
        new_section = re.findall(self.new_section_pattern, line)
        new_class = re.findall(self.class_pattern, line)
        new_property = re.findall(self.property_pattern, line)
        new_relation = re.findall(self.relation_pattern, line)
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


        # debug
        self.stop_at_line = 430
        if i == self.stop_at_line:
            1
        if len(comment) > 0:
            return d
        elif len(new_section) > 0:
            print(f"skip section mark line {i}, {line}")
            return d
        # new class?
        elif len(new_class) > 0:
            self.add_new_item(d, self.strip(new_class[0]), {"R4": 'p.I12["mathematical object"]'}, auto_keys=auto_keys)
        # new property?
        elif len(new_property) > 0:
            self.add_new_item(d, self.strip(new_property[0]), {"R4": 'p.I54["mathematical property"]'}, auto_keys=auto_keys)
        # new relation?
        elif len(new_relation) > 0:
            self.add_new_rel(d, self.strip(new_relation[0]))
        elif len(new_unary_operator) > 0:
            self.add_new_item(d, self.strip(new_unary_operator[0]), {"R4": 'p.I7["mathematical operation with arity 1"]'}, auto_keys=auto_keys)
        elif len(new_binary_operator) > 0:
            self.add_new_item(d, self.strip(new_binary_operator[0]), {"R4": 'p.I8["mathematical operation with arity 2"]'}, auto_keys=auto_keys)
        elif len(type_of_arg_1) > 0:
            # todo R8, R9, R11 should just be in general relation parsing instead of here
            arg1, arg2 = self.strip(type_of_arg_1[0])
            if arg2 not in self.d["items"].keys():
                print(f"unknown type: {arg2}")
            if arg1 in self.d["items"].keys():
                self.add_relation_inplace(d["items"][arg1], "R8", self.build_reference(arg2))
            elif arg1 in self.d["relations"].keys():
                self.add_relation_inplace(d["relations"][arg1], "R8", self.build_reference(arg2))
            else:
                raise KeyError()
        elif len(type_of_arg_2) > 0:
            arg1, arg2 = self.strip(type_of_arg_2[0])
            if arg2 not in self.d["items"].keys():
                print(f"unknown type: {arg2}")
            if arg1 in self.d["items"].keys():
                self.add_relation_inplace(d["items"][arg1], "R9", self.build_reference(arg2))
            elif arg1 in self.d["relations"].keys():
                self.add_relation_inplace(d["relations"][arg1], "R9", self.build_reference(arg2))
            else:
                raise KeyError()
        elif len(type_of_result) > 0:
            arg1, arg2 = self.strip(type_of_result[0])
            if arg2 not in self.d["items"].keys():
                print(f"unknown type: {arg2}")
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
                        elif "formal" in name:
                            # here we need to be careful, since operators might have spaces in their name. These need
                            # to be converted to not mess with the equation parser
                            eq_dict[name] = self.strip_formal_eq(res[0])
                        else:
                            eq_dict[name] = self.strip(res[0])
            d["items"][item_name] = eq_dict

        # statements
        elif len(equivalence) > 0 or len(if_then) > 0 or len(general_statement) > 0:
            if len(equivalence) > 0:
                additional_context = {"R4": 'p.I17["equivalence proposition"]', "comments": []}
                new_item_name = f"equivalence-statement_{i}"
            elif len(if_then) > 0:
                additional_context = {"R4": 'p.I15["implication proposition"]', "comments": []}
                new_item_name = f"if-then-statement_{i}"
            elif len(general_statement) > 0:
                additional_context = {"R4": 'p.I14["general mathematical proposition"]', "comments": []}
                new_item_name = f"general-statement_{i}"
            additional_content = self.get_sub_content(self.lines[i+1:])
            temp_dict = {"items": {}, "relations": {}}
            for ii, l in enumerate(additional_content):
                full_source = re.findall(self.equation_pattern_dict["full_source"], l)
                if len(full_source) > 0:
                    additional_context["comments"].append(full_source[0])
                    continue
                # todo depricated source code of scopes
                source_pre = re.findall(r"source code of premise: (.+?)(?=\.$|$)", l)
                source_ass = re.findall(r"source code of assertion: (.+?)(?=\.$|$)", l)
                if source_pre: additional_context["source_pre"] = source_pre[0]
                if source_ass: additional_context["source_ass"] = source_ass[0]
                formal = re.findall(r"(?<=formalized )(set|pre|ass)", l)
                if formal:
                    # in order for new relations in assertion to relate to the subject created in setting, the dict
                    # is passed from one scope to the next. In order to still differentiate "dict_ass - dict_set",
                    # the temp_dict is copied
                    temp_dict = copy.deepcopy(temp_dict)
                    # pass this item name down the recursion chain to the point where equations are added so we can find them later
                    self.new_item_name = new_item_name + "__" + f"formal_{formal[0]}"
                    temp_dict = self.recurse_nested_statements(self.strip(additional_content[ii+1:]), i+ii+2, temp_dict)
                    additional_context[f"formal_{formal[0]}"] = temp_dict
            # now differentiate between the dicts
            formal_keys = [key for key in additional_context.keys() if "formal" in key]
            dict_list = [additional_context[key] for key in formal_keys]
            key_pattern = re.compile(r"(?<=\[').+?(?='\])")
            if len(dict_list) > 1:
                diff_list = []
                for index in range(len(dict_list)-1):
                    diff_list.append(deepdiff.DeepDiff(dict_list[index], dict_list[index+1]))
                for index, diff in enumerate(diff_list):
                    additional_context[formal_keys[index+1]] = self.get_diffed_dict(diff)

            d = self.add_new_item(d, new_item_name, additional_context, auto_keys=auto_keys)
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
        else:
            for k, v in self.d["relations"].items():
                # relations of structure: arg1 rel arg2
                res = re.findall(f"(?<=- )(.+?)(?: {k}:? )(.+?)(?=\\.$|$)", self.strip(line))
                if len(res) > 0:
                    arg1, arg2 = self.strip(res[0])
                    arg2 = self.build_reference(arg2, d)
                    # first check for some special relation that require special attention
                    # todo having this explicite relation name here is very unelegant, pls change
                    if k == "is associated to":
                        # this relation should be symmetric so we check for that both cases in input
                        # this is used to relate equation to items, we check if this is the case and modify subj/obj
                        key_to_local_item = self.get_local_item_dict_key_interpreter(d)
                        # if arg1 is the reference obj, we need to find the correspondig item and add the relation
                        if arg1 in self.eq_reference_dict.keys():
                            eq_key = self.eq_reference_dict[arg1]["key"]
                            stm_name, scope = self.eq_reference_dict[arg1]["statement_name"].split("__")
                            # we are still in the same scope as the equation -> trivial
                            if eq_key in key_to_local_item.keys():
                                arg1 = key_to_local_item[eq_key]
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
                        self.add_new_item(d, arg1, {"R4": arg2}, auto_keys=auto_keys)
                    # subclass of
                    elif v["key"] == "R3":
                        self.add_new_item(d, arg1, {"R3": arg2}, auto_keys=auto_keys)
                    else:
                        if not (arg1 in self.d["items"].keys() or arg1 in d["items"].keys() or arg1 in self.d["relations"]):
                            self.add_new_item(d, arg1, auto_keys=auto_keys)
                            print(f"dummy item {arg1} added")
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
                        process_next_line = True
                        additional_content = []
                        k = i
                        additional_context = {"R4": 'p.I20["mathematical definition"]'}
                        while process_next_line:
                            k += 1
                            if self.lines[k].startswith(" ") and "-" in self.lines[k]:
                                additional_content.append(self.lines[k])
                            else:
                                process_next_line = False
                                #todo this could result in problem, if definition is last in file with no new line at end
                        # setting
                        # todo this data structure should be a list rather than dict for if there are multiple lines in scope
                        try:
                            obj_type = self.d["items"][arg1][self.applicable_to_key]
                            s = obj_type.split('"')[1]
                            p = "p.uq_instance_of"
                            o = obj_type
                        except KeyError:
                            s = "obj"
                            p = "p.instance_of"
                            o = 'p.I12["mathematical object"]'
                            print(f"pls check def: {i, line, additional_content, additional_context}")
                        additional_context["setting"] = {"s": s, "p": p, "o": o}
                        # premise
                        ## with this temp dict, we cover the non existing subject 'arg1' that refers to the subject in setting
                        temp_dict = None
                        if any(["arg1" in s for s in additional_content]):
                            temp_dict = {"items": {"arg1": {}}, "relations": {}}
                        additional_context["premise"] = self.recurse_nested_statements(additional_content, i, temp_dict)
                        # assertion
                        if self.d["items"][arg1]["R4"] == 'p.I54["mathematical property"]':
                            p = 'p.R16["has property"]'
                        else:
                            raise NotImplementedError()
                            # p = 'p.R30["is secondary instance of"]'
                            # print(f"pls check def: {i, line, additional_content, p}") # todo does this make sense?
                        o = f'{self.d["items"][arg1]["key"]}["{arg1}"]'
                        additional_context["assertion"] = {"s": s, "p": p, "o": o}

                        new_item_name = f"definition of {arg1}"
                        d = self.add_new_item(d, new_item_name, additional_context)
                        d["items"][arg1][v["key"]] = self.build_reference(new_item_name)
                        break
                    else:
                        print(f"maybe? not processed line {i}: {line}")

            else:
                print(f"not processed line {i}: {line}")

        return d

    def replace_expr(self, expr):
        try:
            parsed_expr = sp.parse_expr(expr)
        except:
            print(f"sympy parsing failed for {expr}")
            return expr
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
                repl_list.append((func, sp.Function(f"cm.{func.name}")))
        # replace free variables
        elif isinstance(parsed_expr, sp.Symbol):
            if parsed_expr.name in self.d["items"].keys():
                subs_list.append((parsed_expr, sp.Symbol(self.build_reference(parsed_expr.name))))
            # before pasring, the spaces in the names were removed (for sympy), now check if this is applicable here
            elif parsed_expr.name.replace("_", " ") in self.d["items"].keys():
                subs_list.append((parsed_expr, sp.Symbol(self.build_reference(parsed_expr.name.replace("_", " ")))))
            else:
                subs_list.append((parsed_expr, sp.Symbol(f"cm.{parsed_expr.name}")))
        # this is necessary, since sp.N is some existing function and the Symbol 'N' maps onto that function, which has no args
        if hasattr(parsed_expr, "args"):
            for subexpr in parsed_expr.args:
                # traverse the tree
                repl_list, subs_list = self._get_repl_list_rec(subexpr, repl_list, subs_list)
                # elif isinstance(subexpr, sp.Symbol):
                #     subs_list.append((subexpr, sp.var(f"cm.{subexpr.name}")))
        return repl_list, subs_list

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

        self.interpr = self.get_rel_dict_key_interpreter()
        if key in self.interpr.keys():
            relation = self.d["relations"][self.interpr[key]]

            # relation is functional: only one object, might be overwriting old one
            if "R22" in relation.keys() and relation["R22"] == True:
                d[key] = value
            # relation is not functional: make list or append to it
            else:
                if key in d.keys():
                    assert type(d[key]) == list, f"{d[key]} should be a list."
                    d[key].append(value)
                else:
                    d[key] = [value]

        # key is probably a special key such as 'comment' or 'formal_set'
        else:
            assert not key.startswith("R"), f"is {key} maybe a relation key that should be in d[relations]?"
            d[key] = value




        # for i, v in d["items"].items():
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
        # so far this only happens in snippet 81, with 3 equations in premise and 3 equations in assertion
        if "values_changed" in diff.keys():
            for ikey, ivalue in diff["values_changed"].items():
                key_pattern = re.compile(r"(?<=\[').+?(?='\])")
                res = re.findall(key_pattern, ikey)
                set_nested_value(current_dict, res, diff["values_changed"][ikey]["new_value"])
            dbg += 1
        if dbg != len(diff.keys()):
            raise KeyError("apparently some change between the dicts was not considered. please investigate diff.keys()")
        return current_dict

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
        rel_dict = {}
        for k,v in self.d["items"].items():
            rel_dict[v["key"]] = k
        return rel_dict

    def get_local_item_dict_key_interpreter(self, d):
        """create a dict for the items that can be addressed by pyirk keys (I1234)
        to get the long (and possibly different) literal key in d["items"]
        this is used for the local dict inside scopes
        """
        rel_dict = {}
        for k,v in d["items"].items():
            rel_dict[v["key"]] = k
        return rel_dict

    def built_simple_context(self, value_dict):
        """return context for template. works for most items and relations."""
        keys_that_want_literals = ["R1", "R2", "R24", "R77", "R81"]

        context = {"key": value_dict["key"], "rel": []}
        if "snip" in value_dict.keys():
            context["snip"] = value_dict["snip"]
        else: context["snip"] = ""
        if "comments" in value_dict.keys():
            context["comments"] = value_dict["comments"]
        else: context["comments"] = ""
        for key, value in value_dict.items():
            if key.startswith("R"):
                # first some exceptions, then the general case
                if key == "R6":
                    # the object of this relation is a reference string that appears in the 'reference' key of some equation item
                    # todo find this equation
                    pass
                elif key in keys_that_want_literals:
                    # value is literal -> need extra quotation marks ""
                    quotes = '"'
                else:
                    quotes = ""
                # R22 rels are not lists, for easier processing, put them in a list
                if not type(value) == list:
                    value = [value]
                for v in value:
                    res = re.findall(r"[R|I]\d\d\d\d", str(v))
                    # if relation expects an item (or relation), but its just a literal
                    if not quotes and len(res) == 0:
                        # then maybe the object of rel was set before the item was introduced (order in FNL)
                        if v in self.d["items"].keys():
                            v = self.build_reference(v)
                    context["rel"].append(f'{self.d["relations"][self.interpr[key]]["render"]}={quotes}{v}{quotes}')
        return context


    def render(self):
        self.interpr = self.get_rel_dict_key_interpreter()
        self.item_inter = self.get_item_dict_key_interpreter()
        self.key_to_name = dict(self.interpr)
        self.key_to_name.update(self.item_inter)
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
            context = self.built_simple_context(v)
            res = render_template(f"basic_{tag[:-1]}_template.py", context)
            output += res + "\n\n"
            count += 1

            if "equivalence-statement_" in name or "if-then-statement_" in name or "general-statement_" in name:
                context = {"id": self.build_reference(name)}
                if "snip" in v.keys():
                    context["snip"] = v["snip"]
                else: context["snip"] = ""
                if "comments" in v.keys():
                    context["comments"] = v["comments"]

                if "formal_set" in v.keys():
                    context["setting"] = self.get_statement_context_recursively(v[f"formal_set"])
                elif "source_set" in v.keys():
                    context["setting"] = [f'cm.create_expression({v["source_set"]})']

                if "formal_pre" in v.keys():
                    context["premise"] = self.get_statement_context_recursively(v[f"formal_pre"])
                elif "source_pre" in v.keys():
                    context["premise"] = [f'cm.create_expression({v["source_pre"]})']

                if "formal_ass" in v.keys():
                    context["assertion"] = self.get_statement_context_recursively(v[f"formal_ass"])
                elif "source_ass" in v.keys():
                    context["assertion"] = [f'cm.create_expression({v["source_ass"]})']
                res = render_template("statement_template.py", context)
                output += res + "\n\n"

        try:
            import pyirk as p
            ct_path = os.path.join(os.path.abspath(os.path.join(os.path.dirname(p.__file__), "../../..", "irk-data", "ocse")), "control_theory1.py")
        except:
            ct_path = ""

        pyirk_context = {"uri_name": f"auto_import_{os.path.split(self.statements_fpath)[-1].split('.')[0]}",
                         "ct_path": ct_path,
                         "content": output}

        res = render_template("pyirk_template.py", pyirk_context)

        fpath = "output.py"
        with open(fpath, "wt", encoding="utf-8") as f:
            f.write(res)
        print(f"{count} new entities written to {fpath}.")

    # def get_statement_context(self, subdict, part):

    def get_statement_context_recursively(self, subdict:dict):
        # output
        out = []
        # insertion index makes sure that item creation happens before relations are added, that reference said items
        insertion_index = 0
        for key, value in subdict["items"].items():
            # if key == "other":
            if "equation" in key or "math_relation" in key:
                if value["type"] in ["equation", "mathematical relation"]:
                    res = self.render_math_relation(value)
                    for l in res.split("\n"):
                        # adapt equation to context manager
                        # l = re.sub(r".+? = p.new_mathematical_relation", r"cm.new_mathematical_relation", l)
                        if len(l) > 0 and not "snippet" in l:
                            out.append(l)
                else:
                    raise TypeError()
            elif "OR" in key or "AND" in key:
                res = self.get_statement_context_recursively(subdict["items"][key])
                s = "["
                for r in res:
                    s += r + ", "
                    s.replace("\n", "") # remove \n from r
                op = key.split("_")[0]
                out.append(f"cm.{op}({s[:-2]}])")  # remove last ", "
            else:
                key = self.strip_math(key).replace(" ", "_")
                if "R4" in value.keys():
                    out.insert(insertion_index, f'cm.new_var({key}=p.uq_instance_of({value["R4"]}))')
                    insertion_index += 1
                else:
                    out.insert(insertion_index, f'cm.new_var({key}=p.uq_instance_of(p.I12["mathematical object"]))')
                    insertion_index += 1
                for kk, vv in value.items():
                    number = re.findall(r"(?<=R)\d+", kk)
                    if number and int(number[0]) > 4: # just exclude R1-R4 here
                        if not type(vv) == list:
                            vv = [vv]
                        for vvv in vv:
                            # some exceptions when not to add cm.
                            # in case of literals (numbers)
                            if isinstance(vvv, Real):
                                obj_str = f"{vvv}"
                            # in case of equation references (global item names)
                            elif re.findall(r"I\d\d\d\d", vvv):
                                obj_str = f"{vvv}"
                            else:
                                obj_str = f"cm.{vvv}"
                            out.append(f'cm.new_relation(cm.{key}, {self.build_reference(self.interpr[kk])}, {obj_str})')
        return out

    def render_math_relation(self, eq_dict):
        context = {"key": eq_dict["key"], "rel": []}
        if "snip" in eq_dict.keys():
            context["snip"] = eq_dict["snip"]
        else: context["snip"] = ""
        if "comments" in eq_dict.keys():
            context["comments"] = eq_dict["comments"]

        if eq_dict["type"] == "equation":
            context["rsgn"] = '"=="'
        elif eq_dict["type"] == "mathematical relation":
            context["rsgn"] = f'"{eq_dict["rel_sign"]}"'

        if "lhs_formal" in eq_dict.keys():
            context["lhs_formal"] = self.replace_expr(eq_dict["lhs_formal"])
        elif "lhs_source" in eq_dict.keys():
            context["lhs_source"] = eq_dict["lhs_source"]
        if "rhs_formal" in eq_dict.keys():
            context["rhs_formal"] = self.replace_expr(eq_dict["rhs_formal"])
        elif "rhs_source" in eq_dict.keys():
            context["rhs_source"] = eq_dict["rhs_source"]
        res = render_template("math_relation_template.py", context)
        return res



def main(statements_fpath: str):
    convm = ConversionManager(statements_fpath)
    convm.step1()
    convm.step2()
    convm.render()
