from __future__ import annotations

from typing import Iterable


def cover_all_floor(numbers: int, wager: float, minimum_prize: float) -> tuple[float, float, float]:
    """Return cost, minimum gross payout, and minimum gross-return ratio.

    Assumes exactly one of `numbers` mutually-exclusive draw outcomes wins and
    every outcome is purchased once at the same wager.
    """
    if numbers <= 0 or wager <= 0 or minimum_prize < 0:
        raise ValueError("invalid arguments")
    cost = numbers * wager
    return cost, minimum_prize, minimum_prize / cost


def prize_table_ev(rows: Iterable[tuple[float, float]]) -> float:
    """EV from published overall prize odds rows `(prize, one_in_odds)`."""
    total = 0.0
    for prize, odds in rows:
        if prize < 0 or odds <= 0:
            raise ValueError("invalid prize/odds row")
        total += prize / odds
    return total


def random_overlay_guarantee_value(has_zero_payout_branch: bool, minimum_payout: float = 0.0) -> float:
    """Strict guaranteed contribution of a random auxiliary prize."""
    if minimum_payout < 0:
        raise ValueError("minimum_payout cannot be negative")
    return 0.0 if has_zero_payout_branch else minimum_payout
