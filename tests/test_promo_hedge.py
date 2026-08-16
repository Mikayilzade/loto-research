import unittest

from loto_research.promo_hedge import (
    cash_refund_same_odds_hedge,
    refund_hedge_has_strict_mechanical_profit,
    selective_cash_refund_back_lay_hedge,
    selective_refund_requires_underlying_arbitrage,
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

    def test_selective_refund_does_not_fix_non_refunded_loss_branch(self):
        result = selective_cash_refund_back_lay_hedge(
            back_stake=5.0,
            back_decimal_odds=5.0,
            lay_decimal_odds=5.1,
            lay_stake=5.3,
            cash_refund=5.0,
            exchange_commission_rate=0.02,
        )
        self.assertGreater(result.eligible_loss_profit, 0.0)
        self.assertLess(result.ineligible_loss_profit, result.eligible_loss_profit)
        self.assertLess(result.guaranteed_profit, 0.0)

    def test_selective_refund_requires_preexisting_price_arbitrage(self):
        self.assertFalse(
            selective_refund_requires_underlying_arbitrage(
                back_decimal_odds=5.0,
                lay_decimal_odds=5.1,
                exchange_commission_rate=0.02,
            )
        )
        self.assertTrue(
            selective_refund_requires_underlying_arbitrage(
                back_decimal_odds=5.5,
                lay_decimal_odds=5.0,
                exchange_commission_rate=0.02,
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
