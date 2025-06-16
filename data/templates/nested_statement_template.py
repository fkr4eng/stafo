with p.ImplicationStatement() as cm{{context.rd}}:{% if context.setting %}{% for line in context.setting%}
{{context.indent}}    {{line}}{% endfor %}{% endif %}{% if context.premise %}{% for line in context.premise%}
{{context.indent}}    cm{{context.rd}}.antecedent_relation{{line}}{% endfor %}{% endif %}{% if context.assertion %}{% for line in context.assertion%}
{{context.indent}}    cm{{context.rd}}.consequent_relation{{line}}{% endfor %}{% endif %}