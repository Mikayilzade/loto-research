from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class HedgeResult:
    win_profit: float
    lose_profit: float
    guaranteed_profit: float


def cash_refund_same_odds_hedge(
    *,
    back_stake: float,
    decimal_odds: float,
    lay_stake: float,
    cash_refund: float,
    commission_rate: float = 0.0,
) -> HedgeResult:
    """Evaluate a two-sided same-market hedge around a cash-refund qualifying bet.

    The qualifying leg is a back bet of ``back_stake`` at ``decimal_odds``.
    The hedge is a lay bet at the same odds. Commission is applied only to a
    positive pre-commission market result, which is a conservative simplified
    model suitable for screening.
    """
    if back_stake <= 0:
        raise ValueError("back_stake must be positive")
    if decimal_odds <= 1:
        raise ValueError("decimal_odds must exceed 1")
    if lay_stake < 0 or cash_refund < 0:
        raise ValueError("lay_stake and cash_refund must be non-negative")
    if not 0 <= commission_rate < 1:
        raise ValueError("commission_rate must be in [0, 1)")

    win_pre = (back_stake - lay_stake) * (decimal_odds - 1.0)
    lose_pre = -back_stake + lay_stake + cash_refund

    win_profit = win_pre * (1.0 - commission_rate) if win_pre > 0 else win_pre
    lose_profit = lose_pre * (1.0 - commission_rate) if lose_pre > 0 else lose_pre

    return HedgeResult(
        win_profit=win_profit,
        lose_profit=lose_profit,
        guaranteed_profit=min(win_profit, lose_profit),
    )


def refund_hedge_has_strict_mechanical_profit(
    *,
    back_stake: float,
    decimal_odds: float,
    lay_stake: float,
    cash_refund: float,
    commission_rate: float = 0.0,
) -> bool:
    return cash_refund_same_odds_hedge(
        back_stake=back_stake,
        decimal_odds=decimal_odds,
        lay_stake=lay_stake,
        cash_refund=cash_refund,
        commission_rate=commission_rate,
    ).guaranteed_profit > 0


def strict_guarantee_contract_gate(
    *,
    mechanical_profit_positive: bool,
    refund_is_withdrawable_cash: bool,
    both_legs_irrevocably_matched: bool,
    settlement_mismatch_eliminated: bool,
    anti_arbitrage_clawback_possible: bool,
    all_costs_covered: bool,
) -> bool:
    """Necessary gate for promoting a promo hedge to strict executable guarantee."""
    return all(
        (
            mechanical_profit_positive,
            refund_is_withdrawable_cash,
            both_legs_irrevocably_matched,
            settlement_mismatch_eliminated,
            not anti_arbitrage_clawback_possible,
            all_costs_covered,
        )
    )
