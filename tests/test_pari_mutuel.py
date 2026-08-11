import math
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from loto_research.pari_mutuel import (  # noqa: E402
    expected_shared_pool_payout,
    expected_shared_pool_payout_closed_form,
    zero_winner_probability,
)


class PariMutuelTests(unittest.TestCase):
    def test_closed_form_matches_share_form(self):
        p = 0.02
        n = 20
        pool = 1000.0
        direct = expected_shared_pool_payout(
            category_probability=p,
            pool_value=pool,
            other_entries=n - 1,
        )
        closed = expected_shared_pool_payout_closed_form(
            category_probability=p,
            pool_value=pool,
            total_entries_including_us=n,
        )
        self.assertAlmostEqual(direct, closed, places=14)

    def test_zero_winner_probability(self):
        self.assertAlmostEqual(
            zero_winner_probability(0.1, 3),
            0.9 ** 3,
            places=15,
        )

    def test_kz_1546_screen(self):
        # Exact 4/20 grouped probabilities, derived analytically.
        probabilities = {
            1: 0.000000042600278393,
            2: 0.000005452835634281,
            3: 0.000061344400885660,
            4: 0.000190849247199830,
            5: 0.000155065013349862,
            6: 0.000174490740296988,
            7: 0.003926041656682226,
            8: 0.012214351820789148,
            9: 0.009924160854391182,
            10: 0.022083984318837523,
            11: 0.137411457983877900,
            12: 0.111646809611900810,
        }
        weights = {
            2: 0.02,
            3: 0.02,
            4: 0.03,
            5: 0.02,
            6: 0.02,
            7: 0.02,
            8: 0.06,
            9: 0.04,
            10: 0.06,
            11: 0.145,
            12: 0.115,
        }
        n = 14_742
        unit_price = 300.0
        lower = 0.0
        for category, weight in weights.items():
            pool = weight * unit_price * n
            lower += expected_shared_pool_payout_closed_form(
                probabilities[category], pool, n
            )

        jackpot = expected_shared_pool_payout_closed_form(
            probabilities[1], 227_247_957.0, n
        )

        self.assertAlmostEqual(lower, 155.42686229970462, places=9)
        self.assertAlmostEqual(jackpot, 9.67778723614877, places=9)
        self.assertAlmostEqual(lower + jackpot, 165.10464953585338, places=9)
        self.assertLess(lower + jackpot, unit_price)

    def test_kz_1545_to_1546_transition_closes_exactly(self):
        old_superprize = 226_866_699
        unpaid = 99_432 + 149_148
        current_contribution = 14_742 * 300 * 0.03
        new_superprize = old_superprize + unpaid + current_contribution
        self.assertEqual(new_superprize, 227_247_957)


if __name__ == "__main__":
    unittest.main()
