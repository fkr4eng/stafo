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

# todo this is not very elegant
MATH_FPATH = os.path.join(os.path.abspath(os.path.join(os.path.dirname(p.__file__), "../../..", "irk-data", "ocse")), "math1.py")
ma = p.irkloader.load_mod_from_path(MATH_FPATH, prefix="ma", reuse_loaded=True)

"""
tests/test_statements_to_kg.py::Test_02_FeatureRequest::test_c01__render_order_ring_problem
"""

TEST_URI = "irk://stafo/unittest"

def create_key_tuple(number):
    item_keys = [f"I{i}" for i in range(2000 + number - 1, 2000 - 1, -1)]
    relation_keys = [f"R{i}" for i in range(2000 + number - 1, 2000 - 1, -1)]
    return (item_keys, relation_keys)


class HousekeeperMixin(GeneralHousekeeperMixin):
    pass


class Test_00_Core(unittest.TestCase):

    def setUp(self) -> None:
        return super().setUp()

    def test_a01__base(self):
        # do the conversion
        res_mod_fpath = s2k.main(TEST_DATA1_FPATH)

        # ensure that the result can be loaded without errors

        mod = p.irkloader.load_mod_from_path(res_mod_fpath, prefix="tst")

    # test_r stands for render :)
    def test_r01__render_order_ring_problem(self):
        res_mod_fpath = s2k.main(TEST_DATA2_FPATH, create_key_tuple(40))
        # ensure that the result can be loaded without errors
        mod = p.irkloader.load_mod_from_path(res_mod_fpath, prefix="tst")
        self.assertEqual(
            mod.I2003.get_relations()["irk:/ocse/0.2/auto_import_statements02_ring#R2000"][0]
            .object.get_relations()["irk:/ocse/0.2/auto_import_statements02_ring#R2000"][0]
            .object,
            mod.I2003,
        )

    def test_r02__render_latex_equations(self):
        res_mod_fpath = s2k.main(TEST_DATA3_FPATH, create_key_tuple(50))
        with open(res_mod_fpath, "rt") as f:
            res = f.read()
        int_res_pattern = r"""cm1.new_math_relation\(lhs=cm1.F\(I\d+\["s"\]\), rsgn="==", rhs=ma.I5443\["definite integral"\]\(\(\(I\d+\["e"\]\*\*\(-1\*I\d+\["s"\]\*I\d+\["t"\]\)\)\*cm1.f\(I\d+\["t"\]\)\), I\d+\["t"\], ma.I5440\["limits"\]\(ma.I5000\["scalar zero"\], ma.I4291\["infinity"\]\)\)"""
        deriv_res = """cm1.new_math_relation(lhs=cm1.y(cm1.x), rsgn="==", rhs=ma.derivative(cm1.f(cm1.x), cm1.x, ma.I5001["scalar one"])"""
        int_res = re.findall(int_res_pattern, res)
        self.assertEqual(len(int_res), 1)
        self.assertIn(deriv_res, res)

    def test_m01__match_entities(self):
        res_mod_fpath = s2k.main(TEST_DATA4_FPATH, create_key_tuple(20))
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
        res_mod_fpath = s2k.main(TEST_DATA5_FPATH, create_key_tuple(20))
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


class Test_01_Bugs(HousekeeperMixin, unittest.TestCase):
    """
    These tests specifically trigger bugs (or test former bugs)
    """

    def test_b01__R77_list_problem(self):
        with p.uri_context(uri=self.TEST_BASE_URI, prefix="ut"):
            I1000 = p.create_item(
                R1__has_label="test item",
                R4__is_instance_of=p.I35["real number"],
                R77__has_alternative_label=["test1", "test2"],
            )
