import unittest

from loto_research.lucky_contestant_time_state import (
    OFFICIAL_TIME_BINS,
    equivalent_one_in,
    hidden_time_alone_can_guarantee_profit,
    jackpot_only_break_even_probability,
    optimistic_truncated_next_window_probability,
    prior_mass,
    validate_prior,
)


class LuckyContestantTimeStateTests(unittest.TestCase):
    def test_official_prior_sums_to_one_and_is_contiguous(self):
        validate_prior()
        self.assertAlmostEqual(sum(b.probability for b in OFFICIAL_TIME_BINS), 1.0)

    def test_published_block_masses(self):
        self.assertAlmostEqual(prior_mass(60, 120), 0.10)
        self.assertAlmostEqual(prior_mass(1320, 1425), 0.15)

    def test_optimistic_late_survival_concentrates_target(self):
        # Under the explicit uniform-within-bin + T>=now information bound,
        # after 23:00 all remaining selected-time mass lies within 60 minutes.
        self.assertAlmostEqual(
            optimistic_truncated_next_window_probability(1380, 60), 1.0
        )
        self.assertAlmostEqual(
            optimistic_truncated_next_window_probability(1380, 30), 2 / 3
        )

    def test_minimum_stake_jackpot_only_threshold(self):
        p = jackpot_only_break_even_probability(0.20, 600.0)
        self.assertAlmostEqual(p, 1 / 3000)
        self.assertAlmostEqual(equivalent_one_in(p), 3000.0)

    def test_hidden_time_mechanism_is_not_terminal_guarantee(self):
        self.assertFalse(
            hidden_time_alone_can_guarantee_profit(
                positive_stake=True,
                target_time_hidden=True,
                jackpot_can_be_won_earlier_by_others=True,
                losing_nonjackpot_outcome_exists=True,
            )
        )


if __name__ == "__main__":
    unittest.main()
