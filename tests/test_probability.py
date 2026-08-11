import math
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from loto_research.probability import (  # noqa: E402
    expected_jackpot_share_fraction,
    four_plus_four_any_prize_probability,
    four_plus_four_category_probabilities,
    jackpot_denominator_two_pool,
    multi_pool_match_probability,
    single_pool_match_probability,
)


class ProbabilityTests(unittest.TestCase):
    def test_besde5_match_distribution_sums_to_one(self):
        total = sum(
            single_pool_match_probability(36, 5, 5, matches)
            for matches in range(6)
        )
        self.assertAlmostEqual(total, 1.0, places=14)

    def test_super_keno_match_distribution_sums_to_one(self):
        total = sum(
            single_pool_match_probability(70, 10, 20, matches)
            for matches in range(11)
        )
        self.assertAlmostEqual(total, 1.0, places=14)

    def test_powerball_exact_jackpot_denominator(self):
        self.assertEqual(
            jackpot_denominator_two_pool(69, 5, 26, 1),
            292_201_338,
        )

    def test_mega_millions_exact_jackpot_denominator(self):
        self.assertEqual(
            jackpot_denominator_two_pool(70, 5, 24, 1),
            290_472_336,
        )

    def test_four_plus_four_jackpot_probability(self):
        actual = multi_pool_match_probability(
            [
                (20, 4, 4, 4),
                (20, 4, 4, 4),
            ]
        )
        expected = 1.0 / (math.comb(20, 4) ** 2)
        self.assertAlmostEqual(actual, expected, places=18)
        self.assertEqual(math.comb(20, 4) ** 2, 23_474_025)

    def test_four_plus_four_category_one_is_jackpot(self):
        categories = four_plus_four_category_probabilities()
        self.assertAlmostEqual(
            categories["I"],
            1.0 / 23_474_025,
            places=18,
        )

    def test_four_plus_four_any_prize_probability(self):
        self.assertAlmostEqual(
            four_plus_four_any_prize_probability(),
            0.186147241472223,
            places=15,
        )

    def test_four_plus_four_categories_are_mutually_exclusive(self):
        categories = four_plus_four_category_probabilities()
        # Winning states are exactly the 11 public match groups; the remainder
        # of the A/B match-state grid is losing.
        self.assertEqual(len(categories), 11)
        self.assertGreater(sum(categories.values()), 0.0)
        self.assertLess(sum(categories.values()), 1.0)

    def test_expected_share_with_no_other_tickets(self):
        self.assertEqual(expected_jackpot_share_fraction(0, 0.5), 1.0)

    def test_expected_share_when_every_other_ticket_wins(self):
        self.assertAlmostEqual(
            expected_jackpot_share_fraction(4, 1.0),
            0.2,
            places=15,
        )

    def test_expected_share_closed_form_matches_manual_small_case(self):
        # Three other tickets, each independently has 25% jackpot probability.
        # Compare the closed form with direct binomial enumeration.
        n = 3
        q = 0.25
        manual = 0.0
        for other_winners in range(n + 1):
            probability = (
                math.comb(n, other_winners)
                * (q ** other_winners)
                * ((1.0 - q) ** (n - other_winners))
            )
            manual += probability / (1 + other_winners)

        self.assertAlmostEqual(
            expected_jackpot_share_fraction(n, q),
            manual,
            places=15,
        )


if __name__ == "__main__":
    unittest.main()
