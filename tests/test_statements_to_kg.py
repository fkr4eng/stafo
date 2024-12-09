import unittest
import sys
import os
from os.path import join as pjoin
from typing import Dict, List, Union
from packaging import version
import pyirk as p
from pyirk.utils import GeneralHousekeeperMixin

from stafo import statement_to_kg as s2k
from stafo.utils import TESTA_DATA_DIR

from ipydex import IPS, activate_ips_on_exception

activate_ips_on_exception()

TEST_DATA1_FPATH = os.path.join(TESTA_DATA_DIR, "statements01.md")


class HousekeeperMixin(GeneralHousekeeperMixin):
    pass


class Test_00_Core(unittest.TestCase):

    def setUp(self) -> None:
        return super().setUp()

    def test_01__base(self):
        # do the conversion
        res_mod_fpath = s2k.main(TEST_DATA1_FPATH)

        # ensure that the result can be loaded without errors

        # TODO JF (should be easy):
        # currently this fails
        # a) because of hardcoded IPS()
        # b) due to "PyIRKError: The module irk:/ocse/0.2/auto_import_statements01
        # was not properly ended. Ensure that pyirk.end_mod() is called after the last PyIRK-statement."
        mod = p.irkloader.load_mod_from_path(res_mod_fpath, prefix="tst")


class Test_01_Bugs(HousekeeperMixin, unittest.TestCase):
    """
    These tests specifically trigger bugs (or test former bugs)
    """

    def test_b01__R77_list_problem(self):
        with p.uri_context(uri=self.TEST_BASE_URI, prefix="ut"):
            I1000 = p.create_item(
                R1__has_label="test item",
                R4__is_instance_of=p.I35["real number"],
                R77__has_alternative_label=["test1", "test2"]
            )
