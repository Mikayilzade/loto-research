"""Exact UK Lotto probability helpers split by rule regime.

Important rule-version boundary:
- through 6 June 2026: one 6/59 round per £2 line;
- from 10 June 2026: one £2 line is entered into two separate 6/59 rounds.

Do not mix prize tables or draw mechanics across these regimes. The current
(2026+) helpers accept lower-tier prize amounts explicitly where the repository
has not yet captured a primary rules document for the exact values.
"""

from __future__ import annotations

from math import comb
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
    """Old one-round cash EV excluding Match 6 and Match-2 Lucky Dip.

    Applies to the rule regime ending with the 6 June 2026 draw.
    """

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

    One purchased line is entered into two independent rounds. ``prizes`` must
    contain per-round cash values for match5_bonus, match5, match4, match3 and
    match2. Values are explicit so secondary observations are not silently
    promoted into permanent official constants.
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

    For the 2026+ format, winner tables usually report round-wins (Round 1 plus
    Round 2), so set ``rounds_per_ticket=2``. This method-of-moments estimate has
    sampling error and can be biased by non-uniform/correlated player choices.
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


def must_be_won_crowd_average_ev(
    jackpot: float,
    entries: float,
    non_jackpot_value: float | None = None,
    lucky_dip_value: float = 0.0,
) -> float:
    """Crowd-average gross EV for a forced-redistribution draw.

    The jackpot-derived aggregate value is approximately J/N per sold ticket if
    the advertised jackpot fund is fully distributed to players. For the old
    one-round regime, omit ``non_jackpot_value`` to use the historical fixed cash
    baseline plus an explicit Match-2 Lucky-Dip value. For 2026+, pass the
    two-round fixed-cash EV as ``non_jackpot_value`` and leave lucky_dip_value 0.
    """

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
    """EV of a post-draw no-jackpot payout schedule for a uniform fixed line.

    Expected keys: match5_bonus, match5, match4, match3, match2_cash. This is a
    diagnostic using realized per-winner payouts, not a complete ex-ante model.
    """

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
