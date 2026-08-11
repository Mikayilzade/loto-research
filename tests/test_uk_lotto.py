import math
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from loto_research.uk_lotto import (  # noqa: E402
    TOTAL_COMBINATIONS,
    estimate_entries_from_winner_count,
    lotto_probabilities,
    must_be_won_break_even_jackpot,
    ordinary_fixed_cash_ev,
    published_rolldown_schedule_cash_ev,
)


class UKLottoTests(unittest.TestCase):
    def test_total_combinations(self):
        self.assertEqual(TOTAL_COMBINATIONS, 45_057_474)

    def test_official_jackpot_denominator(self):
        self.assertAlmostEqual(lotto_probabilities()["match6"], 1 / 45_057_474)

    def test_fixed_cash_ev(self):
        self.assertAlmostEqual(ordinary_fixed_cash_ev(), 0.5214539989525377, places=14)

    def test_july_2025_match2_sales_estimate(self):
        estimated = estimate_entries_from_winner_count(1_522_131, "match2")
        self.assertAlmostEqual(estimated, 15_614_190.035480577, places=6)

    def test_july_2025_cash_only_break_even_jackpot(self):
        entries = estimate_entries_from_winner_count(1_522_131, "match2")
        threshold = must_be_won_break_even_jackpot(entries, lucky_dip_value=0)
        self.assertAlmostEqual(threshold, 23_086_298.23655494, places=6)

    def test_july_2025_published_rolldown_schedule_is_negative_cash_ev(self):
        ev = published_rolldown_schedule_cash_ev(
            {
                "match5_bonus": 1_036_946,
                "match5": 4_446,
                "match4": 206,
                "match3": 66,
                "match2_cash": 5,
            }
        )
        self.assertAlmostEqual(ev, 1.4370766323917756, places=14)
        self.assertLess(ev, 2.0)


if __name__ == "__main__":
    unittest.main()
