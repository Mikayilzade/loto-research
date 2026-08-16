import unittest

from loto_research.rebate_guarantee import (
    guaranteed_net,
    required_cash_rebate,
    zero_floor_credit_can_guarantee_profit,
)


class RebateGuaranteeTests(unittest.TestCase):
    def test_zero_payout_game_needs_more_than_100pct_cash_rebate_for_profit(self):
        self.assertEqual(required_cash_rebate(6.0, 0.0), 6.0)
        self.assertEqual(guaranteed_net(6.0, 0.0, 6.0), 0.0)
        self.assertGreater(guaranteed_net(6.0, 0.0, 6.01), 0.0)

    def test_nonwithdrawable_100pct_face_bonus_does_not_create_cash_guarantee(self):
        self.assertFalse(
            zero_floor_credit_can_guarantee_profit(
                spend=6.0,
                direct_minimum_cash_payout=0.0,
                credit_face_value=6.0,
                credit_has_zero_cash_outcome=True,
            )
        )

    def test_cash_rebate_can_combine_with_positive_floor(self):
        self.assertEqual(required_cash_rebate(10.0, 4.0), 6.0)
        self.assertGreater(guaranteed_net(10.0, 4.0, 6.5), 0.0)

    def test_execution_costs_raise_hurdle(self):
        self.assertEqual(required_cash_rebate(10.0, 4.0, 1.0), 7.0)


if __name__ == "__main__":
    unittest.main()
