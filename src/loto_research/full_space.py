from __future__ import annotations

from math import comb
from typing import Mapping


def full_space_match_counts(pool_size: int, picks: int) -> dict[int, int]:
    """Count how many covered k-subsets obtain each exact match count.

    If every `picks`-subset of a `pool_size` universe is bought exactly once,
    then for any realized winning `picks`-subset the number of tickets with
    exactly m matches is C(picks,m) * C(pool_size-picks, picks-m).
    """
    if pool_size <= 0 or picks <= 0 or picks > pool_size:
        raise ValueError("invalid pool_size/picks")
    result: dict[int, int] = {}
    for matches in range(picks + 1):
        misses = picks - matches
        if misses > pool_size - picks:
            result[matches] = 0
        else:
            result[matches] = comb(picks, matches) * comb(pool_size - picks, misses)
    return result


def fixed_match_full_coverage(
    pool_size: int,
    picks: int,
    stake_per_variant: float,
    payouts_by_matches: Mapping[int, float],
) -> tuple[int, float, float, float]:
    """Return variants, total cost, deterministic gross payout and ROI.

    This applies when payouts are fixed by exact match count and each covered
    variant is bought once. Sharing/tax are deliberately excluded; therefore a
    negative result here is already sufficient to reject a guaranteed-profit
    full-coverage strategy.
    """
    if stake_per_variant < 0:
        raise ValueError("stake_per_variant cannot be negative")
    counts = full_space_match_counts(pool_size, picks)
    variants = comb(pool_size, picks)
    cost = variants * stake_per_variant
    gross = 0.0
    for matches, payout in payouts_by_matches.items():
        if payout < 0:
            raise ValueError("payout cannot be negative")
        gross += counts.get(int(matches), 0) * float(payout)
    roi = gross / cost if cost else 0.0
    return variants, cost, gross, roi


def ordered_last_hit_full_coverage(
    pool_size: int,
    picks: int,
    stake_per_variant: float,
    multiplier_by_last_position: Mapping[int, float],
) -> tuple[int, float, float, float]:
    """Exact full-space result for ordered-draw games such as ONLOTO.

    Buy every unordered `picks`-subset once. If a covered variant wins when all
    its selected numbers have appeared by draw position j, and its payout is
    stake * multiplier[j], then exactly C(j-1, picks-1) covered variants have
    their last selected number at position j. Summing this over winning
    positions gives a deterministic gross payout for any draw order.
    """
    if pool_size <= 0 or picks <= 0 or picks > pool_size:
        raise ValueError("invalid pool_size/picks")
    if stake_per_variant < 0:
        raise ValueError("stake_per_variant cannot be negative")

    variants = comb(pool_size, picks)
    cost = variants * stake_per_variant
    gross_multiplier_units = 0.0
    for position, multiplier in multiplier_by_last_position.items():
        position = int(position)
        if position < picks or position > pool_size:
            raise ValueError("invalid last-hit position")
        if multiplier < 0:
            raise ValueError("multiplier cannot be negative")
        gross_multiplier_units += comb(position - 1, picks - 1) * float(multiplier)

    gross = gross_multiplier_units * stake_per_variant
    roi = gross / cost if cost else 0.0
    return variants, cost, gross, roi
