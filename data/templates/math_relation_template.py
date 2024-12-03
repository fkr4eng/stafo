{% if context.snip %}# {{context.snip}} {% endif %}
{% if context.lhs_formal %}cm{{context.rd}}.new_math_relation(lhs={{context.lhs_formal}}, rsgn={{context.rsgn}}, rhs={{context.rhs_formal}}, force_key="{{context.key}}")
{% else %}cm{{context.rd}}.new_math_relation(lhs=p.create_expression("{{context.lhs_source}}"), rsgn={{context.rsgn}}, rhs=p.create_expression("{{context.rhs_source}}"), force_key="{{context.key}}")
{% endif %}
