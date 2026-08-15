import unittest

from loto_research.live_complete_set import (
    BookLevel,
    fee_aware_binary_complete_set,
    kalshi_crossed_book_required,
    kalshi_market_buy_complete_set_cost,
    max_profitable_quantity,
    taker_fee,
)


class LiveCompleteSetTests(unittest.TestCase):
    def test_polymarket_fee_formula(self):
        self.assertAlmostEqual(taker_fee(100, 0.50, 0.04), 1.0, places=12)
        self.assertAlmostEqual(taker_fee(100, 0.30, 0.04), 0.84, places=12)
        self.assertAlmostEqual(taker_fee(100, 0.70, 0.04), 0.84, places=12)

    def test_top_of_book_pair_below_one_can_be_profitable_fee_free(self):
        result = fee_aware_binary_complete_set(
            [BookLevel(0.47, 100)],
            [BookLevel(0.50, 100)],
            100,
        )
        self.assertTrue(result.profitable)
        self.assertAlmostEqual(result.gross_cost, 97.0)
        self.assertAlmostEqual(result.redemption, 100.0)
        self.assertAlmostEqual(result.guaranteed_profit, 3.0)

    def test_fee_can_destroy_apparent_cross(self):
        result = fee_aware_binary_complete_set(
            [BookLevel(0.49, 100)],
            [BookLevel(0.50, 100)],
            100,
            yes_fee_rate=0.05,
            no_fee_rate=0.05,
        )
        self.assertFalse(result.profitable)
        self.assertGreater(result.fees, 2.0)

    def test_depth_walking_prevents_top_quote_overstatement(self):
        yes = [BookLevel(0.45, 10), BookLevel(0.56, 100)]
        no = [BookLevel(0.50, 100)]
        ten = fee_aware_binary_complete_set(yes, no, 10)
        self.assertTrue(ten.profitable)
        twenty = fee_aware_binary_complete_set(yes, no, 20)
        self.assertFalse(twenty.profitable)

    def test_largest_profitable_quantity_found_on_depth_breakpoint(self):
        yes = [BookLevel(0.45, 10), BookLevel(0.56, 100)]
        no = [BookLevel(0.50, 100)]
        best = max_profitable_quantity(yes, no)
        self.assertIsNotNone(best)
        self.assertAlmostEqual(best.quantity, 10.0)

    def test_kalshi_implied_complete_set(self):
        self.assertAlmostEqual(kalshi_market_buy_complete_set_cost(0.48, 0.49), 1.03)
        self.assertFalse(kalshi_crossed_book_required(0.48, 0.49))
        self.assertAlmostEqual(kalshi_market_buy_complete_set_cost(0.52, 0.51), 0.97)
        self.assertTrue(kalshi_crossed_book_required(0.52, 0.51))


if __name__ == "__main__":
    unittest.main()
