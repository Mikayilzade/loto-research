import unittest

from loto_research.capped_competition import CappedCompetition


class CappedCompetitionTests(unittest.TestCase):
    def test_external_entry_kills_exclusivity(self):
        c = CappedCompetition(100, 1.0, 150.0, external_entries=1)
        self.assertFalse(c.exclusivity_possible())
        self.assertFalse(c.passes_basic_guarantee_filter())

    def test_personal_cap_kills_exclusivity(self):
        c = CappedCompetition(100, 1.0, 150.0, per_person_cap=99)
        self.assertFalse(c.exclusivity_possible())

    def test_negative_takeover_economics_fail(self):
        c = CappedCompetition(300, 1.99, 280.0)
        self.assertAlmostEqual(c.full_takeover_cost, 597.0)
        self.assertFalse(c.positive_full_takeover_economics())
        self.assertFalse(c.passes_basic_guarantee_filter())

    def test_hypothetical_positive_instance_passes_only_basic_filter(self):
        c = CappedCompetition(100, 1.0, 120.0)
        self.assertTrue(c.exclusivity_possible())
        self.assertTrue(c.positive_full_takeover_economics())
        self.assertTrue(c.passes_basic_guarantee_filter())


if __name__ == "__main__":
    unittest.main()
