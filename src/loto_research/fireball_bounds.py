from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable


@dataclass(frozen=True)
class PrizeOdds:
    prize: float
    odds_one_in: float

    def expected_value(self) -> float:
        if self.prize < 0 or self.odds_one_in <= 0:
            raise ValueError("invalid prize/odds")
        return self.prize / self.odds_one_in


def fireball_ev_upper_bound(parts: Iterable[PrizeOdds]) -> float:
    """Deliberately favorable EV bound from published prize/odds rows.

    Summing rows is exact when prize events are disjoint.  For Virginia 50/50
    rows, Exact prizes include Any prizes; summing both published rows can
    double-count overlap, so this function is explicitly an *upper bound*.
    If even this bound is below the incremental FIREBALL cost, the add-on is
    conclusively negative-EV.
    """
    return sum(part.expected_value() for part in parts)


def combined_ev_ratio_upper_bound(
    base_ev_ratio_upper: float,
    base_cost: float,
    fireball_parts: Iterable[PrizeOdds],
) -> float:
    """Upper bound on base+FIREBALL gross EV / doubled cost.

    Virginia states that FIREBALL doubles the cost of the play, so the
    incremental FIREBALL stake equals the underlying base-play cost.
    """
    if base_cost <= 0:
        raise ValueError("base_cost must be positive")
    if base_ev_ratio_upper < 0:
        raise ValueError("base_ev_ratio_upper cannot be negative")
    base_ev = base_ev_ratio_upper * base_cost
    fireball_ev = fireball_ev_upper_bound(fireball_parts)
    return (base_ev + fireball_ev) / (2.0 * base_cost)


def additive_portfolio_guarantee_possible(max_constituent_ev_ratio: float) -> bool:
    """Necessary-condition screen for additive nonnegative portfolios.

    If every constituent wager has EV <= stake, strict positive profit in every
    outcome is impossible by linearity of expectation.
    """
    return max_constituent_ev_ratio > 1.0
