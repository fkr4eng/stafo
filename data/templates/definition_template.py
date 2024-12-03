{% if context.snip %}# {{context.snip}} {% endif %}
with {{context.id}}.scope("setting") as cm{{context.rd}}:
    cm{{context.rd}}.new_var({{context.setting.s}}={{context.setting.p}}({{context.setting.o}}))

with {{context.id}}.scope("premise") as cm{{context.rd}}:
    {{context.premise}}

with {{context.id}}.scope("assertion") as cm{{context.rd}}:
    cm{{context.rd}}.new_rel(cm{{context.rd}}.{{context.assertion.s}}, {{context.assertion.p}}, {{context.assertion.o}})
