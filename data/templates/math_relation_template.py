{% if context.snip %}# {{context.snip}} {% endif %}
{% if context.lhs_formal %}cm.new_mathematical_relation(lhs={{context.lhs_formal}}, rsgn={{context.rsgn}}, rhs={{context.rhs_formal}}, force_key="{{context.key}}")
{% else %}cm.new_mathematical_relation(lhs=p.create_expression("{{context.lhs_source}}"), rsgn={{context.rsgn}}, rhs=p.create_expression("{{context.rhs_source}}"), force_key="{{context.key}}")
{% endif %}
