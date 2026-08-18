import unittest

from loto_research.giftcard_cash_redemption import (
    RedemptionScreen,
    required_discount_rate,
)


class GiftCardRedemptionTests(unittest.TestCase):
    def test_california_strict_under_15_threshold(self):
        s = RedemptionScreen(14.99, 13.50, 0.25, 15.0, True)
        self.assertTrue(s.threshold_eligible)
        self.assertAlmostEqual(s.net_floor_if_valid_and_redeemable, 1.24)

    def test_exact_threshold_not_eligible_when_statute_says_less_than(self):
        s = RedemptionScreen(15.0, 13.0, 0.0, 15.0, True)
        self.assertFalse(s.threshold_eligible)
        self.assertEqual(s.guaranteed_cash_if_valid_and_redeemable, 0.0)

    def test_discount_hurdle_equals_execution_cost_share(self):
        self.assertAlmostEqual(required_discount_rate(10.0, 0.50), 0.05)


if __name__ == "__main__":
    unittest.main()
