import unittest

from loto_research.nz_bullseye import (
    full_space_coverage,
    strict_cash_guarantee_possible_with_unbounded_external_duplicates,
    winning_counts_per_full_space_draw,
)


class NZBullseyeTests(unittest.TestCase):
    def test_full_space_partition(self):
        counts = winning_counts_per_full_space_draw()
        self.assertEqual(counts, {1: 1, 2: 10, 3: 90, 4: 900, 5: 9_000, 6: 90_000})
        self.assertEqual(sum(counts.values()), 100_001)

    def test_seven_draw_discount(self):
        x = full_space_coverage(7)
        self.assertEqual(x.cost_nzd, 10_000_000.0)
        self.assertEqual(x.standard_cost_nzd, 14_000_000.0)
        self.assertAlmostEqual(x.discount_fraction, 2 / 7, places=12)

    def test_fourteen_draw_discount(self):
        x = full_space_coverage(14)
        self.assertEqual(x.cost_nzd, 20_000_000.0)
        self.assertEqual(x.standard_cost_nzd, 28_000_000.0)
        self.assertAlmostEqual(x.discount_fraction, 2 / 7, places=12)

    def test_no_strict_cash_guarantee_under_unbounded_duplication(self):
        self.assertFalse(strict_cash_guarantee_possible_with_unbounded_external_duplicates())


if __name__ == "__main__":
    unittest.main()
