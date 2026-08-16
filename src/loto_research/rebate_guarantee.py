from __future__ import annotations


def guaranteed_net(
    spend: float,
    minimum_cash_payout: float,
    withdrawable_cash_rebate: float = 0.0,
    execution_costs: float = 0.0,
) -> float:
    """Worst-case net cash profit for a deterministic rebate + lottery portfolio.

    Nonwithdrawable credits/free plays must NOT be entered as cash rebates here;
    their cash floor is handled separately and is zero whenever the credited
    wager has a legal zero-cash outcome.
    """
    values = (spend, minimum_cash_payout, withdrawable_cash_rebate, execution_costs)
    if any(value < 0 for value in values):
        raise ValueError("inputs cannot be negative")
    return minimum_cash_payout + withdrawable_cash_rebate - spend - execution_costs


def required_cash_rebate(
    spend: float,
    minimum_cash_payout: float = 0.0,
    execution_costs: float = 0.0,
) -> float:
    """Cash rebate needed to reach break-even in the worst outcome."""
    values = (spend, minimum_cash_payout, execution_costs)
    if any(value < 0 for value in values):
        raise ValueError("inputs cannot be negative")
    return max(0.0, spend + execution_costs - minimum_cash_payout)


def zero_floor_credit_can_guarantee_profit(
    spend: float,
    direct_minimum_cash_payout: float,
    credit_face_value: float,
    *,
    credit_has_zero_cash_outcome: bool,
    execution_costs: float = 0.0,
) -> bool:
    """Necessary-condition screen for free-play / lottery-credit promotions.

    Face value is deliberately ignored when the credited product has a legal
    zero-cash outcome. In that case its strict cash floor is zero regardless of
    advertised face value.
    """
    if min(spend, direct_minimum_cash_payout, credit_face_value, execution_costs) < 0:
        raise ValueError("inputs cannot be negative")
    credit_floor = 0.0 if credit_has_zero_cash_outcome else credit_face_value
    return direct_minimum_cash_payout + credit_floor > spend + execution_costs
