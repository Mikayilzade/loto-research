import unittest

from loto_research.free_bet_conversion import (
    free_bet_equal_profit,
    qualifying_cash_bet_equal_profit,
    welcome_offer_floor,
)


class FreeBetConversionTests(unittest.TestCase):
    def test_even_2_odds_zero_commission_converts_half_token_to_cash(self):
        lay, floor = free_bet_equal_profit(10.0, 2.0, 2.0, 0.0)
        self.assertAlmostEqual(lay, 5.0, places=12)
        self.assertAlmostEqual(floor, 5.0, places=12)

    def test_two_percent_commission(self):
        lay, floor = free_bet_equal_profit(10.0, 2.0, 2.0, 0.02)
        self.assertAlmostEqual(lay, 5.05050505050505, places=12)
        self.assertAlmostEqual(floor, 4.94949494949495, places=12)

    def test_qualifier_is_nearly_flat_at_matching_prices(self):
        lay, floor = qualifying_cash_bet_equal_profit(0.05, 2.0, 2.0, 0.02)
        self.assertAlmostEqual(lay, 0.05050505050505051, places=12)
        self.assertAlmostEqual(floor, -0.0005050505050505, places=12)

    def test_sky_style_three_tokens_mechanical_floor(self):
        floor = welcome_offer_floor(
            [10.0, 10.0, 10.0],
            token_bookmaker_odds=2.0,
            token_lay_odds=2.0,
            qualifying_stake=0.05,
            qualifying_bookmaker_odds=2.0,
            qualifying_lay_odds=2.0,
            exchange_commission=0.02,
        )
        self.assertAlmostEqual(floor, 14.8479797979798, places=12)


if __name__ == "__main__":
    unittest.main()
