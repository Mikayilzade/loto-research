"""Exact UK Lotto probability helpers split by rule regime.

Important rule-version boundary:
- through 6 June 2026: one 6/59 round per £2 line;
- from 10 June 2026: one £2 line is entered into two separate 6/59 rounds.

Do not mix prize tables or draw mechanics across these regimes. Current-regime
sales-proxy helpers are deliberately assumption-driven: the 9.79% jackpot-sales
allocation is authoritative for the pre-2026 procedures and is independently
reported as continuing in 2026, but an updated primary procedure document has
not yet been captured. Treat those outputs as research estimates, not sales data.
"""

from __future__ import annotations

from math import comb, inf
from typing import Mapping


POOL_SIZE = 59
PICKS = 6
TICKET_COST = 2.0
TOTAL_COMBINATIONS = comb(POOL_SIZE, PICKS)


def lotto_probabilities() -> dict[str, float]:
    """Return exact probabilities for one independent UK Lotto 6/59 round."""

    d = TOTAL_COMBINATIONS
    return {
        "match6": 1 / d,
        "match5_bonus": 6 / d,
        "match5": (6 * 52) / d,
        "match4": (comb(6, 4) * comb(53, 2)) / d,
        "match3": (comb(6, 3) * comb(53, 3)) / d,
        "match2": (comb(6, 2) * comb(53, 4)) / d,
    }


def pre_2026_fixed_cash_ev() -> float:
    """Old one-round cash EV excluding Match 6 and Match-2 Lucky Dip."""

    p = lotto_probabilities()
    return (
        p["match5_bonus"] * 1_000_000
        + p["match5"] * 1_750
        + p["match4"] * 140
        + p["match3"] * 30
    )


# Backward-compatible name used by the first historical benchmark/tests.
def ordinary_fixed_cash_ev() -> float:
    return pre_2026_fixed_cash_ev()


def two_round_fixed_cash_ev(prizes: Mapping[str, float]) -> float:
    """Gross fixed cash EV for the 2026+ two-round format, excluding Match 6.

    ``prizes`` contains per-round cash values for match5_bonus, match5, match4,
    match3 and match2. Values stay explicit so observed secondary-source values
    are not silently promoted into permanent official constants.
    """

    required = {"match5_bonus", "match5", "match4", "match3", "match2"}
    missing = required - set(prizes)
    if missing:
        raise ValueError(f"missing prize keys: {sorted(missing)}")
    if any(prizes[key] < 0 for key in required):
        raise ValueError("prizes cannot be negative")

    p = lotto_probabilities()
    one_round = sum(p[key] * prizes[key] for key in required)
    return 2.0 * one_round


def two_round_any_prize_probability(include_match6: bool = True) -> float:
    """Probability a £2 line wins at least one prize across two rounds."""

    p = lotto_probabilities()
    categories = ["match5_bonus", "match5", "match4", "match3", "match2"]
    if include_match6:
        categories.append("match6")
    one_round_any = sum(p[key] for key in categories)
    return 1.0 - (1.0 - one_round_any) ** 2


def estimate_entries_from_winner_count(
    winners: int,
    category: str,
    rounds_per_ticket: int = 1,
) -> float:
    """Estimate sold tickets from category winner-count observations.

    This is only a method-of-moments proxy. It can be materially biased draw by
    draw when players choose numbers non-uniformly; 2026 round-level Match-2
    counts demonstrate that this caveat is economically relevant.
    """

    if winners < 0:
        raise ValueError("winners cannot be negative")
    if rounds_per_ticket <= 0:
        raise ValueError("rounds_per_ticket must be positive")
    probabilities = lotto_probabilities()
    if category not in probabilities:
        raise ValueError(f"unknown category: {category}")
    probability = probabilities[category]
    if probability <= 0:
        raise ValueError("category probability must be positive")
    return winners / (rounds_per_ticket * probability)


def implied_ticket_sales_from_jackpot_growth(
    jackpot_increment: float,
    jackpot_sales_fraction: float = 0.0979,
    ticket_price: float = TICKET_COST,
) -> float:
    """Estimate sold tickets from a rollover jackpot increment.

    Assumes ``jackpot_increment = jackpot_sales_fraction * ticket_price * N``.
    For 2026 this is a research proxy until the current primary procedures are
    captured and reserve/top-up effects are fully modelled. Do not apply across
    resets, jackpot wins, special top-ups or rule changes without review.
    """

    if jackpot_increment < 0:
        raise ValueError("jackpot_increment cannot be negative")
    if not 0 < jackpot_sales_fraction <= 1:
        raise ValueError("jackpot_sales_fraction must be in (0, 1]")
    if ticket_price <= 0:
        raise ValueError("ticket_price must be positive")
    return jackpot_increment / (jackpot_sales_fraction * ticket_price)


def carryover_break_even_max_sales(
    prior_carryover: float,
    non_jackpot_value: float,
    jackpot_sales_fraction: float = 0.0979,
    ticket_price: float = TICKET_COST,
) -> float:
    """Maximum current-draw sales compatible with crowd-average break-even.

    Approximate model:
        J_final = prior_carryover + f * ticket_price * N
        gross_EV = non_jackpot_value + J_final / N

    Solving gross_EV >= ticket_price gives the largest N that still breaks even.
    This assumes the jackpot fund is fully distributable in aggregate and ignores
    reserve/top-up/capping details. It is a screening model, not a profit proof.
    """

    if prior_carryover < 0:
        raise ValueError("prior_carryover cannot be negative")
    if non_jackpot_value < 0:
        raise ValueError("non_jackpot_value cannot be negative")
    if not 0 < jackpot_sales_fraction <= 1:
        raise ValueError("jackpot_sales_fraction must be in (0, 1]")
    if ticket_price <= 0:
        raise ValueError("ticket_price must be positive")

    current_sales_jackpot_value = jackpot_sales_fraction * ticket_price
    gap = ticket_price - non_jackpot_value - current_sales_jackpot_value
    if gap <= 0:
        return inf
    return prior_carryover / gap


def must_be_won_crowd_average_ev(
    jackpot: float,
    entries: float,
    non_jackpot_value: float | None = None,
    lucky_dip_value: float = 0.0,
) -> float:
    """Crowd-average gross EV for a forced-redistribution draw."""

    if jackpot < 0:
        raise ValueError("jackpot cannot be negative")
    if entries <= 0:
        raise ValueError("entries must be positive")
    if lucky_dip_value < 0:
        raise ValueError("lucky_dip_value cannot be negative")

    if non_jackpot_value is None:
        p2 = lotto_probabilities()["match2"]
        non_jackpot_value = pre_2026_fixed_cash_ev() + p2 * lucky_dip_value
    elif non_jackpot_value < 0:
        raise ValueError("non_jackpot_value cannot be negative")

    return non_jackpot_value + jackpot / entries


def must_be_won_break_even_jackpot(
    entries: float,
    non_jackpot_value: float | None = None,
    lucky_dip_value: float = 0.0,
    ticket_cost: float = TICKET_COST,
) -> float:
    """Jackpot needed for crowd-average gross EV to reach ticket cost."""

    if entries <= 0:
        raise ValueError("entries must be positive")
    if ticket_cost <= 0:
        raise ValueError("ticket_cost must be positive")
    if lucky_dip_value < 0:
        raise ValueError("lucky_dip_value cannot be negative")

    if non_jackpot_value is None:
        p2 = lotto_probabilities()["match2"]
        non_jackpot_value = pre_2026_fixed_cash_ev() + p2 * lucky_dip_value
    elif non_jackpot_value < 0:
        raise ValueError("non_jackpot_value cannot be negative")

    return max(0.0, entries * (ticket_cost - non_jackpot_value))


def published_rolldown_schedule_cash_ev(
    prizes: Mapping[str, float],
    rounds_per_ticket: int = 1,
) -> float:
    """EV of a post-draw no-jackpot payout schedule for a uniform fixed line."""

    if rounds_per_ticket <= 0:
        raise ValueError("rounds_per_ticket must be positive")

    p = lotto_probabilities()
    required = {"match5_bonus", "match5", "match4", "match3", "match2_cash"}
    missing = required - set(prizes)
    if missing:
        raise ValueError(f"missing prize keys: {sorted(missing)}")
    if any(prizes[key] < 0 for key in required):
        raise ValueError("prizes cannot be negative")

    one_round = (
        p["match5_bonus"] * prizes["match5_bonus"]
        + p["match5"] * prizes["match5"]
        + p["match4"] * prizes["match4"]
        + p["match3"] * prizes["match3"]
        + p["match2"] * prizes["match2_cash"]
    )
    return rounds_per_ticket * one_round
