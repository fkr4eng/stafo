import os
import tempfile
import unittest

import pytest
import yaml

import pyirk as p

from stafo import statement_to_kg as s2k
from stafo.sparql_agent import SparqlAgent
from stafo.utils import TESTA_DATA_DIR

from ipydex import activate_ips_on_exception

activate_ips_on_exception()

EVAL_KB_FPATH = os.path.join(TESTA_DATA_DIR, "eval_knowledge_base.md")
EVAL_QUESTIONS_FPATH = os.path.join(TESTA_DATA_DIR, "eval_questions.yaml")


@pytest.mark.slow
class Test_SparqlAgent(unittest.TestCase):
    """
    Integration tests for SparqlAgent. Require a running Ollama instance.
    Run with: pytest -m slow
    """

    @classmethod
    def setUpClass(cls):
        cls._tmpdir = tempfile.TemporaryDirectory()
        embedding_csv_path = os.path.join(cls._tmpdir.name, "test_embeddings.csv")

        CM = s2k.ConversionManager(EVAL_KB_FPATH, num_keys=50)
        cls.mod_fpath = CM.run()
        nl_load_dict = {"path": cls.mod_fpath, "prefix": "ut", "module_name": "ut"}

        cls.sa = SparqlAgent([nl_load_dict], embedding_csv_path=embedding_csv_path)
        cls.sa.setup_embeddings()

        with open(EVAL_QUESTIONS_FPATH, "r", encoding="utf-8") as f:
            cls.questions = yaml.safe_load(f)

    @classmethod
    def tearDownClass(cls):
        cls._tmpdir.cleanup()

    @staticmethod
    def _normalize(text: str) -> str:
        return text.lower().replace("‑", "-").replace("‒", "-").replace("–", "-")

    def _check_question(self, idx):
        q = self.questions[idx]
        question = q["question"]
        expected_labels = q["expected_labels"]
        text_answer = self.sa.run_all_at_once(question)
        normalized = self._normalize(text_answer)
        for label in expected_labels:
            self.assertIn(
                self._normalize(label),
                normalized,
                f"Expected '{label}' in answer to: '{question}'\nGot: {text_answer}",
            )

    def test_q01__result_type_of_gradient(self):
        self._check_question(0)

    def test_q02__operators_taking_scalar_field(self):
        self._check_question(1)

    def test_q03__subclass_of_function(self):
        self._check_question(2)

    def test_q04__has_jacobian_matrix_relation(self):
        self._check_question(3)

    def test_q05__real_vector_space_hierarchy(self):
        self._check_question(4)
