from __future__ import annotations

from dataclasses import dataclass
from math import comb
from typing import Mapping


@dataclass(frozen=True)
class CoverageResult:
    combinations: int
    cost: float
    optimistic_gross: float
    strict_cash_floor: float

    @property
    def optimistic_return(self) -> float:
        return self.optimistic_gross / self.cost

    @property
    def strict_cash_return(self) -> float:
        return self.strict_cash_floor / self.cost


def six_of_n_with_bonus_match_counts(pool_size: int) -> dict[tuple[int, int], int]:
    """Exact ticket counts under complete 6-number coverage.

    Draw has 6 main numbers plus one bonus number. Keys are
    ``(main_matches, bonus_match)`` where bonus_match is 0 or 1.
    """
    if pool_size < 7:
        raise ValueError("pool_size must be at least 7")
    other = pool_size - 7
    counts: dict[tuple[int, int], int] = {}
    for main_matches in range(7):
        for bonus_match in (0, 1):
            remainder = 6 - main_matches - bonus_match
            if 0 <= remainder <= other:
                count = (
                    comb(6, main_matches)
                    * comb(1, bonus_match)
                    * comb(other, remainder)
                )
                if count:
                    counts[(main_matches, bonus_match)] = count
    assert sum(counts.values()) == comb(pool_size, 6)
    return counts


def full_coverage_six_plus_bonus(
    pool_size: int,
    stake_per_line: float,
    payouts: Mapping[tuple[int, int], float],
    shareable_top_prize: float,
) -> CoverageResult:
    if stake_per_line <= 0:
        raise ValueError("stake_per_line must be positive")
    if shareable_top_prize < 0:
        raise ValueError("shareable_top_prize cannot be negative")
    counts = six_of_n_with_bonus_match_counts(pool_size)
    combinations = comb(pool_size, 6)
    cost = combinations * stake_per_line
    gross = sum(counts.get(key, 0) * value for key, value in payouts.items())
    # For a strict pre-draw cash guarantee, a shareable top prize cannot be
    # credited at its headline amount without a hard cap on external co-winners.
    strict_floor = gross - shareable_top_prize
    return CoverageResult(combinations, cost, gross, strict_floor)


def euromillions_plus_full_coverage(stake_per_line: float = 1.0) -> CoverageResult:
    """Complete 5-of-50 cover for Irish EuroMillions Plus.

    Headline payouts used: 5=EUR500k (shareable/limited), 4=EUR2k, 3=EUR20.
    """
    combinations = comb(50, 5)
    cost = combinations * stake_per_line
    match5 = 1
    match4 = comb(5, 4) * comb(45, 1)
    match3 = comb(5, 3) * comb(45, 2)
    lower = match4 * 2_000 + match3 * 20
    optimistic_gross = 500_000 * match5 + lower
    strict_floor = lower
    return CoverageResult(combinations, cost, optimistic_gross, strict_floor)


def capped_bonus_effective_rebate(required_spend: float, bonus: float) -> float:
    """Face-value rebate fraction at the minimum qualifying spend.

    This is deliberately only a face-value accounting bound. Lottery-only
    bonus funds are not cash and can themselves lose, so they are not a
    guaranteed cash rebate.
    """
    if required_spend <= 0 or bonus < 0:
        raise ValueError("invalid spend/bonus")
    return bonus / required_spend
