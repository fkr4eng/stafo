{% for line in context.prerequisites%}{{line}}
    {% endfor %}
{{context.key}} = p.create_item(
    {% for line in context.rel%}{{line}}
    {% endfor %}
)
