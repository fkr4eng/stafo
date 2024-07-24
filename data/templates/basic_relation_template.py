{{context.key}} = p.create_relation(
    {% for line in context.rel%}{{line}}
    {% endfor %}
)
