{% if context.lhs_formal %}
{{context.key}} = p.new_equation(lhs={{context.lhs_formal}}, rhs={{context.rhs_formal}})
{% else %}
{{context.key}} = p.new_equation(lhs=p.create_expression("{{context.lhs_source}}"), rhs=p.create_expression("{{context.rhs_source}}"))
{% endif %}
