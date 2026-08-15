import unittest

from loto_research.euromillions_coverage import (
    category_count,
    euromillions_space,
    full_space_cost,
    full_coverage_forces_jackpot_winner,
    terminal_cap_rolldown_compatible_with_full_coverage,
)


class EuroMillionsCoverageTests(unittest.TestCase):
    def test_space_and_cost(self):
        self.assertEqual(euromillions_space(), 139_838_160)
        self.assertEqual(full_space_cost(), 349_595_400.0)

    def test_key_category_counts(self):
        self.assertEqual(category_count(5, 2), 1)
        self.assertEqual(category_count(5, 1), 20)
        self.assertEqual(category_count(5, 0), 45)
        self.assertEqual(category_count(4, 2), 225)
        self.assertEqual(category_count(2, 0), 6_385_500)

    def test_complete_space_forces_jackpot_and_blocks_rolldown(self):
        self.assertTrue(full_coverage_forces_jackpot_winner())
        self.assertFalse(terminal_cap_rolldown_compatible_with_full_coverage())


if __name__ == "__main__":
    unittest.main()
