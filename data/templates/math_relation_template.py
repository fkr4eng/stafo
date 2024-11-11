{% if context.snip %}# {{context.snip}} {% endif %}
{% if context.lhs_formal %}{{context.key}} = p.new_mathematical_relation(lhs={{context.lhs_formal}}, rsgn={{context.rsgn}}, rhs={{context.rhs_formal}})
{% else %}{{context.key}} = p.new_mathematical_relation(lhs=p.create_expression("{{context.lhs_source}}"), rsgn={{context.rsgn}}, rhs=p.create_expression("{{context.rhs_source}}"))
{% endif %}
