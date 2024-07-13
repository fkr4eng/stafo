import os, sys
import re
from ipydex import IPS
from jinja2 import Environment, FileSystemLoader
import subprocess

BASE_DIR = os.path.dirname(__file__)
TEMPLATE_DIR = os.path.join(BASE_DIR, "templates")



def get_md_lines(fpath) -> list[str]:
    with open(fpath, "rt") as f:
        raw = f.read()
    lines = raw.split("\n")
    return lines


class ConversionManager:
    def __init__(self):
        pass

    def step1(self):

        self.lines = get_md_lines("tmp.md")
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
                }

            }}
        self.items = []
        self.relations = []
        self.existing_relations = ["is applicable to", "is a subproperty of", "is an instance of", "is a subclass of"]


        self.comment_pattern = re.compile(r"- //")
        self.class_pattern = re.compile(r"(?<=There is a class: ).+?(?=\.)")
        self.property_pattern = re.compile(r"(?<=There is a property: ).+?(?=\.)")
        self.relation_pattern = re.compile(r"(?<=There is a relation: ).+?(?=\.)")


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


    def render_template(self, template: str, context: dict):
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

    def step2(self):
        # res = subprocess.run(["pyirk", "-l", os.path.join(BASE_DIR, 'control_theory1.py'), "ct", "--new-keys", "100"], capture_output=True)

        # item_keys = re.findall(r"I\d\d\d\d", res.stdout.decode())
        # relation_keys = re.findall(r"R\d\d\d\d", res.stdout.decode())
        with open("keys.txt", "rt") as f:
            keys = f.read()
        self.item_keys = re.findall(r"I\d\d\d\d", keys)
        self.relation_keys = re.findall(r"R\d\d\d\d", keys)

        for i, line in enumerate(self.lines):
            new_class = re.findall(self.class_pattern, line)
            new_property = re.findall(self.property_pattern, line)
            new_relation = re.findall(self.relation_pattern, line)
            # continue on comment
            if re.findall(self.comment_pattern, line):
                continue
            elif line == "":
                continue
            # new class?
            elif len(new_class) > 0:
                self.items.append(self.strip(new_class[0]))
                self.add_item(self.self.strip(new_class[0]), {"R4": 'p.I12["mathematical object"]'})
            # new property?
            elif len(new_property) > 0:
                self.items.append(self.strip(new_property[0]))
                self.add_item(self.strip(new_property[0]), {"R4": 'p.I54["mathematical property"]'})
            # new relation?
            elif len(new_relation) > 0:
                self.relations.append(self.strip(new_relation[0]))
                self.self.add_rel(self.strip(new_relation[0]))
            # existing relations
            else:
                for k, v in self.d["relations"].items():
                    # relations of structure: arg1 rel arg2
                    res = re.findall(f"(?<=- )(.+?)(?: {k} )(.+?)(?=\.)", line)
                    if len(res) > 0:
                        arg1, arg2 = self.strip(res[0])
                        # instance of
                        if v["key"] == "R4":
                            self.add_item(arg1, {"R4": arg2})
                        # subclass of
                        elif v["key"] == "R3":
                            self.add_item(arg1, {"R3": arg2})
                        else:
                            assert arg1 in self.d["items"].keys(), f"missing item {arg1}"
                            assert arg2 in self.d["items"].keys(), f"missing item {arg2}"
                            self.d["items"][arg1][v["key"]] = arg2
                        break
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
                                p = p.instance_of
                                o = 'p.I12["mathematical object"]'
                                print(f"pls check def: {i, line, additional_content, additional_context}")
                            additional_context["setting"] = {"s": s, "p": p, "o": o}
                            # premise
                            # todo
                            # assertion
                            if self.d["items"][arg1]["R4"] == 'p.I54["mathematical property"]':
                                p = 'p.R16["has property"]'
                            else:
                                p = 'p.R30["is secondary instance of"]'
                                print(f"pls check def: {i, line, additional_content, p}") # todo does this make sense?
                            o = f'{self.d["items"][arg1]["key"]}["{arg1}"]'
                            additional_context["assertion"] = {"s": s, "p": p, "o": o}




                            self.self.add_item(f"definition of {arg1}", additional_context)
                        else:
                            print(f"not processed line: {line}")


                if len(res) == 0:
                    print(f"not processed line: {line}")


        # for i, v in d["items"].items():
        #     context = v
        #     res = render_template("new_item__template.py", context)
        #     print(res)
        IPS()


def main():
    convm = ConversionManager()
    convm.step1()
    convm.step2()
