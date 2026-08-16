import unittest

from loto_research.commission_subsidy import (
    commission_rebate_can_create_profit_without_gross_edge,
    post_rebate_profit,
)


class CommissionSubsidyTests(unittest.TestCase):
    def test_full_rebate_recovers_zero_commission_result(self):
        self.assertEqual(post_rebate_profit(0.0, 2.0, 1.0), 0.0)
        self.assertEqual(post_rebate_profit(5.0, 2.0, 1.0), 5.0)

    def test_partial_rebate_cannot_exceed_precommission_profit(self):
        self.assertLessEqual(post_rebate_profit(3.0, 2.0, 0.5), 3.0)

    def test_no_nonpositive_gross_state_becomes_positive_from_commission_refund_only(self):
        for gross in (0.0, -0.01, -10.0):
            for rebate in (0.0, 0.5, 1.0):
                self.assertFalse(
                    commission_rebate_can_create_profit_without_gross_edge(
                        gross, 2.0, rebate
                    )
                )


if __name__ == "__main__":
    unittest.main()
