{% if context.snip %}# {{context.snip}} {% endif %}
{{context.key}}["{{context.name}}"].update_relations(
    {% for line in context.rel%}{{line}},
    {% endfor %}{% if context.comments %}{% for line in context.comments%}# {{line}}{% endfor %}{% endif %}
)
{% for line in context.extra%}{{line}}{% endfor %}