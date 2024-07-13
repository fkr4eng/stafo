import unittest
import sys
import os
from os.path import join as pjoin
from typing import Dict, List, Union
from packaging import version

from stafo import statement_to_kg as s2k
from stafo.utils import TESTA_DATA_DIR

from ipydex import IPS, activate_ips_on_exception

activate_ips_on_exception()

TEST_DATA1_FPATH = os.path.join(TESTA_DATA_DIR, "statements01.md")

class Test_00_Core(unittest.TestCase):

    def setUp(self) -> None:
        return super().setUp()

    def test_01__base(self):
        # just test basic call
        s2k.main(TEST_DATA1_FPATH)
