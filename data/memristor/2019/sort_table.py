import re

with open("data/memristor/2019/table_og.md", "rt") as f:
    content = f.read()
lines = content.split("\n")
new_lines = []
begin_body = 9999
for i, line in enumerate(lines):
    if "Mechanism" in line and "Selector geometry" in line:
        # detect table head
        new_lines.append("|Source " + line)
        # add column for citations
        begin_body = i + 1
    elif i == begin_body:
        new_lines.append("|-" + line)
    elif i > begin_body and line.count("|") > 2:
        res = re.findall(r"\d+(?= *\|)", line.split("|")[2]+"|")
        if res:
            split = line.split("|")
            split[2] = re.sub(r"\d+(?= *\|)", "", line.split("|")[2]+"|")[:-1]
            new_line = f"|{res[0]}" + "|".join(split)
            new_lines.append(new_line)
    # else:
    #     new_lines.append(line)
with open("data/memristor/2019/table.md", "wt") as f:
    f.write("\n".join(new_lines))
