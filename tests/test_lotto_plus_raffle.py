import unittest

from loto_research.lotto_plus_raffle import (
    break_even_total_plus_lines,
    event_count_posterior,
    fixed_plus_ev,
    incremental_plus_ev,
    mean_promotion_uplift,
    posterior_mean_raffle_winners,
    posterior_predictive_tail_probability,
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
        self.assertGreater(incremental_plus_ev(1_200_000), 1.0)
        self.assertGreater(incremental_plus_ev(600_000), 1.0)

    def test_six_event_posterior(self):
        counts = [73, 104, 81, 82, 84, 72]
        shape, rate = event_count_posterior(counts)
        self.assertEqual(shape, 496.5)
        self.assertEqual(rate, 6.0)
        self.assertAlmostEqual(posterior_mean_raffle_winners(counts), 82.75, places=12)
        self.assertLess(posterior_predictive_tail_probability(counts, 170), 1e-10)

    def test_matched_adjacent_draw_uplift(self):
        events = [73, 104, 81, 82, 84, 72]
        before = [55, 69, 56, 62, 59, 48]
        after = [51, 76, 54, 81, 62, 52]
        self.assertAlmostEqual(
            mean_promotion_uplift(events, before, after),
            1.3766419034722104,
            places=12,
        )

    def test_external_entries_destroy_strict_million_guarantee(self):
        self.assertFalse(strict_guarantee_possible_with_external_entries())


if __name__ == "__main__":
    unittest.main()
