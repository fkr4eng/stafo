{% if context.snip %}# {{context.snip}} {% endif %}
with {{context.id}}.scope("setting") as cm{{context.rd}}:{% if context.setting %}{% for line in context.setting%}
    {{line}}{% endfor %}
    {% else %}
    pass{% endif %}

with {{context.id}}.scope("premise") as cm{{context.rd}}:{% if context.premise %}{% for line in context.premise%}
    {{line}}{% endfor %}
    {% else %}
    pass{% endif %}

with {{context.id}}.scope("assertion") as cm{{context.rd}}:{% if context.assertion %}{% for line in context.assertion%}
    {{line}}{% endfor %} {% endif %}


