import unittest

from loto_research.lotto_plus_raffle import (
    break_even_total_plus_lines,
    fixed_plus_ev,
    incremental_plus_ev,
    strict_guarantee_possible_with_external_entries,
)


class LottoPlusRaffleTests(unittest.TestCase):
    def test_fixed_plus_ev(self):
        self.assertAlmostEqual(fixed_plus_ev(), 0.41166459590076826, places=12)

    def test_break_even_entry_threshold(self):
        self.assertAlmostEqual(
            break_even_total_plus_lines(), 1_699_710.7313829695, places=6
        )

    def test_typical_winner_count_band_implies_positive_incremental_ev(self):
        # 60-120 ordinary raffle winners corresponds heuristically to
        # ~600k-1.2m eligible lines because each line wins the 1/10,000 raffle.
        self.assertGreater(incremental_plus_ev(1_200_000), 1.0)
        self.assertGreater(incremental_plus_ev(600_000), 1.0)

    def test_external_entries_destroy_strict_million_guarantee(self):
        self.assertFalse(strict_guarantee_possible_with_external_entries())


if __name__ == "__main__":
    unittest.main()
