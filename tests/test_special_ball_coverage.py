import unittest

from loto_research.special_ball_coverage import (
    special_ball_full_coverage_counts,
    special_ball_full_coverage_value,
)


class SpecialBallCoverageTests(unittest.TestCase):
    def test_counts_partition_full_space(self):
        counts = special_ball_full_coverage_counts(58, 5, 5)
        self.assertEqual(sum(counts.values()), 22_910_580)
        self.assertEqual(counts[(5, True)], 1)
        self.assertEqual(counts[(5, False)], 4)
        self.assertEqual(counts[(4, True)], 265)
        self.assertEqual(counts[(4, False)], 1_060)

    def test_millionaire_for_life_optimistic_full_space_is_loss(self):
        payouts = {
            (5, True): 18_000_000,
            (5, False): 2_200_000,
            (4, True): 7_500,
            (4, False): 500,
            (3, True): 250,
            (3, False): 50,
            (2, True): 25,
            (2, False): 8,
            (1, True): 8,
        }
        lines, cost, gross, ratio = special_ball_full_coverage_value(
            58, 5, 5, 5.0, payouts
        )
        self.assertEqual(lines, 22_910_580)
        self.assertEqual(cost, 114_552_900.0)
        self.assertEqual(gross, 60_584_320.0)
        self.assertAlmostEqual(ratio, 0.5288763531957724, places=15)
        self.assertLess(ratio, 1.0)

    def test_lotto_america_nonjackpot_full_space_floor(self):
        payouts = {
            (5, False): 20_000,
            (4, True): 1_000,
            (4, False): 100,
            (3, True): 20,
            (3, False): 5,
            (2, True): 5,
            (1, True): 2,
            (0, True): 2,
        }
        lines, cost, gross, ratio = special_ball_full_coverage_value(
            52, 5, 10, 1.0, payouts
        )
        self.assertEqual(lines, 25_989_600)
        self.assertEqual(cost, 25_989_600.0)
        self.assertEqual(gross, 6_991_428.0)
        self.assertAlmostEqual(ratio, 0.269008680395235, places=15)
        self.assertEqual(cost - gross, 18_998_172.0)

    def test_lotto_america_july_2026_cash_state_still_below_full_space_cost(self):
        nonjackpot_gross = 6_991_428.0
        cash_jackpot = 15_154_248.0
        cost = 25_989_600.0
        total = nonjackpot_gross + cash_jackpot
        self.assertEqual(total, 22_145_676.0)
        self.assertAlmostEqual(total / cost, 0.8520976082740789, places=15)
        self.assertEqual(cost - total, 3_843_924.0)


if __name__ == "__main__":
    unittest.main()
