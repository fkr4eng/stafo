with ma.IntegerRangeElement(start={{context.start}}, stop={{context.stop}}) as {{context.index_var}}:{% for line in context.content%}
{{context.indent}}    {{line}}{% endfor %}
