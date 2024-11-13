{% if context.snip %}# {{context.snip}} {% endif %}
{{context.key}} = p.create_item(
    {% for line in context.rel%}{{line}},
    {% endfor %}{% if context.comments %}{% for line in context.comments%}# {{line}}{% endfor %}{% endif %}
)
