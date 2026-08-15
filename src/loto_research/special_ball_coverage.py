from __future__ import annotations

from math import comb
from typing import Mapping


def special_ball_full_coverage_counts(
    white_pool: int,
    white_picks: int,
    special_pool: int,
) -> dict[tuple[int, bool], int]:
    """Exact counts for buying every white-set × special-ball play once."""
    if white_pool <= 0 or white_picks <= 0 or white_picks > white_pool:
        raise ValueError("invalid white pool/picks")
    if special_pool <= 0:
        raise ValueError("special_pool must be positive")

    counts: dict[tuple[int, bool], int] = {}
    outside = white_pool - white_picks
    for matches in range(white_picks + 1):
        misses = white_picks - matches
        white_count = 0 if misses > outside else comb(white_picks, matches) * comb(outside, misses)
        counts[(matches, True)] = white_count
        counts[(matches, False)] = white_count * (special_pool - 1)
    return counts


def special_ball_full_coverage_value(
    white_pool: int,
    white_picks: int,
    special_pool: int,
    ticket_price: float,
    payouts: Mapping[tuple[int, bool], float],
) -> tuple[int, float, float, float]:
    """Return line count, cost, deterministic gross and gross/cost ratio."""
    if ticket_price < 0:
        raise ValueError("ticket_price cannot be negative")
    counts = special_ball_full_coverage_counts(white_pool, white_picks, special_pool)
    lines = comb(white_pool, white_picks) * special_pool
    cost = lines * ticket_price
    gross = 0.0
    for outcome, payout in payouts.items():
        if payout < 0:
            raise ValueError("payout cannot be negative")
        gross += counts.get(outcome, 0) * float(payout)
    return lines, cost, gross, gross / cost if cost else 0.0
