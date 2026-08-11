"""Exact UK Lotto probabilities and Must Be Won benchmark helpers.

The Must Be Won functions distinguish a crowd-average aggregate benchmark from
strategy-specific sharing. In a Must Be Won draw the jackpot is paid to players
whether Match 6 is hit or the jackpot rolls down. Therefore, if J is the jackpot
fund and N is the number of sold entries, J/N is the average jackpot-derived
value per sold entry across the whole crowd. A particular number-selection
strategy can differ from that average when duplicated/popular selections change
sharing in rolldown categories.
"""

from __future__ import annotations

from math import comb
from typing import Mapping


POOL_SIZE = 59
PICKS = 6
TICKET_COST = 2.0
TOTAL_COMBINATIONS = comb(POOL_SIZE, PICKS)


def lotto_probabilities() -> dict[str, float]:
    """Return exact probabilities for the UK Lotto prize categories."""

    d = TOTAL_COMBINATIONS
    return {
        "match6": 1 / d,
        "match5_bonus": 6 / d,
        "match5": (6 * 52) / d,
        "match4": (comb(6, 4) * comb(53, 2)) / d,
        "match3": (comb(6, 3) * comb(53, 3)) / d,
        "match2": (comb(6, 2) * comb(53, 4)) / d,
    }


def ordinary_fixed_cash_ev() -> float:
    """Cash EV excluding Match 6 and the non-cash Match 2 Lucky Dip."""

    p = lotto_probabilities()
    return (
        p["match5_bonus"] * 1_000_000
        + p["match5"] * 1_750
        + p["match4"] * 140
        + p["match3"] * 30
    )


def estimate_entries_from_winner_count(winners: int, category: str) -> float:
    """Estimate sold entries as winners / exact category probability.

    This is a simple method-of-moments estimate. It is useful for historical
    draws when official sales counts are unavailable, but it carries sampling
    error and may be affected by correlated/duplicated player selections.
    """

    if winners < 0:
        raise ValueError("winners cannot be negative")
    probabilities = lotto_probabilities()
    if category not in probabilities:
        raise ValueError(f"unknown category: {category}")
    probability = probabilities[category]
    if probability <= 0:
        raise ValueError("category probability must be positive")
    return winners / probability


def must_be_won_crowd_average_ev(
    jackpot: float,
    entries: float,
    lucky_dip_value: float = 0.0,
) -> float:
    """Crowd-average gross EV for a Must Be Won draw.

    ``lucky_dip_value`` is deliberately explicit. Use 0 for a conservative
    cash-only benchmark; £2 is a face-value upper bound when a future free line
    genuinely substitutes for a line that would otherwise have been purchased.
    """

    if jackpot < 0:
        raise ValueError("jackpot cannot be negative")
    if entries <= 0:
        raise ValueError("entries must be positive")
    if lucky_dip_value < 0:
        raise ValueError("lucky_dip_value cannot be negative")

    p2 = lotto_probabilities()["match2"]
    return ordinary_fixed_cash_ev() + jackpot / entries + p2 * lucky_dip_value


def must_be_won_break_even_jackpot(
    entries: float,
    lucky_dip_value: float = 0.0,
    ticket_cost: float = TICKET_COST,
) -> float:
    """Jackpot needed for the crowd-average Must Be Won EV to reach ticket cost."""

    if entries <= 0:
        raise ValueError("entries must be positive")
    if ticket_cost <= 0:
        raise ValueError("ticket_cost must be positive")
    if lucky_dip_value < 0:
        raise ValueError("lucky_dip_value cannot be negative")

    p2 = lotto_probabilities()["match2"]
    non_jackpot_value = ordinary_fixed_cash_ev() + p2 * lucky_dip_value
    return max(0.0, entries * (ticket_cost - non_jackpot_value))


def published_rolldown_schedule_cash_ev(prizes: Mapping[str, float]) -> float:
    """EV of a published no-jackpot rolldown schedule for a uniform fixed line.

    Expected keys are ``match5_bonus``, ``match5``, ``match4``, ``match3`` and
    ``match2_cash``. This is a post-draw schedule diagnostic, not a complete
    ex-ante model: prize-per-winner amounts themselves depend on winner counts.
    """

    p = lotto_probabilities()
    required = {"match5_bonus", "match5", "match4", "match3", "match2_cash"}
    missing = required - set(prizes)
    if missing:
        raise ValueError(f"missing prize keys: {sorted(missing)}")
    if any(prizes[key] < 0 for key in required):
        raise ValueError("prizes cannot be negative")

    return (
        p["match5_bonus"] * prizes["match5_bonus"]
        + p["match5"] * prizes["match5"]
        + p["match4"] * prizes["match4"]
        + p["match3"] * prizes["match3"]
        + p["match2"] * prizes["match2_cash"]
    )
