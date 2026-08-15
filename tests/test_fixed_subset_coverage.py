import unittest

from loto_research.fixed_subset_coverage import fixed_subset_full_coverage


class FixedSubsetCoverageTests(unittest.TestCase):
    def test_current_irish_54321_six_number_k5(self):
        r = fixed_subset_full_coverage(47, 6, 5, 1.0, 125_000.0)
        self.assertEqual(r.variants, 1_533_939)
        self.assertEqual(r.winning_variants, 6)
        self.assertEqual(r.gross, 750_000.0)
        self.assertAlmostEqual(r.return_ratio, 0.4889373045473125, places=15)

    def test_current_irish_54321_best_case_is_below_one(self):
        payouts6 = {1: 6, 2: 45, 3: 550, 4: 6000, 5: 125000}
        payouts7 = {1: 5, 2: 32, 3: 275, 4: 3000, 5: 40000}
        ratios = []
        for k, payout in payouts6.items():
            ratios.append(fixed_subset_full_coverage(47, 6, k, 1.0, payout).return_ratio)
        for k, payout in payouts7.items():
            ratios.append(fixed_subset_full_coverage(47, 7, k, 1.0, payout).return_ratio)
        self.assertAlmostEqual(max(ratios), 36/47, places=15)
        self.assertLess(max(ratios), 1.0)

    def test_announced_45_ball_sensitivity_still_below_one(self):
        payouts6 = {1: 6, 2: 45, 3: 550, 4: 6000, 5: 125000}
        payouts7 = {1: 5, 2: 32, 3: 275, 4: 3000, 5: 40000}
        ratios = []
        for k, payout in payouts6.items():
            ratios.append(fixed_subset_full_coverage(45, 6, k, 1.0, payout).return_ratio)
        for k, payout in payouts7.items():
            ratios.append(fixed_subset_full_coverage(45, 7, k, 1.0, payout).return_ratio)
        self.assertAlmostEqual(max(ratios), 0.8, places=15)
        self.assertLess(max(ratios), 1.0)


if __name__ == "__main__":
    unittest.main()
