with {{context.id}}.scope("setting") as cm:
    cm.new_var({{context.setting.s}}={{context.setting.p}}({{context.setting.o}}))


with {{context.id}}.scope("premise") as cm:
    {{context.premise}}


with {{context.id}}.scope("assertion") as cm:
    cm.new_rel(cm.{{context.assertion.s}}, {{context.assertion.p}}, {{context.assertion.o}})
