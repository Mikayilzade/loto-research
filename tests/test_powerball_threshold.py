import unittest

from loto_research.powerball_threshold import (
    COMBINATION_SPACE,
    expected_jackpot_share,
    full_space_required_jackpot_with_external_winner_cap,
    full_space_required_jackpot_without_external_sharing,
    required_cash_jackpot,
)


LOWER_EV = 0.31987825


class PowerballThresholdTests(unittest.TestCase):
    def test_combination_space(self):
        self.assertEqual(COMBINATION_SPACE, 292_201_338)

    def test_zero_other_tickets_keeps_full_jackpot(self):
        self.assertEqual(expected_jackpot_share(0), 1.0)

    def test_sharing_reduces_expected_share(self):
        self.assertLess(expected_jackpot_share(100_000_000), 1.0)
        self.assertGreater(expected_jackpot_share(100_000_000), 0.8)

    def test_absolute_optimistic_floor(self):
        self.assertAlmostEqual(
            required_cash_jackpot(LOWER_EV, 0),
            490_933_823.3529015,
            places=5,
        )

    def test_full_space_ideal_floor_equals_single_ticket_no_sharing_floor(self):
        self.assertAlmostEqual(
            full_space_required_jackpot_without_external_sharing(LOWER_EV),
            required_cash_jackpot(LOWER_EV, 0),
            places=5,
        )

    def test_external_winner_cap_scales_required_jackpot(self):
        base = full_space_required_jackpot_without_external_sharing(LOWER_EV)
        self.assertAlmostEqual(
            full_space_required_jackpot_with_external_winner_cap(LOWER_EV, 2),
            base * 3,
            places=5,
        )


if __name__ == "__main__":
    unittest.main()
