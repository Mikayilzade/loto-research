from __future__ import annotations

from collections import Counter


def super66_full_space_counts() -> dict[int, int]:
    """Exact count of six-digit strings by highest Super66 end-match division.

    The winning string may be normalized to 000000 by digit symmetry.
    A ticket receives only its larger prize when both ends match.
    Returns division -> number of strings in a hypothetical complete 10^6 cover.
    """
    counts: Counter[int] = Counter()
    for value in range(1_000_000):
        s = f"{value:06d}"
        prefix = 0
        for char in s:
            if char == "0":
                prefix += 1
            else:
                break
        suffix = 0
        for char in reversed(s):
            if char == "0":
                suffix += 1
            else:
                break
        run = max(prefix, suffix)
        if run >= 2:
            division = {6: 1, 5: 2, 4: 3, 3: 4, 2: 5}[run]
            counts[division] += 1
    return dict(sorted(counts.items()))


def super66_hypothetical_full_space_floor(
    top_prize_floor: float = 66_666.0,
    stake_per_game: float = 1.0,
) -> tuple[float, float, float]:
    """Cost, gross floor and gross-return ratio for hypothetical unique full cover."""
    counts = super66_full_space_counts()
    payouts = {1: top_prize_floor, 2: 6_666.0, 3: 666.0, 4: 66.0, 5: 6.6}
    cost = 1_000_000 * stake_per_game
    gross = sum(counts[d] * payouts[d] for d in payouts)
    return cost, gross, gross / cost


def cash3_minimal_partition_cover(stake: float = 0.5) -> dict[str, float]:
    """A simple exact partition cover for all 1,000 ordered Cash 3 outcomes.

    - 10 triples (000,111,...) are covered by Exact Order.
    - 270 ordered one-pair outcomes are covered by 90 Any Order 3-way wagers.
    - 720 all-distinct ordered outcomes are covered by 120 Any Order 6-way wagers.

    Published payouts at the 0.50 stake are 250/80/40 respectively.
    """
    if stake <= 0:
        raise ValueError("stake must be positive")
    scale = stake / 0.5
    exact_wagers = 10
    any3_wagers = 90
    any6_wagers = 120
    cost = (exact_wagers + any3_wagers + any6_wagers) * stake
    payouts = {
        "triple": 250.0 * scale,
        "one_pair": 80.0 * scale,
        "all_distinct": 40.0 * scale,
    }
    min_gross = min(payouts.values())
    expected_gross = (
        10 * payouts["triple"]
        + 270 * payouts["one_pair"]
        + 720 * payouts["all_distinct"]
    ) / 1000.0
    return {
        "wagers": exact_wagers + any3_wagers + any6_wagers,
        "cost": cost,
        "min_gross": min_gross,
        "min_return_ratio": min_gross / cost,
        "expected_gross": expected_gross,
        "expected_return_ratio": expected_gross / cost,
    }
