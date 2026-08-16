from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class HedgeResult:
    win_profit: float
    lose_profit: float
    guaranteed_profit: float


@dataclass(frozen=True)
class SelectiveRefundHedgeResult:
    win_profit: float
    eligible_loss_profit: float
    ineligible_loss_profit: float
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


def selective_cash_refund_back_lay_hedge(
    *,
    back_stake: float,
    back_decimal_odds: float,
    lay_decimal_odds: float,
    lay_stake: float,
    cash_refund: float,
    exchange_commission_rate: float = 0.0,
) -> SelectiveRefundHedgeResult:
    """Evaluate a back/lay hedge when only some losing outcomes receive cash.

    This models offers such as horse-racing money-back promotions where the
    selection is refunded only for specified finishing positions. The exchange
    lay wins whenever the backed selection does not win, so eligible and
    ineligible losing branches have the same hedge payoff; only the eligible
    branch receives the refund.

    A crucial consequence is that, whenever an ineligible losing outcome
    remains possible, the refund cannot improve the strict all-outcome floor:
    the worst losing branch is the ineligible one. Any strictly positive floor
    therefore already requires an ordinary back/lay arbitrage before counting
    the promotion.
    """
    if back_stake <= 0:
        raise ValueError("back_stake must be positive")
    if back_decimal_odds <= 1 or lay_decimal_odds <= 1:
        raise ValueError("decimal odds must exceed 1")
    if lay_stake < 0 or cash_refund < 0:
        raise ValueError("lay_stake and cash_refund must be non-negative")
    if not 0 <= exchange_commission_rate < 1:
        raise ValueError("exchange_commission_rate must be in [0, 1)")

    win_profit = (
        back_stake * (back_decimal_odds - 1.0)
        - lay_stake * (lay_decimal_odds - 1.0)
    )
    lay_win_net = lay_stake * (1.0 - exchange_commission_rate)
    ineligible_loss_profit = -back_stake + lay_win_net
    eligible_loss_profit = ineligible_loss_profit + cash_refund

    return SelectiveRefundHedgeResult(
        win_profit=win_profit,
        eligible_loss_profit=eligible_loss_profit,
        ineligible_loss_profit=ineligible_loss_profit,
        guaranteed_profit=min(
            win_profit,
            eligible_loss_profit,
            ineligible_loss_profit,
        ),
    )


def selective_refund_requires_underlying_arbitrage(
    *,
    back_decimal_odds: float,
    lay_decimal_odds: float,
    exchange_commission_rate: float = 0.0,
) -> bool:
    """Return whether a positive back/lay floor is even algebraically possible.

    With at least one non-refunded losing outcome, a positive floor requires a
    lay stake x satisfying simultaneously:

        x > S/(1-c)
        x < S*(O_back-1)/(O_lay-1)

    for stake S and commission c. Such an x exists iff the inequality below is
    true. This is precisely an underlying bookmaker-vs-exchange price edge; the
    selective refund does not create it.
    """
    if back_decimal_odds <= 1 or lay_decimal_odds <= 1:
        raise ValueError("decimal odds must exceed 1")
    if not 0 <= exchange_commission_rate < 1:
        raise ValueError("exchange_commission_rate must be in [0, 1)")
    return (
        (back_decimal_odds - 1.0) * (1.0 - exchange_commission_rate)
        > (lay_decimal_odds - 1.0)
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
