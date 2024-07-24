with {{context.id}}.scope("setting") as cm:
    {% if context.setting %}cm.new_var({{context.setting.s}}={{context.setting.p}}({{context.setting.o}}))
    {% else %}pass{% endif %}

with {{context.id}}.scope("premise") as cm:
    # {{context.premise}}
    pass

with {{context.id}}.scope("assertion") as cm:
    # {{context.assertion}}
    pass
