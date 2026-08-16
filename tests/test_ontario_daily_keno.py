import unittest

from loto_research.ontario_daily_keno import (
    PAYOUTS_BY_PICK,
    additive_portfolio_guarantee_impossible,
    exact_match_count_full_coverage,
    uncapped_full_coverage,
)


class OntarioDailyKenoTests(unittest.TestCase):
    def test_pick2_full_coverage(self):
        variants, cost, gross, roi = uncapped_full_coverage(2)
        self.assertEqual(variants, 2_415)
        self.assertEqual(cost, 2_415.0)
        self.assertEqual(exact_match_count_full_coverage(2, 2), 190)
        self.assertEqual(gross, 1_330.0)
        self.assertAlmostEqual(roi, 1330 / 2415, places=12)

    def test_pick10_zero_match_count(self):
        self.assertEqual(
            exact_match_count_full_coverage(10, 0),
            10_272_278_170,
        )

    def test_all_pick_categories_are_negative_before_cap(self):
        ratios = [uncapped_full_coverage(pick)[3] for pick in PAYOUTS_BY_PICK]
        self.assertLess(max(ratios), 0.551)
        self.assertGreater(min(ratios), 0.42)

    def test_any_nonnegative_mix_is_rejected_by_expectation(self):
        self.assertTrue(
            additive_portfolio_guarantee_impossible(
                {pick: 1.0 for pick in PAYOUTS_BY_PICK}
            )
        )


if __name__ == "__main__":
    unittest.main()
