"""
Test for the FNL-compression / glossary feature (`core.digest_prior_fnl`).

`digest_prior_fnl` replaces the full accumulated FNL (Input Part 4 of prompt01) with
a compact digest: a glossary of every concept defined so far + the last few snippet
blocks. These tests assert the properties that make that substitution safe:
  * every defined concept (class/property/relation/operator) survives in the glossary,
    including concepts whose snippet block has fallen out of the recent window
    (so entity names can still be reused);
  * non-definition statement types (example, if-then, ...) are not treated as concepts;
  * concept labels are kept;
  * only the last N snippet blocks are shown verbatim;
  * on a large input the digest is a small fraction of the original size.
"""

import os
import unittest

from stafo.core import digest_prior_fnl
from stafo.utils import TESTA_DATA_DIR

# small hand-written FNL over four snippets; concepts are defined in the *early*
# snippets on purpose, so we can check they survive after those blocks drop out.
FIXTURE_FPATH = os.path.join(TESTA_DATA_DIR, "statements17_fnl_digest.md")

with open(FIXTURE_FPATH, "rt", encoding="utf-8") as _fp:
    FIXTURE = _fp.read()


class TestFnlDigest(unittest.TestCase):

    def _split(self, digest):
        """return (glossary_part, recent_blocks_part)"""
        glossary, recent = digest.split("## Most recent")
        return glossary, recent

    def test_glossary_contains_every_defined_concept(self):
        glossary, _ = self._split(digest_prior_fnl(FIXTURE, num_recent_blocks=2))
        for name in ["'set'", "'is subset of'", "'open'", "'union op'", "'closure op'"]:
            self.assertIn(name, glossary, f"{name} missing from glossary")

    def test_old_concept_survives_when_its_block_drops_out(self):
        # keeping only the last 2 blocks drops snippet(1)/(2) from the verbatim section,
        # but their concepts must remain reusable via the glossary.
        glossary, recent = self._split(digest_prior_fnl(FIXTURE, num_recent_blocks=2))
        self.assertIn("'set'", glossary)              # defined in snippet(1)
        self.assertNotIn("- // snippet(1)", recent)   # its block is gone
        self.assertNotIn("- // snippet(2)", recent)
        self.assertIn("- // snippet(3)", recent)      # only the recent blocks remain
        self.assertIn("- // snippet(4)", recent)

    def test_glossary_preserves_labels(self):
        glossary, _ = self._split(digest_prior_fnl(FIXTURE, num_recent_blocks=2))
        self.assertIn("'set' has the alternative german label 'Menge'", glossary)
        self.assertIn("'union op' has the alternative german label 'Vereinigung'", glossary)

    def test_non_definition_statements_excluded_from_glossary(self):
        glossary, _ = self._split(digest_prior_fnl(FIXTURE, num_recent_blocks=2))
        self.assertNotIn("There is an example", glossary)
        self.assertNotIn("There is an if-then-statement", glossary)
        self.assertNotIn("some named theorem", glossary)
        self.assertNotIn("empty set is a subset", glossary)  # example prose must not leak

    def test_num_recent_blocks_zero_keeps_glossary_only(self):
        glossary, recent = self._split(digest_prior_fnl(FIXTURE, num_recent_blocks=0))
        self.assertIn("'closure op'", glossary)     # every concept still present
        self.assertNotIn("- // snippet(", recent)   # no verbatim blocks

    def test_digest_much_smaller_on_large_input(self):
        # 60 snippets, each defining one class + 20 filler lines
        blocks = []
        for k in range(1, 61):
            lines = [f"- // snippet({k})", f"- There is a class: 'concept_{k}' @en"]
            lines += [f"    - 'concept_{k}' has the property 'filler_{j}'" for j in range(20)]
            blocks.append("\n".join(lines))
        big_fnl = "\n".join(blocks)

        digest = digest_prior_fnl(big_fnl, num_recent_blocks=3)

        self.assertLess(len(digest), 0.3 * len(big_fnl))      # bounded
        self.assertIn("'concept_1'", digest)                  # earliest concept retained
        self.assertIn("'concept_60'", digest)                 # newest retained
        _, recent = self._split(digest)
        self.assertIn("- // snippet(60)", recent)             # only last 3 blocks verbatim
        self.assertNotIn("- // snippet(1)\n", recent)


if __name__ == "__main__":
    unittest.main()
