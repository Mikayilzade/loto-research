from __future__ import annotations

from math import comb
from typing import Mapping


POOL_SIZE = 70
DRAW_SIZE = 20
CATEGORY_CAP_CAD = 4_000_000.0

# Official OLG $1-bet prize table, keyed by Pick category and exact matches.
PAYOUTS_BY_PICK: dict[int, dict[int, float]] = {
    2: {2: 7.0},
    3: {3: 25.0},
    4: {4: 100.0},
    5: {5: 250.0, 4: 5.0},
    6: {6: 1_000.0, 5: 25.0},
    7: {7: 5_000.0, 6: 50.0, 5: 5.0},
    8: {8: 25_000.0, 7: 200.0, 6: 10.0},
    9: {9: 50_000.0, 8: 1_000.0, 7: 100.0, 6: 5.0},
    10: {10: 250_000.0, 9: 5_000.0, 8: 200.0, 7: 25.0, 0: 2.0},
}


def exact_match_count_full_coverage(pick: int, matches: int) -> int:
    """Number of covered pick-subsets with exactly `matches` hits.

    When every k-subset of 70 is owned once and the draw contains 20 winning
    numbers, exactly C(20,m)*C(50,k-m) of our k-subsets have m matches.
    """
    if not 0 <= matches <= pick <= POOL_SIZE:
        raise ValueError("invalid pick/matches")
    misses = pick - matches
    if misses > POOL_SIZE - DRAW_SIZE:
        return 0
    return comb(DRAW_SIZE, matches) * comb(POOL_SIZE - DRAW_SIZE, misses)


def uncapped_full_coverage(pick: int, stake: float = 1.0) -> tuple[int, float, float, float]:
    """Return variants, cost, favorable uncapped gross and gross return ratio.

    OLG caps aggregate payout in each prize category at CAD 4m. Ignoring that
    cap is deliberately favorable to the player, so a return below 100% here
    is already sufficient to reject guaranteed-profit full coverage.
    """
    if pick not in PAYOUTS_BY_PICK:
        raise ValueError("pick must be 2..10")
    if stake <= 0:
        raise ValueError("stake must be positive")

    variants = comb(POOL_SIZE, pick)
    cost = variants * stake
    gross = 0.0
    for matches, payout_per_dollar in PAYOUTS_BY_PICK[pick].items():
        gross += exact_match_count_full_coverage(pick, matches) * payout_per_dollar * stake
    return variants, cost, gross, gross / cost


def per_selection_gross_ev_ratio(pick: int) -> float:
    """Gross EV/stake for a $1 selection before the CAD 4m category cap.

    By symmetry this equals the full-coverage gross return ratio. The actual
    ratio can only be lower once a prize-category cap binds.
    """
    return uncapped_full_coverage(pick, 1.0)[3]


def additive_portfolio_guarantee_impossible(
    pick_weights: Mapping[int, float],
) -> bool:
    """Necessary-condition rejection for nonnegative additive portfolios.

    If every included base selection has gross EV below stake, then any finite
    nonnegative linear combination also has negative expected profit. A strict
    all-outcome positive-profit portfolio would necessarily have positive
    expected profit, yielding a contradiction.
    """
    total_weight = 0.0
    weighted_ev = 0.0
    for pick, weight in pick_weights.items():
        if pick not in PAYOUTS_BY_PICK:
            raise ValueError("pick must be 2..10")
        if weight < 0:
            raise ValueError("weights must be nonnegative")
        total_weight += weight
        weighted_ev += weight * per_selection_gross_ev_ratio(pick)
    if total_weight <= 0:
        raise ValueError("portfolio must contain positive weight")
    return weighted_ev / total_weight < 1.0
