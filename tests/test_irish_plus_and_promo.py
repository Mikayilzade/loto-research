import unittest

from loto_research.irish_plus_and_promo import (
    capped_bonus_effective_rebate,
    euromillions_plus_full_coverage,
    full_coverage_six_plus_bonus,
    six_of_n_with_bonus_match_counts,
)


class IrishPlusAndPromoTests(unittest.TestCase):
    def test_six_of_39_partition(self):
        counts = six_of_n_with_bonus_match_counts(39)
        self.assertEqual(sum(counts.values()), 3_262_623)
        self.assertEqual(counts[(6, 0)], 1)
        self.assertEqual(counts[(5, 1)], 6)
        self.assertEqual(counts[(5, 0)], 192)
        self.assertEqual(counts[(4, 1)], 480)
        self.assertEqual(counts[(3, 0)], 99_200)

    def test_daily_million_identity_reproduces_existing_h024(self):
        result = full_coverage_six_plus_bonus(
            39,
            1.0,
            {
                (6, 0): 1_000_000,
                (5, 1): 10_000,
                (5, 0): 500,
                (4, 1): 100,
                (4, 0): 25,
                (3, 1): 10,
                (3, 0): 3,
            },
            shareable_top_prize=1_000_000,
        )
        self.assertEqual(result.combinations, 3_262_623)
        self.assertEqual(result.optimistic_gross, 1_786_800)
        self.assertAlmostEqual(result.optimistic_return, 0.547657513601786, places=12)

    def test_daily_million_plus_full_cover_is_far_below_cost(self):
        result = full_coverage_six_plus_bonus(
            39,
            1.0,
            {
                (6, 0): 500_000,
                (5, 1): 5_000,
                (5, 0): 250,
                (4, 1): 50,
                (4, 0): 15,
                (3, 1): 5,
                (3, 0): 2,
            },
            shareable_top_prize=500_000,
        )
        self.assertEqual(result.optimistic_gross, 961_600)
        self.assertAlmostEqual(result.optimistic_return, 0.294732183277075, places=12)
        self.assertAlmostEqual(result.strict_cash_return, 0.141481256032340, places=12)

    def test_euromillions_plus_full_cover_is_negative(self):
        result = euromillions_plus_full_coverage()
        self.assertEqual(result.combinations, 2_118_760)
        self.assertEqual(result.optimistic_gross, 1_148_000)
        self.assertEqual(result.strict_cash_floor, 648_000)
        self.assertAlmostEqual(result.optimistic_return, 0.541826351262059, places=12)
        self.assertAlmostEqual(result.strict_cash_return, 0.305839264475448, places=12)

    def test_olg_bogo_face_value_rebate_is_capped_one_for_one(self):
        self.assertEqual(capped_bonus_effective_rebate(6, 6), 1.0)
        self.assertEqual(capped_bonus_effective_rebate(3, 3), 1.0)
        self.assertAlmostEqual(capped_bonus_effective_rebate(18, 6), 1 / 3)


if __name__ == "__main__":
    unittest.main()
