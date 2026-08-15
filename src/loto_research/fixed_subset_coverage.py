from __future__ import annotations

from dataclasses import dataclass
from math import comb


@dataclass(frozen=True)
class CoverageResult:
    pool_size: int
    target_size: int
    picks: int
    stake: float
    payout: float
    variants: int
    winning_variants: int
    cost: float
    gross: float
    return_ratio: float


def fixed_subset_full_coverage(
    pool_size: int,
    target_size: int,
    picks: int,
    stake: float,
    payout: float,
) -> CoverageResult:
    """Exact deterministic full-space result for all-selected-numbers-must-hit games.

    Buy every `picks`-subset of a pool of `pool_size` exactly once. If a ticket
    wins iff all its selected numbers are contained in a realized target set of
    size `target_size`, exactly C(target_size, picks) covered variants win for
    every legal realized target set.
    """
    if pool_size <= 0:
        raise ValueError("pool_size must be positive")
    if target_size <= 0 or target_size > pool_size:
        raise ValueError("invalid target_size")
    if picks <= 0 or picks > target_size:
        raise ValueError("picks must be in 1..target_size")
    if stake < 0 or payout < 0:
        raise ValueError("stake and payout must be nonnegative")

    variants = comb(pool_size, picks)
    winning_variants = comb(target_size, picks)
    cost = variants * stake
    gross = winning_variants * payout
    return_ratio = gross / cost if cost else 0.0
    return CoverageResult(
        pool_size=pool_size,
        target_size=target_size,
        picks=picks,
        stake=stake,
        payout=payout,
        variants=variants,
        winning_variants=winning_variants,
        cost=cost,
        gross=gross,
        return_ratio=return_ratio,
    )
