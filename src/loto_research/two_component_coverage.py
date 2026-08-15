from __future__ import annotations

from dataclasses import dataclass
from math import comb
from typing import Mapping


@dataclass(frozen=True)
class CoverageResult:
    entries: int
    cost: float
    gross: float
    return_ratio: float
    net: float


def main_match_counts(pool_size: int, picks: int) -> dict[int, int]:
    """Exact main-number match counts when every k-subset is owned once."""
    if pool_size <= 0 or picks <= 0 or picks > pool_size:
        raise ValueError("invalid pool_size/picks")
    outside = pool_size - picks
    result: dict[int, int] = {}
    for matches in range(picks + 1):
        misses = picks - matches
        result[matches] = (
            comb(picks, matches) * comb(outside, misses)
            if 0 <= misses <= outside
            else 0
        )
    return result


def fixed_bonus_full_coverage(
    *,
    main_pool: int,
    main_picks: int,
    bonus_pool: int,
    stake: float,
    payout_if_bonus: Mapping[int, float],
    payout_if_not_bonus: Mapping[int, float],
) -> CoverageResult:
    """Deterministic full-space payout for k-main + one bonus-number games.

    We buy every `main_picks` subset of the main pool paired with every possible
    bonus number exactly once. For each main-number subset, exactly one covered
    line has the realized bonus number and `bonus_pool-1` do not.

    `payout_if_bonus[m]` is the payout for exactly m main matches plus bonus.
    `payout_if_not_bonus[m]` is the payout for exactly m main matches without
    bonus. Missing categories are treated as zero-prize outcomes.
    """
    if bonus_pool <= 0:
        raise ValueError("bonus_pool must be positive")
    if stake < 0:
        raise ValueError("stake cannot be negative")

    counts = main_match_counts(main_pool, main_picks)
    entries = comb(main_pool, main_picks) * bonus_pool
    cost = entries * stake
    gross = 0.0

    for matches, count in counts.items():
        bonus_prize = float(payout_if_bonus.get(matches, 0.0))
        nonbonus_prize = float(payout_if_not_bonus.get(matches, 0.0))
        if bonus_prize < 0 or nonbonus_prize < 0:
            raise ValueError("payouts cannot be negative")
        gross += count * bonus_prize
        gross += count * (bonus_pool - 1) * nonbonus_prize

    ratio = gross / cost if cost else 0.0
    return CoverageResult(
        entries=entries,
        cost=cost,
        gross=gross,
        return_ratio=ratio,
        net=gross - cost,
    )
