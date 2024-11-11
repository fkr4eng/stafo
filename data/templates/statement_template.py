{% if context.snip %}# {{context.snip}} {% endif %}
with {{context.id}}.scope("setting") as cm:
    {% if context.setting %}{% for line in context.setting%}
    {{line}}{% endfor %}
    {% else %}pass{% endif %}

with {{context.id}}.scope("premise") as cm:
    {% if context.premise %}{% for line in context.premise%}
    {{line}}{% endfor %} {% endif %}

with {{context.id}}.scope("assertion") as cm:
    {% if context.assertion %}{% for line in context.assertion%}
    {{line}}{% endfor %} {% endif %}


