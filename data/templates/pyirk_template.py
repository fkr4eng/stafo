import pyirk as p
import sympy as sp

from ipydex import IPS, activate_ips_on_exception  # noqa

{{context.irk_module_names.control_theory}} = p.irkloader.load_mod_from_path(r"{{context.ct_path}}", prefix="{{context.irk_module_names.control_theory}}")
{{context.irk_module_names.math}} = {{context.irk_module_names.control_theory}}.ma
{{context.irk_module_names.agents}} = {{context.irk_module_names.math}}.ag

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
