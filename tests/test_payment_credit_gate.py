import unittest

from loto_research.payment_credit_gate import PaymentCreditCase, reward_floor


class PaymentCreditGateTests(unittest.TestCase):
    def test_non_cash_bonus_has_zero_strict_reward_floor(self):
        self.assertEqual(
            reward_floor(
                cash_withdrawable=False,
                deterministic_vesting=True,
                nominal_reward=10.0,
            ),
            0.0,
        )

    def test_discretionary_cash_bonus_has_zero_strict_reward_floor(self):
        self.assertEqual(
            reward_floor(
                cash_withdrawable=True,
                deterministic_vesting=False,
                nominal_reward=10.0,
            ),
            0.0,
        )

    def test_positive_cash_reward_still_fails_if_cost_bound_is_larger(self):
        case = PaymentCreditCase(
            committed_principal=100.0,
            guaranteed_principal_recovery=100.0,
            guaranteed_withdrawable_cash_reward=5.0,
            worst_case_costs=6.0,
        )
        self.assertEqual(case.guaranteed_net_floor(), -1.0)
        self.assertFalse(case.is_strict_guarantee())

    def test_true_principal_preserving_cash_credit_would_pass(self):
        case = PaymentCreditCase(
            committed_principal=100.0,
            guaranteed_principal_recovery=100.0,
            guaranteed_withdrawable_cash_reward=5.0,
            worst_case_costs=1.0,
        )
        self.assertEqual(case.guaranteed_net_floor(), 4.0)
        self.assertTrue(case.is_strict_guarantee())


if __name__ == "__main__":
    unittest.main()
