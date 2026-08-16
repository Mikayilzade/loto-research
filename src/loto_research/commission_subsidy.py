from __future__ import annotations


def post_rebate_profit(pre_commission_profit: float, commission_paid: float, rebate_fraction: float) -> float:
    """Profit after a rebate of already-paid exchange commission.

    `pre_commission_profit` is the outcome P/L before exchange commission.
    Commission is then deducted and the stated fraction is refunded.
    A commission-only subsidy can never outperform the zero-commission result.
    """
    if commission_paid < 0:
        raise ValueError("commission_paid cannot be negative")
    if not 0 <= rebate_fraction <= 1:
        raise ValueError("rebate_fraction must be in [0,1]")
    return pre_commission_profit - commission_paid * (1.0 - rebate_fraction)


def commission_rebate_can_create_profit_without_gross_edge(
    pre_commission_profit: float,
    commission_paid: float,
    rebate_fraction: float,
) -> bool:
    """Whether commission refund alone turns a non-positive gross state positive."""
    result = post_rebate_profit(pre_commission_profit, commission_paid, rebate_fraction)
    return pre_commission_profit <= 0 < result
