{% if context.snip %}# {{context.snip}} {% endif %}
{{context.key}} = p.create_relation(
    {% for line in context.rel%}{{line}}
    {% endfor %}
)
