import os, sys
import re
from ipydex import IPS
from jinja2 import Environment, FileSystemLoader
import subprocess
import copy
import deepdiff

from .utils import BASE_DIR, CONFIG_PATH, render_template, get_nested_value, set_nested_value


def get_md_lines(fpath) -> list[str]:
    with open(fpath, "rt", encoding="utf-8") as f:
        raw = f.read()
    lines = raw.split("\n")
    return lines


class ConversionManager:
    def __init__(self, statements_fpath: str):
        self.statements_fpath = statements_fpath
        self.lines = get_md_lines(statements_fpath)

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
        self.d = {"items": {"other": []},
            # todo: some of them have custom keys (as given by llm), some are copied from p.builtins. automate?
            "relations": {
                "has label": {
                    "key": "R1",
                    "R1": "has label",
                    "render": "R1__has_label"
                },
                "has the verbal description": {
                    "key": "R2",
                    "R1": "has description",
                    "render": "R2__has_description"
                },
                "is a subclass of": {
                    "key": "R3",
                    "R1": "is subclass of",
                    "render": "R3__is_subclass_of"
                },
                "is an instance of": {
                    "key": "R4",
                    "R1": "is instance of",
                    "render": "R4__is_instance_of"
                },
                "has defining formula": {
                    "key": "R6",
                    "R1": "has defining mathematical relation",
                    "render": "R6__has_defining_mathematical_relation"
                },
                "has domain of argument 1": {
                    "key": "R8",
                    "R1": "has domain of argument 1",
                    "render": "R8__has_domain_of_argument_1"
                },
                "has domain of argument 2": {
                    "key": "R9",
                    "R1": "has domain of argument 2",
                    "render": "R9__has_domain_of_argument_2"
                },
                "has range of result": {
                    "key": "R11",
                    "R1": "has range of result",
                    "render": "R11__has_range_of_result"
                },
                "is applicable to": {
                    "key": self.applicable_to_key, # todo
                    "R1": "is applicable to",
                    "render": f"{self.applicable_to_key}__is_applicable_to"
                },
                "is a subproperty of": {                # this is the dict key the way it occurs in document
                    "key": "R17",                       # this is the irk key
                    "R1": "is subproperty of",          # this is the label in irk
                    "render": "R17__is_subproperty_of"  # this is for the rendered template
                },
                "has the definition": {
                    "key": "R37",
                    "R1": "has definition",
                    "render": "R37__has_definition"
                },
                "has the associated LaTeX notation": {
                    "key": "R24",
                    "R1": "has LaTeX string",
                    "render": "R24__has_associated_LaTeX_notation"
                },
                "has the property": {
                    "key": "R16",
                    "R1": "has property",
                    "render": "R16__has_property"
                },
                "has the alternative label": {
                    "key": "R77",
                    "R1": "has alternative label",
                    "render": "R77__has_alternative_label"
                },
                "is associated to": {
                    "key": "R58",
                    "R1": "wildcard relation",
                    "render": "R58__wildcard_relation"
                },
                "has explanation": {
                    "key": "R81",
                    "R1": "has explanation",
                    "render": "R81__has_explanation"
                },

            }}
        """
            # todo:
            "has the alternative associated LaTeX notation",
            "is associate with",
            "is associated to",
            "There is an example:",
            "There is an explanation:",
            "There is special terminology:"
            "alternative verbal description?
        """


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
            "lhs_source": re.compile(r"(?<=- source code of left hand side)(?::? )(.+?)(?=\.$|$)"),
            "rhs_source": re.compile(r"(?<=- source code of right hand side)(?::? )(.+?)(?=\.$|$)"),
            "lhs_formal": re.compile(r"(?<=- formalized left hand side)(?::? )(.+?)(?=\.$|$)"),
            "rhs_formal": re.compile(r"(?<=- formalized right hand side)(?::? )(.+?)(?=\.$|$)"),
            "reference": re.compile(r"(?<=- reference)(?::? )(.+)")
        }
        self.math_rel_pattern_dict = copy.deepcopy(self.equation_pattern_dict)
        self.math_rel_pattern_dict["rel_sign"] = re.compile(r"(?<=- relation sign)(?::? )(.+?)(?=\.$|$)")
        self.explanation_pattern_dict = {
            "related": re.compile(r"(?<=- related to)(?::? )(.+?)(?=\.$|$)"),
            "verbal": re.compile(r"(?<=- verbal summary)(?::? )(.+?)(?=\.$|$)"),
        }

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

    def add_item(self, d, label, additional_relations:dict={}):
        if label not in d["items"].keys():
            d["items"][label] = {"key": self.item_keys.pop(), "R1": label, "snip": self.current_snippet}
            for k, v in additional_relations.items():
                d["items"][label][k] = v
        else:
            print(f"label {label} already existed")
        return d

    def add_rel(self, d, label, additional_relations:dict={}):
        if label not in d["relations"].keys():
            key = self.relation_keys.pop()
            d["relations"][label] = {
                "key": key,
                "R1": label,
                "render": f"""{key}__{self.sp_to_us(label)}""",
                "snip": self.current_snippet}
            for k, v in additional_relations.items():
                d["items"][label][k] = v
        else:
            print(f"label {label} already existed")
        return d

    def get_keys(self):
        """
        Get pyirk keys from a file to avoid key collisions with existing entities
        """
        # res = subprocess.run(["pyirk", "-l", os.path.join(BASE_DIR, 'control_theory1.py'), "ct", "--new-keys", "100"], capture_output=True)

        # item_keys = re.findall(r"I\d\d\d\d", res.stdout.decode())
        # relation_keys = re.findall(r"R\d\d\d\d", res.stdout.decode())
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
        [{"OR": [
            {"AND": [statement1, statement2]},
            statement3
        ]}]
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
                    res = self.recurse_nested_statements(sub_content, line_no+i+1, temp_dict=temp_dict)
                    # skip next lines that were processed in subroutine
                    # not really necessary anymore
                    i += len(res)
                    # d= {f"{operator[0]}_{op_count}": res}
                    # l.append(d)
                    # temp_dict[f"{operator[0]}_{op_count}"] = res

                    op_count += 1
                else:
                    # l.append(line)
                    if temp_dict is not None:
                        # l.append(self.process_line(copy.deepcopy(temp_dict), line_no+i, line))
                        self.process_line(temp_dict, line_no+i, line)
                    else:
                        # l.append(self.process_line({}, None, line))
                        raise ValueError()

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
                if len(snippet) > 0:
                    self.current_snippet = snippet[0]
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

    def build_reference(self, arg2):
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
        return arg2

    def process_line(self, d:dict, i:int, line:str, *args, **kwargs):
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
        # if i == 41:
        #     1
        if len(comment) > 0:
            return d
        elif len(new_section) > 0:
            print(f"skip section mark line {i}, {line}")
            return d
        # new class?
        elif len(new_class) > 0:
            # self.items.append(self.strip(new_class[0]))
            self.add_item(d, self.strip(new_class[0]), {"R4": 'p.I12["mathematical object"]'})
        # new property?
        elif len(new_property) > 0:
            # self.items.append(self.strip(new_property[0]))
            self.add_item(d, self.strip(new_property[0]), {"R4": 'p.I54["mathematical property"]'})
        # new relation?
        elif len(new_relation) > 0:
            # self.relations.append(self.strip(new_relation[0]))
            self.add_rel(d, self.strip(new_relation[0]))
        elif len(new_unary_operator) > 0:
            self.add_item(d, self.strip(new_unary_operator[0]), {"R4": 'p.I7["mathematical operation with arity 1"]'})
        elif len(new_binary_operator) > 0:
            self.add_item(d, self.strip(new_binary_operator[0]), {"R4": 'p.I8["mathematical operation with arity 2"]'})
        elif len(type_of_arg_1) > 0:
            # todo R8, R9, R11 should just be in general relation parsing instead of here
            arg1, arg2 = self.strip(type_of_arg_1[0])
            if arg2 not in self.d["items"].keys():
                print(f"unknown type: {arg2}")
            if arg1 in self.d["items"].keys():
                d["items"][arg1]["R8"] = self.build_reference(arg2)
            elif arg1 in self.d["relations"].keys():
                d["relations"][arg1]["R8"] = self.build_reference(arg2)
            else:
                raise KeyError()
        elif len(type_of_arg_2) > 0:
            arg1, arg2 = self.strip(type_of_arg_2[0])
            if arg2 not in self.d["items"].keys():
                print(f"unknown type: {arg2}")
            if arg1 in self.d["items"].keys():
                d["items"][arg1]["R9"] = self.build_reference(arg2)
            elif arg1 in self.d["relations"].keys():
                d["relations"][arg1]["R9"] = self.build_reference(arg2)
            else:
                raise KeyError()
        elif len(type_of_result) > 0:
            arg1, arg2 = self.strip(type_of_result[0])
            if arg2 not in self.d["items"].keys():
                print(f"unknown type: {arg2}")
            if arg1 in self.d["items"].keys():
                d["items"][arg1]["R11"] = self.build_reference(arg2)
            elif arg1 in self.d["relations"].keys():
                d["relations"][arg1]["R11"] = self.build_reference(arg2)
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
        elif len(equation) > 0:
            lines = self.get_sub_content(self.lines[i+1:])
            eq_dict = {
                "type": "equation",
                "key": self.item_keys.pop(),
                "snip": self.current_snippet
                }
            for l in lines:
                for name, pattern in self.equation_pattern_dict.items():
                    res = re.findall(pattern, l)
                    if res: eq_dict[name] = self.strip(res[0])
            d["items"]["other"].append(eq_dict)
        elif len(math_rel) > 0:
            lines = self.get_sub_content(self.lines[i+1:])
            math_rel_dict = {
                "type": "mathematical relation",
                "key": self.item_keys.pop(),
                "snip": self.current_snippet
                }
            for l in lines:
                for name, pattern in self.math_rel_pattern_dict.items():
                    res = re.findall(pattern, l)
                    if res: math_rel_dict[name] = self.strip(res[0])
            d["items"]["other"].append(math_rel_dict)
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
            temp_dict = {"items": {"other":[]}, "relations": {}}
            for ii, l in enumerate(additional_content):
                full_source = re.findall(self.equation_pattern_dict["full_source"], l)
                if len(full_source) > 0:
                    additional_context["comments"].append(full_source[0])
                    continue
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
                    additional_context[f"formal_{formal[0]}"] = self.recurse_nested_statements(self.strip(additional_content[ii+1:]), i+ii+2, temp_dict)
            # now differentiate between the dicts
            formal_keys = [key for key in additional_context.keys() if "formal" in key]
            dict_list = [additional_context[key] for key in formal_keys]
            if len(dict_list) > 1:
                diff_list = []
                for index in range(len(dict_list)-1):
                    diff_list.append(deepdiff.DeepDiff(dict_list[index], dict_list[index+1]))
                for index, diff in enumerate(diff_list):
                    dbg = 0
                    current_dict = additional_context[formal_keys[index+1]] = {"items": {"other":[]}, "relations": {}}
                    if "iterable_item_added" in diff.keys():
                        for ikey, ivalue in diff["iterable_item_added"].items():
                            key_pattern = re.compile(r"(?<=\[').+?(?='\])")
                            res = re.findall(key_pattern, ikey)
                            prev = get_nested_value(current_dict, res)
                            prev.append(ivalue)
                            set_nested_value(current_dict, res, prev)
                        dbg += 1

                    if "dictionary_item_added" in diff.keys():
                        for ikey in diff["dictionary_item_added"]:
                            key_pattern = re.compile(r"(?<=\[').+?(?='\])")
                            res = re.findall(key_pattern, ikey)
                            set_nested_value(current_dict, res, get_nested_value(diff.t2, res))
                        dbg += 1
                    if dbg != len(diff.keys()):
                        raise KeyError("apparently some change between the dicts was not considered. please investigate diff.keys()")


            d = self.add_item(d, new_item_name, additional_context)
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
                    arg2 = self.build_reference(arg2)
                    # instance of
                    if v["key"] == "R4":
                        self.add_item(d, arg1, {"R4": arg2})
                    # subclass of
                    elif v["key"] == "R3":
                        self.add_item(d, arg1, {"R3": arg2})
                    else:
                        if not (arg1 in self.d["items"].keys() or \
                            arg1 in d["items"].keys() or \
                            arg1 in self.d["relations"]):
                            self.add_item(d, arg1)
                            print(f"dummy item {arg1} added")
                        if arg1 in d["items"]:
                            d["items"][arg1][v["key"]] = arg2
                        elif arg1 in d["relations"]:
                            d["relations"][arg1][v["key"]] = arg2
                        else:
                            raise KeyError
                        # todo: keep an eye out for this change, why would a scope reference something outside as a subject?
                        # elif arg1 in self.d["items"]:
                        #     self.d["items"][arg1][v["key"]] = arg2
                        # elif arg1 in self.d["relations"]:
                        #     self.d["relations"][arg1][v["key"]] = arg2


                    break
                # relations of structure arg1 rel.
                res = re.findall(f"(?<=- )(.+?)(?: {k})", line)
                if len(res) > 0:
                    arg1 = self.strip(res[0])
                    # definition
                    if v["key"] == "R37":
                        # resolve if this is def for property or concept or something else?

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
                        d = self.add_item(d, new_item_name, additional_context)
                        d["items"][arg1][v["key"]] = self.build_reference(new_item_name)
                        break
                    else:
                        print(f"not processed line {i}: {line}")

            else:
                print(f"not processed line {i}: {line}")

        return d


        # for i, v in d["items"].items():

    def get_rel_dict_key_interpreter(self):
        """create a dict for the relations that can be addressed by pyirk keys (R1)
        to get the long (and possibly different) literal key in self.d["relations"]"""
        rel_dict = {}
        for k,v in self.d["relations"].items():
            rel_dict[v["key"]] = k
        return rel_dict

    def built_simple_context(self, value_dict):
        """return context for template. works for most items and relations."""
        keys_that_want_literals = ["R1", "R2", "R24"]

        context = {"key": value_dict["key"], "rel": [], "prerequisites": []}
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
                    lhs, rhs = value.split(r"\isdef")
                    lhs = lhs.replace("`", "").replace("$", "")
                    rhs = rhs.replace("`", "").replace("$", "")
                    item_key = self.item_keys.pop()
                    eq = f'{item_key} = p.new_equation(lhs=p.create_expression("${lhs}$"), rhs=p.create_expression("${rhs}$"))'
                    context["prerequisites"].append(eq)
                    line = f'{self.d["relations"][self.interpr[key]]["render"]}={item_key}'
                elif key in keys_that_want_literals:
                    # value is literal -> need ""
                    line = f'{self.d["relations"][self.interpr[key]]["render"]}="{value}"'
                else:
                    line = f'{self.d["relations"][self.interpr[key]]["render"]}={value}'
                context["rel"].append(line)
        return context

    def recursively_render_premise(self, premise_obj, setting_subj):
        out = ""
        for key, value in premise_obj.items():
            if "OR" in key or "AND" in key:
                res = [self.recursively_render_premise(arg, setting_subj) for arg in value]
                s = ""
                for r in res:
                    s += r[:-1] + ", " # remove \n from r
                op = key.split("_")[0]
                out += f"cm.{op}({s[:-2]})\n" # remove last ", "
            elif key == "items":
                for k, v in value.items():
                    if k == "arg1":
                        s = setting_subj
                    else:
                        s = k
                    # todo: these should always only have one entry, right !?
                    p = list(v.keys())[0]
                    o = list(v.values())[0]
                    out += f"cm.new_rel(cm.{s}, {self.build_reference(self.interpr[p])}, {o})\n"
            elif key == "relations":
                pass
            else:
                raise ValueError()
        return out

    def render(self):
        self.interpr = self.get_rel_dict_key_interpreter()
        output = ""
        count = 0
        # render new relations
        for rel, v in self.d["relations"].items():
            # check for new relations and discard small numbered keys (builtins)
            if int(v["key"].split("R")[1]) >= 1000:
                context = self.built_simple_context(v)
                res = render_template("basic_relation_template.py", context)
                output += res + "\n\n"
                count += 1
        # render new items
        for item, v in self.d["items"].items():
            if item != "other":
                context = self.built_simple_context(v)
                res = render_template("basic_item_template.py", context)
                output += res + "\n\n"
                count += 1

                # handle more exitic concepts
                if "definition" in item:
                    context = {"id": self.build_reference(item)}
                    if "snip" in v.keys():
                        context["snip"] = v["snip"]
                    else: context["snip"] = ""
                    if "comments" in v.keys():
                        context["comments"] = v["comments"]
                    if "setting" in v.keys():
                        context["setting"] = v["setting"]
                    if "premise" in v.keys():
                        context["premise"] = self.recursively_render_premise(v["premise"][0], v["setting"]["s"])
                    if "assertion" in v.keys():
                        context["assertion"] = v["assertion"]
                    res = render_template("definition_template.py", context)
                    output += res + "\n\n"

                elif "equivalence-statement" in item or "if-then" in item:
                    context = {"id": self.build_reference(item)}
                    if "snip" in v.keys():
                        context["snip"] = v["snip"]
                    else: context["snip"] = ""
                    if "comments" in v.keys():
                        context["comments"] = v["comments"]
                    context["setting"] = []
                    if "setting" in v.keys():
                        context["setting"].append(v["setting"])

                    if "formal_pre" in v.keys():
                        context = self.get_equiv_context(context, v, "premise")
                    elif "source_pre" in v.keys():
                        context["premise"] = [f'cm.create_expression({v["source_pre"]})']

                    if "formal_ass" in v.keys():
                        context = self.get_equiv_context(context, v, "assertion")
                    elif "source_ass" in v.keys():
                        context["assertion"] = [f'cm.create_expression({v["source_ass"]})']
                    res = render_template("equivalence_template.py", context)
                    output += res + "\n\n"

            else:
                for other_dict in v:
                    if other_dict["type"] == "equation":
                        res = self.render_equation(other_dict)
                        output += res + "\n\n"
                    else:
                        raise TypeError()

        fpath = "output.py"
        with open(fpath, "wt", encoding="utf-8") as f:
            f.write(output)
        print(f"{count} new entities written to {fpath}.")

    def get_equiv_context(self, context:dict, v:dict, part:str):
        context[part] = []
        for key, value in v[f"formal_{part[:3]}"]["items"].items():
            if key == "other":
                # iterate over list of dicts
                for d in value:
                    if d["type"] == "equation":
                        res = self.render_equation(d)
                        for l in res.split("\n"):
                            # adapt equation to context manager
                            l = re.sub(r".+? = p.new_equation", r"cm.new_equation", l)
                            context[part].append(l)
                    else:
                        raise TypeError()
            else:
                if "R4" in value.keys():
                    context["setting"].append(f'cm.new_var({self.strip_math(key)}=p.uq_instance_of({value["R4"]}))')
                else:
                    context["setting"].append(f'cm.new_var({self.strip_math(key)}=p.uq_instance_of(p.I12["mathematical object"]))')
                for kk, vv in value.items():
                    number = re.findall(r"(?<=R)\d+", kk)
                    if number and int(number[0]) > 4: # just exclude R1-R4 here
                        context[part].append(f'cm.new_relation({self.strip_math(key)}, {self.build_reference(self.interpr[kk])}, {self.strip_math(vv)})')
        return context

    def render_equation(self, eq_dict):
        context = {"key": eq_dict["key"], "rel": [], "prerequisites": []}
        if "snip" in eq_dict.keys():
            context["snip"] = eq_dict["snip"]
        else: context["snip"] = ""
        if "comments" in eq_dict.keys():
            context["comments"] = eq_dict["comments"]
        if "lhs_formal" in eq_dict.keys():
            context["lhs_formal"] = eq_dict["lhs_formal"]
        elif "lhs_source" in eq_dict.keys():
            context["lhs_source"] = eq_dict["lhs_source"]
        if "rhs_formal" in eq_dict.keys():
            context["rhs_formal"] = eq_dict["rhs_formal"]
        elif "rhs_source" in eq_dict.keys():
            context["rhs_source"] = eq_dict["rhs_source"]
        res = render_template("equation_template.py", context)
        return res



def main(statements_fpath: str):
    convm = ConversionManager(statements_fpath)
    convm.step1()
    convm.step2()
    convm.render()
