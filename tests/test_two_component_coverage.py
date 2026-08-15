import unittest

from loto_research.two_component_coverage import fixed_bonus_full_coverage


class TwoComponentCoverageTests(unittest.TestCase):
    def test_set_for_life_full_space_nominal(self):
        result = fixed_bonus_full_coverage(
            main_pool=47,
            main_picks=5,
            bonus_pool=10,
            stake=1.50,
            payout_if_bonus={5: 3_600_000, 4: 250, 3: 30, 2: 10},
            payout_if_not_bonus={5: 120_000, 4: 50, 3: 20, 2: 5},
        )
        self.assertEqual(result.entries, 15_339_390)
        self.assertEqual(result.cost, 23_009_085.0)
        self.assertEqual(result.gross, 12_949_100.0)
        self.assertAlmostEqual(result.return_ratio, 12_949_100 / 23_009_085, places=12)
        self.assertEqual(result.net, -10_059_985.0)

    def test_thunderball_full_space(self):
        result = fixed_bonus_full_coverage(
            main_pool=39,
            main_picks=5,
            bonus_pool=14,
            stake=1.0,
            payout_if_bonus={5: 500_000, 4: 250, 3: 20, 2: 10, 1: 5, 0: 3},
            payout_if_not_bonus={5: 5_000, 4: 100, 3: 10},
        )
        self.assertEqual(result.entries, 8_060_598)
        self.assertEqual(result.cost, 8_060_598.0)
        self.assertEqual(result.gross, 4_262_568.0)
        self.assertAlmostEqual(result.return_ratio, 4_262_568 / 8_060_598, places=12)
        self.assertEqual(result.net, -3_798_030.0)


if __name__ == "__main__":
    unittest.main()
