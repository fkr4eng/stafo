import os, sys
import re
from ipydex import IPS
from jinja2 import Environment, FileSystemLoader
import subprocess

from .utils import BASE_DIR, CONFIG_PATH, render_template


def get_md_lines(fpath) -> list[str]:
    with open(fpath, "rt") as f:
        raw = f.read()
    lines = raw.split("\n")
    return lines


class ConversionManager:
    def __init__(self, statements_fpath: str):
        self.statements_fpath = statements_fpath
        self.lines = get_md_lines(statements_fpath)

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
            "relations": {
                "is applicable to": {
                    "key": self.applicable_to_key, # todo
                    "R1": "is applicable to"
                },
                "is a subproperty of": {           # this is the dict key the way it occurs in document
                    "key": "R17",                  # this is the irk key
                    "R1": "is subproperty of"      # this is the label in irk
                },
                "is an instance of": {
                    "key": "R4",
                    "R1": "is instance of"
                },
                "is a subclass of": {
                    "key": "R3",
                    "R1": "is subclass of"
                },
                "has the definition": {
                    "key": "R37",
                    "R1": "has definition"
                },
                "has the associated LaTeX notation": {
                    "key": "R24",
                    "R1": "has LaTeX string"
                },
                "has the verbal description": {
                    "key": "R2",
                    "R1": "has description"
                },
                "has the property": {
                    "key": "R16",
                    "R1": "has property"
                }

            }}
        self.items = []
        self.relations = []
        self.existing_relations = [
            "is applicable to",
            "is a subproperty of",
            "is an instance of",
            "is a subclass of",
            "has the associated LaTeX notation",
            "has the alternative associated LaTeX notation", # todo
            "has defining formula", # todo
            "has the verbal description",
            "has the alternative label",# todo
            "is associate with",# todo
            "has the property",
            "is associated to",# todo
            ]


        self.comment_pattern = re.compile(r"- //")
        self.class_pattern = re.compile(r"(?<=There is a class: ).+?(?=\.)")
        self.property_pattern = re.compile(r"(?<=There is a property: ).+?(?=\.)")
        self.relation_pattern = re.compile(r"(?<=There is a relation: ).+?(?=\.)")
        self.unary_operator_pattern = re.compile(r"(?<=There is a unary operator: ).+?(?=\.)")
        self.binary_operator_pattern = re.compile(r"(?<=There is a binary operator: ).+?(?=\.)")
        self.type_of_arg_1_pattern = re.compile(r"(?<=The type of argument1 of )(.+?)(?: is )(.+?)(?=\.)")
        self.type_of_arg_2_pattern = re.compile(r"(?<=The type of argument2 of )(.+?)(?: is )(.+?)(?=\.)")
        self.type_of_result_pattern = re.compile(r"(?<=The result type of )(.+?)(?: is )(.+?)(?=\.)")



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
            return s.replace("'", "").replace('"', '')
        else:
            raise TypeError(s)

    def add_item(self, label, additional_relations:dict={}):
        if label not in self.d["items"].keys():
            self.d["items"][label] = {"key": self.item_keys.pop(), "R1": label}
            for k, v in additional_relations.items():
                self.d["items"][label][k] = v
        else:
            print(f"label {label} already existed")

    def add_rel(self, label, additional_relations:dict={}):
        if label not in self.d["relations"].keys():
            self.d["relations"][label] = {"key": self.relation_keys.pop(), "R1": label}
            for k, v in additional_relations.items():
                self.d["items"][label][k] = v
        else:
            print(f"label {label} already existed")

    def get_keys(self):
        """
        Get pyirk keys from a file to avoid key collisions with existing entities
        """
        # res = subprocess.run(["pyirk", "-l", os.path.join(BASE_DIR, 'control_theory1.py'), "ct", "--new-keys", "100"], capture_output=True)

        # item_keys = re.findall(r"I\d\d\d\d", res.stdout.decode())
        # relation_keys = re.findall(r"R\d\d\d\d", res.stdout.decode())
        with open(os.path.join(BASE_DIR, "keys.txt"), "rt") as f:
            keys = f.read()
        self.item_keys = re.findall(r"I\d\d\d\d", keys)
        self.relation_keys = re.findall(r"R\d\d\d\d", keys)

    def get_indent(self, line:str):
        """get indentation (number of spaces) of string"""
        indent_pattern = re.compile(r" +?(?=-)")
        indent = len(re.findall(indent_pattern, line)[0])
        return indent

    def get_sub_content(self, content):
        """return the lines that have the same (or more) indentation as the first line in content"""
        og_indent = self.get_indent(content[0])
        for i, line in enumerate(content):
            if self.get_indent(line) < og_indent:
                return content[:i]
        return content

    def recurse_nested_statements(self, content):
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
                op_pattern = re.compile(r"(OR|AND)")
                operator = re.findall(op_pattern, line)
                if operator:
                    sub_content = self.get_sub_content(content[i+1:])
                    res = self.recurse_nested_statements(sub_content)
                    # skip next lines that were processed in subroutine
                    # not really necessary anymore
                    i += len(res)
                    d= {f"{operator[0]}_{op_count}": res}
                    l.append(d)
                    op_count += 1
                else:
                    l.append(line)
            else:
                # print(f"skipping: {line}")
                pass
            i += 1
        return l


    def step2(self):
        self.get_keys()

        for i, line in enumerate(self.lines):
            # randomly the llm sometimes does not place a . at end of sentence which confuses regex
            # if len(line) > 0 and not line.endswith("."):
            #     line += "."
            if i==25:
                1+1
            new_class = re.findall(self.class_pattern, line)
            new_property = re.findall(self.property_pattern, line)
            new_relation = re.findall(self.relation_pattern, line)
            new_unary_operator = re.findall(self.unary_operator_pattern, line)
            new_binary_operator = re.findall(self.binary_operator_pattern, line)
            type_of_arg_1 = re.findall(self.type_of_arg_1_pattern, line)
            type_of_arg_2 = re.findall(self.type_of_arg_2_pattern, line)
            type_of_result = re.findall(self.type_of_result_pattern, line)


            # continue on comment
            if re.findall(self.comment_pattern, line):
                continue
            elif line == "":
                continue
            # indeted lines should be processed somewhere down below
            elif line.startswith(" "):
                print(f"line {i} skipped: {line}")
            # new class?
            elif len(new_class) > 0:
                # self.items.append(self.strip(new_class[0]))
                self.add_item(self.strip(new_class[0]), {"R4": 'p.I12["mathematical object"]'})
            # new property?
            elif len(new_property) > 0:
                # self.items.append(self.strip(new_property[0]))
                self.add_item(self.strip(new_property[0]), {"R4": 'p.I54["mathematical property"]'})
            # new relation?
            elif len(new_relation) > 0:
                # self.relations.append(self.strip(new_relation[0]))
                self.add_rel(self.strip(new_relation[0]))
            elif len(new_unary_operator) > 0:
                self.add_item(self.strip(new_unary_operator[0]), {"R4": 'p.I7[""mathematical operation with arity 1"]'})
            elif len(new_binary_operator) > 0:
                self.add_item(self.strip(new_binary_operator[0]), {"R4": 'p.I8[""mathematical operation with arity 2"]'})
            elif len(type_of_arg_1) > 0:
                arg1, arg2 = self.strip(type_of_arg_1[0])
                if arg2 not in self.d["items"].keys():
                    print(f"unknown type: {arg2}")
                self.d["items"][arg1]["R8"] = arg2
            elif len(type_of_arg_2) > 0:
                arg1, arg2 = self.strip(type_of_arg_2[0])
                if arg2 not in self.d["items"].keys():
                    print(f"unknown type: {arg2}")
                self.d["items"][arg1]["R9"] = arg2
            elif len(type_of_result) > 0:
                arg1, arg2 = self.strip(type_of_result[0])
                if arg2 not in self.d["items"].keys():
                    print(f"unknown type: {arg2}")
                self.d["items"][arg1]["R11"] = arg2
            # existing relations
            else:
                for k, v in self.d["relations"].items():
                    # relations of structure: arg1 rel arg2
                    res = re.findall(f"(?<=- )(.+?)(?: {k} )(.+?)(?=\\.)", line)
                    if len(res) > 0:
                        arg1, arg2 = self.strip(res[0])
                        # instance of
                        if v["key"] == "R4":
                            self.add_item(arg1, {"R4": arg2})
                        # subclass of
                        elif v["key"] == "R3":
                            self.add_item(arg1, {"R3": arg2})
                        else:
                            assert arg1 in self.d["items"].keys() or arg1 in self.d["relations"], f"missing item {arg1}"
                            # next line is wrong since object might be literal
                            # assert arg2 in self.d["items"].keys(), f"missing item {arg2}"
                            try:
                                self.d["items"][arg1][v["key"]] = arg2
                            except KeyError:
                                self.d["relations"][arg1][v["key"]] = arg2

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
                            try:
                                obj_type = self.d["items"][arg1][self.applicable_to_key]
                                s = obj_type
                                p = "p.uq_instance_of"
                                o = f'{self.d["items"][obj_type]["key"]}["{obj_type}"]'
                            except:
                                s = "obj"
                                p = "p.instance_of"
                                o = 'p.I12["mathematical object"]'
                                print(f"pls check def: {i, line, additional_content, additional_context}")
                            additional_context["setting"] = {"s": s, "p": p, "o": o}
                            # premise
                            additional_context["premise"] = self.recurse_nested_statements(additional_content)
                            # todo its just text
                            # assertion
                            if self.d["items"][arg1]["R4"] == 'p.I54["mathematical property"]':
                                p = 'p.R16["has property"]'
                            else:
                                p = 'p.R30["is secondary instance of"]'
                                print(f"pls check def: {i, line, additional_content, p}") # todo does this make sense?
                            o = f'{self.d["items"][arg1]["key"]}["{arg1}"]'
                            additional_context["assertion"] = {"s": s, "p": p, "o": o}

                            self.add_item(f"definition of {arg1}", additional_context)
                        else:
                            print(f"not processed line {i}: {line}")


                if len(res) == 0:
                    print(f"not processed line {i}: {line}")


        # for i, v in d["items"].items():
        #     context = v
        #     res = render_template("new_item__template.py", context)
        #     print(res)
        IPS()


def main(statements_fpath: str):
    convm = ConversionManager(statements_fpath)
    convm.step1()
    convm.step2()
