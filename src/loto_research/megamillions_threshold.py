from __future__ import annotations

from math import comb

POOL_WHITE = 70
PICKS_WHITE = 5
MEGA_BALLS = 24
TICKET_COST = 5.0
COMBINATIONS = comb(POOL_WHITE, PICKS_WHITE) * MEGA_BALLS

# Base non-jackpot prizes before the built-in 2x/3x/4x/5x/10x multiplier.
BASE_PRIZES = {
    (5, False): 1_000_000.0,
    (4, True): 10_000.0,
    (4, False): 500.0,
    (3, True): 200.0,
    (3, False): 10.0,
    (2, True): 10.0,
    (1, True): 7.0,
    (0, True): 5.0,
}

# Exact distribution consistent with official displayed odds (rounded 1-in-2.13, 3.2, 8, 16, 32).
MULTIPLIER_PROBABILITIES = {2: 15/32, 3: 10/32, 4: 4/32, 5: 2/32, 10: 1/32}


def outcome_count(white_matches: int, mega_match: bool) -> int:
    return (
        comb(PICKS_WHITE, white_matches)
        * comb(POOL_WHITE - PICKS_WHITE, PICKS_WHITE - white_matches)
        * (1 if mega_match else MEGA_BALLS - 1)
    )


def expected_multiplier() -> float:
    return sum(m * p for m, p in MULTIPLIER_PROBABILITIES.items())


def lower_tier_expected_value() -> float:
    em = expected_multiplier()
    return sum(outcome_count(w, mb) / COMBINATIONS * base * em for (w, mb), base in BASE_PRIZES.items())


def lower_tier_full_space_gross(multiplier: float) -> float:
    return sum(outcome_count(w, mb) * base * multiplier for (w, mb), base in BASE_PRIZES.items())


def expected_jackpot_share(other_lines: int, popularity_multiplier: float = 1.0) -> float:
    if other_lines < 0:
        raise ValueError('other_lines cannot be negative')
    if popularity_multiplier <= 0:
        raise ValueError('popularity_multiplier must be positive')
    q = popularity_multiplier / COMBINATIONS
    if other_lines == 0:
        return 1.0
    return (1.0 - (1.0 - q) ** (other_lines + 1)) / ((other_lines + 1) * q)


def cash_break_even(other_lines: int = 0, retained_fraction: float = 1.0, popularity_multiplier: float = 1.0) -> float:
    if not (0 < retained_fraction <= 1):
        raise ValueError('retained_fraction must be in (0, 1]')
    lower = lower_tier_expected_value()
    needed_per_play = TICKET_COST - lower
    share = expected_jackpot_share(other_lines, popularity_multiplier)
    return needed_per_play * COMBINATIONS / (share * retained_fraction)


def full_space_guarantee_floor_before_sharing() -> tuple[float, float, float]:
    """Worst multiplier assignment is 2x on every non-jackpot winning line.

    Returns total acquisition cost, deterministic lower-tier floor, and jackpot
    cash amount required if our jackpot line were guaranteed to be sole winner.
    External jackpot sharing can make the true all-outcome guarantee requirement
    unbounded absent a rule-based cap on other winning tickets.
    """
    cost = TICKET_COST * COMBINATIONS
    lower_floor = lower_tier_full_space_gross(2.0)
    return cost, lower_floor, cost - lower_floor
