import pyirk as p
import sympy as sp

from ipydex import IPS, activate_ips_on_exception  # noqa

ct = p.irkloader.load_mod_from_path(r"{{context.ct_path}}", prefix="ct")
ma = ct.ma
ag = ma.ag

__URI__ = "irk:/ocse/0.2/{{context.uri_name}}"

keymanager = p.KeyManager()
p.register_mod(__URI__, keymanager)
p.start_mod(__URI__)

{{context.content}}

IPS()