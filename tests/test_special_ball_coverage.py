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


if __name__ == "__main__":
    unittest.main()
