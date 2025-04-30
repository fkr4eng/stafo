import unittest
import sys
import os
from os.path import join as pjoin
from typing import Dict, List, Union
from packaging import version
from pathlib import Path
import sympy as sp
from sympy.parsing.latex import parse_latex_lark
import re

import pyirk as p
from pyirk.utils import GeneralHousekeeperMixin

from stafo import statement_to_kg as s2k
from stafo.utils import TESTA_DATA_DIR

from ipydex import IPS, activate_ips_on_exception

activate_ips_on_exception()

TEST_DATA1_FPATH = os.path.join(TESTA_DATA_DIR, "statements01.md")
TEST_DATA2_FPATH = os.path.join(TESTA_DATA_DIR, "statements02_ring.md")
TEST_DATA3_FPATH = os.path.join(TESTA_DATA_DIR, "statements03_latex.md")
TEST_DATA4_FPATH = os.path.join(TESTA_DATA_DIR, "statements04_matching.md")
TEST_DATA5_FPATH = os.path.join(TESTA_DATA_DIR, "statements05_multilingual.md")
TEST_DATA6_FPATH = os.path.join(TESTA_DATA_DIR, "statements06_qualifier.md")

# todo this is not very elegant
# MATH_FPATH = os.path.join(os.path.abspath(os.path.join(os.path.dirname(p.__file__), "../../..", "irk-data", "ocse")), "math1.py")
# ma = p.irkloader.load_mod_from_path(MATH_FPATH, prefix="ma", reuse_loaded=False)
ma_load_dict = {"uri": "irk:/ocse/0.2/math", "prefix": "ma", "module_name": "math"}
ct_load_dict = {"uri": "irk:/ocse/0.2/control_theory", "prefix": "ct", "module_name": "control_theory"}

"""
tests/test_statements_to_kg.py::Test_02_FeatureRequest::test_c01__render_order_ring_problem
"""

TEST_URI = "irk://stafo/unittest"

def create_key_tuple(number):
    item_keys = [f"I{i}" for i in range(2000 + number - 1, 2000 - 1, -1)]
    relation_keys = [f"R{i}" for i in range(2000 + number - 1, 2000 - 1, -1)]
    return (item_keys, relation_keys)

def get_key_by_name(res_mod_path, name):
    with open(res_mod_path, "rt", encoding="utf-8") as f:
        content = f.read()
    pattern = r'[I|R]\d+(?= = p.create_\w+?\(R1__has_label="' + name + r'")'
    res = re.findall(pattern, content)
    assert len(res) == 1, f"{name} not unique in mod. result: {res}"
    return res[0]

def get_item_by_name(res_mod_path, name, mod):
    key = get_key_by_name(res_mod_path, name)
    item = getattr(mod, key)
    return item

class HousekeeperMixin(GeneralHousekeeperMixin):
    pass


class Test_00_Core(HousekeeperMixin, unittest.TestCase):

    def setUp(self) -> None:
        return super().setUp()

    def tearDown(self):
        return super().tearDown()

    def test_a01__base(self):
        # do the conversion
        CM = s2k.ConversionManager(TEST_DATA1_FPATH, num_keys=10)
        res_mod_fpath = CM.run()

        # ensure that the result can be loaded without errors

        mod = p.irkloader.load_mod_from_path(res_mod_fpath, prefix="ut")

    # test_r stands for render :)
    def test_r01__render_order_ring_problem(self):
        CM = s2k.ConversionManager(TEST_DATA2_FPATH, num_keys=40)
        res_mod_fpath = CM.run()
        # ensure that the result can be loaded without errors
        mod = p.irkloader.load_mod_from_path(res_mod_fpath, prefix="ut")
        A = get_item_by_name(res_mod_fpath, "A", mod)
        rel_key = get_key_by_name(res_mod_fpath, "has some relation to")
        self.assertEqual(
            A.get_relations(f"{mod.__URI__}#{rel_key}")[0]
            .object.get_relations(f"{mod.__URI__}#{rel_key}")[0]
            .object,
            A,
        )

    def test_r02__render_latex_equations(self):
        CM = s2k.ConversionManager(TEST_DATA3_FPATH, [ma_load_dict, ct_load_dict], num_keys=50)
        res_mod_fpath = CM.run()
        with open(res_mod_fpath, "rt") as f:
            res = f.read()

        # check 1. equation with integral
        int_res_pattern = r"""cm1.new_math_relation\(lhs=cm1.F\(I\d+\["s"\]\), rsgn="==", rhs=ma.I5443\["definite integral"\]\(\(\(I\d+\["e"\]\*\*\(-1\*I\d+\["s"\]\*I\d+\["t"\]\)\)\*cm1.f\(I\d+\["t"\]\)\), I\d+\["t"\], ma.I5440\["limits"\]\(ma.I5000\["scalar zero"\], ma.I4291\["infinity"\]\)\)"""
        int_res = re.findall(int_res_pattern, res)
        self.assertEqual(len(int_res), 1)

        # check 2. equation with derivative
        deriv_res = """cm1.new_math_relation(lhs=cm1.y(cm1.x), rsgn="==", rhs=ma.derivative(cm1.f(cm1.x), cm1.x, ma.I5001["scalar one"])"""
        self.assertIn(deriv_res, res)

        # check comments (source code before parsing)
        comment = r"# F(s) == \int\limits_0^\infty f(t)*e^{-st} dt"
        self.assertIn(comment, res)

    def test_m01__match_entities(self):
        CM = s2k.ConversionManager(TEST_DATA4_FPATH, [ma_load_dict], num_keys=20)
        res_mod_fpath = CM.run()
        with open(res_mod_fpath, "rt") as f:
            res = f.read()

        # replaced entities should appear as args
        self.assertIn('R4__is_instance_of=p.I34["complex number"]', res)
        # replaced entities should not be initialized
        self.assertNotIn('p.create_item(R1__has_label="real number"', res)
        # replaced entities should not be updated
        self.assertNotIn('["real number"].update_relations', res)

    def test_m01b__ensure_no_key_warning(self):
        # this failed for pyirk < 0.15.1
        self.assertTrue(hasattr(p.settings, "STRICT"))
        p.settings.STRICT = True

        # passing None as mod_uri should trigger a warning
        with self.assertRaises(Warning) as wrn:
            s2k.main(TEST_DATA4_FPATH, create_key_tuple(20), mod_uri=None)

        self.assertIn("key based on module irk:/builtins", wrn.exception.args[0])

        # passing a valid uri should avoid the warning
        s2k.main(TEST_DATA4_FPATH, create_key_tuple(20), mod_uri=TEST_URI)

    def test_m02__multilingual_match(self):
        CM = s2k.ConversionManager(TEST_DATA5_FPATH, [ma_load_dict, ct_load_dict], num_keys=20)
        res_mod_fpath = CM.run()
        with open(res_mod_fpath, "rt") as f:
            res = f.read()
        mod = p.irkloader.load_mod_from_path(res_mod_fpath, prefix="ut")

        # test entity matching succeeded, existing item got new alt labels
        real_part_item = p.ds.get_item_by_label("real part")
        alt_labels = [rel.object.value for rel in real_part_item.get_relations("R77")]
        self.assertIn("Re", alt_labels)
        self.assertIn("Realteil", alt_labels)

        denom_item = p.ds.get_item_by_label("denominator")
        alt_labels2 = [rel.object.value for rel in denom_item.get_relations("R77")]
        self.assertIn("Nenner", alt_labels2)

        # test no duplicate information was added
        self.assertNotIn("R8__has_domain_of_argument_1=", res)
        self.assertNotIn("R4__is_instance_of=", res)

    def test_q01__qualifier(self):
        CM = s2k.ConversionManager(TEST_DATA6_FPATH, num_keys=20)
        res_mod_fpath = CM.run()
        with open(res_mod_fpath, "rt") as f:
            res = f.read()
        mod = p.irkloader.load_mod_from_path(res_mod_fpath, prefix="ut")

        # check for the qualifier Factory
        self.assertTrue(isinstance(mod.has_position, p.QualifierFactory))

        # check validity of qualifiers
        stack1 = get_item_by_name(res_mod_fpath, "stack1", mod)
        rel_key = get_key_by_name(res_mod_fpath, "has stack component")
        stms = stack1.get_relations(f"{mod.__URI__}#{rel_key}")
        self.assertEqual(len(stms), 2)
        self.assertEqual(len(stms[0].qualifiers), 2)
        self.assertEqual(stms[0].qualifiers[0].relation.R1.value, "has position")
        self.assertEqual(stms[0].qualifiers[0].object, 0)

        stack2 = get_item_by_name(res_mod_fpath, "stack2", mod)
        stms2 = stack2.get_relations(f"{mod.__URI__}#{rel_key}")
        self.assertEqual(len(stms2), 2)
        self.assertEqual(len(stms2[0].qualifiers), 1)
        self.assertEqual(stms2[0].qualifiers[0].relation.R1.value, "has position")
        self.assertEqual(stms2[0].qualifiers[0].object, 0)
        self.assertEqual(len(stms2[1].qualifiers), 1)
        self.assertEqual(stms2[1].qualifiers[0].relation.R1.value, "is at outer position")
        self.assertEqual(stms2[1].qualifiers[0].object, True)

    # todo test qualifiers
    # todo test direct dict approach
