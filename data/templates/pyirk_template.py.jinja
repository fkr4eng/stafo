import pyirk as p
import sympy as sp

from ipydex import IPS, activate_ips_on_exception  # noqa

{% for load_dict in context.load_irk_modules %}
{{load_dict.prefix}} = p.irkloader.load_mod_from_uri(r"{{load_dict.uri}}", prefix="{{load_dict.prefix}}")
{% endfor %}

__URI__ = "{{context.uri_name}}"

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
