import re
import os
import stafo.utils as u



class Preprocessor():
    def __init__(self, folder_name, file_name, preamble_name=None):
        self.f_path = os.path.join("data", folder_name, file_name)
        self.new_path = os.path.join("data", folder_name, "processed", file_name)
        if preamble_name:
            self.preamble_path = os.path.join("data", folder_name, preamble_name)
        else:
            self.preamble_path = None
        os.makedirs(os.path.join("data", folder_name, "processed"), exist_ok=True)

    def get_related_content(self):
        with open(self.f_path, "rt") as f:
            content = f.read()
        input_pattern = re.compile(r"(?<=\\input\{).+?(?=\})")
        res = re.findall(input_pattern, content)
        return res

    def prepare_doc(self):
        with open(self.f_path, "rt", encoding="utf-8") as f:
            content = f.read()

        # remove irrelevant content
        patterns_to_remove = [
            re.compile(r"\\begin\{figure\}.+?\\end\{figure\}", re.DOTALL),      # figures
            re.compile(r"\\begin\{maxima\}.+?\\end\{maxima\}", re.DOTALL),      # maxima code
            re.compile(r"\\index\{.+?\}"),                                      # index ref
        ]

        for pat in patterns_to_remove:
            content = re.sub(pat, "", content)

        # replace custom commands
        command_pattern_1 = re.compile(r"^\\newcommand\{(.+?)\}(\[.*\])*\{(.+)\}", re.MULTILINE)
        command_pattern_2 = re.compile(r"^\\renewcommand\{(.+?)\}(\[.*\])*\{(.+)\}", re.MULTILINE)
        commands = re.findall(command_pattern_1, content)
        commands += re.findall(command_pattern_2, content)
        if self.preamble_path:
            with open(self.preamble_path, "rt", encoding="utf-8") as f:
                preamble = f.read()
            commands += re.findall(command_pattern_1, preamble)
            commands += re.findall(command_pattern_2, preamble)

        for command in commands:
            command = list(command)
            while "" in command:
                command.remove("")
            if len(command) == 2:
                # some escaping magic necessary here: repl escapes backslashes nicely, but adds ''
                pattern = re.compile(repr(command[0]).replace("'", "") + r"(?![a-zA-Z])")
                content = re.sub(pattern, repr(command[1]).replace("'", ""), content)
            else:
                params = re.findall(r"\[.*?\]", command[1])
                # first [n] specifies total number of parameters
                num_paras = int(params[0].replace("[", "").replace("]", ""))
                if len(params) > 1:
                    # -> we have optional parameters
                    num_optional_paras = len(params) - 1
                    op_para_pat = r"(\[.*?\])?" * num_optional_paras
                else:
                    num_optional_paras = 0
                    op_para_pat = ""
                num_positional_paras = num_paras - num_optional_paras
                pos_para_pat = r"\{(.+?)\}" * num_positional_paras
                pattern = re.compile(repr(command[0]).replace("'", "") + op_para_pat + pos_para_pat, re.DOTALL)

                def get_repl(match_obj: re.Match):
                    n = len(match_obj.groups())
                    s = command[2]
                    for i in range(num_paras):
                        replacement = match_obj.group(i+1)
                        if replacement is None:
                            replacement = ""
                        s = s.replace(str(f"#{i+1}"), replacement)
                    return s
                content = re.sub(pattern, get_repl, content)

        # remove header
        if "begin{document}" in content:
            content = content.split("begin{document}")[-1]

        with open(self.new_path, "wt", encoding="utf-8") as f:
            f.write(content)




if __name__ == "__main__":
    pre = Preprocessor("nichtlinear", "grundlagen.tex", preamble_name="buch.tex")
    pre.prepare_doc()