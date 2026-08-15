import unittest

from loto_research.forced_distribution import (
    ForcedDistributionScreen,
    blended_payout_fraction,
    full_space_spend,
)


class ForcedDistributionTests(unittest.TestCase):
    def test_uk_lotto_takeout_hurdle(self):
        spend = full_space_spend(45_057_474, 2.0)
        screen = ForcedDistributionScreen(
            spend=spend,
            player_funded_payout_fraction=0.50,
        )
        self.assertEqual(spend, 90_114_948.0)
        self.assertEqual(screen.minimum_external_subsidy_required, 45_057_474.0)
        self.assertFalse(screen.passes_necessary_condition())

    def test_austrian_blended_fraction(self):
        fraction = blended_payout_fraction((1.50, 0.80), (0.48, 0.45))
        self.assertAlmostEqual(fraction, 1.08 / 2.30, places=15)

    def test_austrian_lottoplus_promo_still_fails(self):
        spend = full_space_spend(8_145_060, 2.30)
        fraction = blended_payout_fraction((1.50, 0.80), (0.48, 0.45))
        screen = ForcedDistributionScreen(
            spend=spend,
            player_funded_payout_fraction=fraction,
            guaranteed_external_subsidy=1_000_000.0,
        )
        self.assertEqual(spend, 18_733_638.0)
        self.assertAlmostEqual(
            screen.player_funded_return_upper_bound,
            8_796_664.8,
            places=6,
        )
        self.assertAlmostEqual(
            screen.minimum_external_subsidy_required,
            9_936_973.2,
            places=6,
        )
        self.assertAlmostEqual(screen.optimistic_net_upper_bound, -8_936_973.2, places=6)
        self.assertFalse(screen.passes_necessary_condition())

    def test_external_subsidy_can_pass_gate_but_is_not_sufficient(self):
        screen = ForcedDistributionScreen(
            spend=100.0,
            player_funded_payout_fraction=0.60,
            guaranteed_external_subsidy=41.0,
        )
        self.assertTrue(screen.passes_necessary_condition())


if __name__ == "__main__":
    unittest.main()
