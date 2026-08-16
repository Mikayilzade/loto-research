import unittest

from loto_research.promo_hedge import (
    cash_refund_same_odds_hedge,
    refund_hedge_has_strict_mechanical_profit,
    strict_guarantee_contract_gate,
)


class PromoHedgeTests(unittest.TestCase):
    def test_full_cash_refund_plus_small_underlay_is_mechanical_sure_profit(self):
        result = cash_refund_same_odds_hedge(
            back_stake=10.0,
            decimal_odds=2.0,
            lay_stake=9.5,
            cash_refund=10.0,
        )
        self.assertAlmostEqual(result.win_profit, 0.5)
        self.assertAlmostEqual(result.lose_profit, 9.5)
        self.assertAlmostEqual(result.guaranteed_profit, 0.5)

    def test_commission_still_leaves_positive_floor_in_example(self):
        result = cash_refund_same_odds_hedge(
            back_stake=10.0,
            decimal_odds=2.0,
            lay_stake=9.5,
            cash_refund=10.0,
            commission_rate=0.05,
        )
        self.assertGreater(result.guaranteed_profit, 0.0)

    def test_mechanical_profit_helper(self):
        self.assertTrue(
            refund_hedge_has_strict_mechanical_profit(
                back_stake=10.0,
                decimal_odds=2.0,
                lay_stake=9.5,
                cash_refund=10.0,
                commission_rate=0.05,
            )
        )

    def test_contract_clawback_blocks_terminal_guarantee(self):
        self.assertFalse(
            strict_guarantee_contract_gate(
                mechanical_profit_positive=True,
                refund_is_withdrawable_cash=True,
                both_legs_irrevocably_matched=True,
                settlement_mismatch_eliminated=True,
                anti_arbitrage_clawback_possible=True,
                all_costs_covered=True,
            )
        )

    def test_unconditional_contract_can_pass_gate(self):
        self.assertTrue(
            strict_guarantee_contract_gate(
                mechanical_profit_positive=True,
                refund_is_withdrawable_cash=True,
                both_legs_irrevocably_matched=True,
                settlement_mismatch_eliminated=True,
                anti_arbitrage_clawback_possible=False,
                all_costs_covered=True,
            )
        )


if __name__ == "__main__":
    unittest.main()
