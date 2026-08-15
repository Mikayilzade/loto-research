from __future__ import annotations

from dataclasses import dataclass
from typing import Sequence


@dataclass(frozen=True)
class ArbResult:
    profitable: bool
    guaranteed_profit: float
    capital: float
    roi: float


def dutching_complete_set(decimal_odds: Sequence[float], target_return: float = 1.0) -> ArbResult:
    """Equal-return dutching across mutually exclusive exhaustive outcomes.

    With decimal odds O_i, stake_i = target_return / O_i.  The payoff is
    target_return in every outcome.  A strict surebet exists iff
    sum_i 1/O_i < 1 after all commissions/taxes have already been embedded
    into the effective odds.
    """
    if target_return <= 0:
        raise ValueError("target_return must be positive")
    if not decimal_odds or any(o <= 1.0 for o in decimal_odds):
        raise ValueError("decimal odds must all exceed 1")
    capital = sum(target_return / o for o in decimal_odds)
    profit = target_return - capital
    return ArbResult(profit > 0, profit, capital, profit / capital)


def back_lay_equal_profit(
    back_odds: float,
    back_stake: float,
    lay_odds: float,
    exchange_commission: float,
) -> tuple[float, ArbResult]:
    """Smarkets-style back/lay equal-profit hedge.

    Commission is a fraction of winning exchange profit.  Uses the published
    equal-profit identity: lay_stake = back_odds*back_stake/(lay_odds-c).
    """
    if back_odds <= 1 or lay_odds <= 1 or back_stake <= 0:
        raise ValueError("invalid odds/stake")
    if not 0 <= exchange_commission < 1:
        raise ValueError("commission must be in [0,1)")
    if lay_odds <= exchange_commission:
        raise ValueError("invalid lay odds/commission")

    lay_stake = back_odds * back_stake / (lay_odds - exchange_commission)
    win_profit = (back_odds - 1) * back_stake - (lay_odds - 1) * lay_stake
    lose_profit = lay_stake * (1 - exchange_commission) - back_stake
    guaranteed = min(win_profit, lose_profit)
    capital = back_stake + (lay_odds - 1) * lay_stake
    return lay_stake, ArbResult(guaranteed > 0, guaranteed, capital, guaranteed / capital)


def complete_set_token_arb(
    yes_cost: float,
    no_cost: float,
    fees_and_gas: float = 0.0,
    redemption_value: float = 1.0,
) -> ArbResult:
    """Binary prediction-market complete-set acquisition/merge test."""
    if min(yes_cost, no_cost, fees_and_gas) < 0 or redemption_value <= 0:
        raise ValueError("invalid costs/value")
    capital = yes_cost + no_cost + fees_and_gas
    profit = redemption_value - capital
    return ArbResult(profit > 0, profit, capital, profit / capital if capital else float("inf"))
