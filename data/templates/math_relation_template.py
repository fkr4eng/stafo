{% if context.snip %}# {{context.snip}} {% endif %}
{% if context.rhs_formal is defined %}{{context.key}} = cm{{context.rd}}.new_math_relation(lhs={{context.lhs_formal}}, rsgn={{context.rsgn}}, rhs={{context.rhs_formal}}, force_key="{{context.key}}")
{% elif context.rhs_source is defined %}{{context.key}} = cm{{context.rd}}.new_math_relation(lhs=p.create_expression("{{context.lhs_source}}"), rsgn={{context.rsgn}}, rhs=p.create_expression("{{context.rhs_source}}"), force_key="{{context.key}}")
{% elif context.full_source is defined %}{{context.key}} = p.create_expression("{{context.full_source}}")
{% endif %}
{% comment %} is defined instead of just testing for rhs_formal is important since one side of the equation might be 0 {% endcomment %}