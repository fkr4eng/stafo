import pyirk as p
import sympy as sp

from ipydex import IPS, activate_ips_on_exception  # noqa

{% if context.ct_path %}
{% endif %}
{% if context.ma_path %}
{{context.irk_module_names.math}} = p.irkloader.load_mod_from_path(r"{{context.ma_path}}", prefix="{{context.irk_module_names.math}}")
{% endif %}
{% if context.ag_path %}
{{context.irk_module_names.agents}} = p.irkloader.load_mod_from_path(r"{{context.ag_path}}", prefix="{{context.irk_module_names.agents}}")
{% endif %}

{% for irk_module in context.additional_modules %}
{{irk_module.module_name}} = p.irkloader.load_mod_from_path(r"{{irk_module.path}}", prefix="{{irk_module.prefix}}")
{% endfor %}

__URI__ = "irk:/ocse/0.2/{{context.uri_name}}"

keymanager = p.KeyManager()
p.register_mod(__URI__, keymanager)
p.start_mod(__URI__)

# these entities are declared here all at once in order to avoid referencing issues when setting relations.
# the relations of these entities are set below with the update method. This update method is called exactly once.
{{context.entity_declaration}}

########################################################################################################################
# content:
########################################################################################################################

{{context.content}}

p.end_mod()
