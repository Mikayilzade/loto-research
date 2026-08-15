import unittest

from loto_research.megamillions_threshold import (
    COMBINATIONS,
    cash_break_even,
    expected_multiplier,
    full_space_guarantee_floor_before_sharing,
    lower_tier_expected_value,
)


class MegaMillionsThresholdTests(unittest.TestCase):
    def test_combination_space(self):
        self.assertEqual(COMBINATIONS, 290_472_336)

    def test_expected_multiplier_is_three(self):
        self.assertAlmostEqual(expected_multiplier(), 3.0, places=12)

    def test_lower_tier_ev(self):
        self.assertAlmostEqual(lower_tier_expected_value(), 1.1184749104644511, places=12)

    def test_optimistic_no_sharing_cash_break_even(self):
        self.assertAlmostEqual(cash_break_even(), 1_127_475_660.0, places=6)

    def test_full_space_worst_multiplier_floor(self):
        cost, lower_floor, sole_jackpot_needed = full_space_guarantee_floor_before_sharing()
        self.assertEqual(cost, 1_452_361_680.0)
        self.assertAlmostEqual(lower_floor, 216_590_680.0, places=6)
        self.assertAlmostEqual(sole_jackpot_needed, 1_235_771_000.0, places=6)


if __name__ == '__main__':
    unittest.main()
