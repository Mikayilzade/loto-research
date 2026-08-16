from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class BullseyeCoverage:
    draws: int
    selections: int
    cost_nzd: float
    standard_cost_nzd: float
    discount_fraction: float
    div1_per_draw: int
    div2_per_draw: int
    div3_per_draw: int
    div4_per_draw: int
    div5_per_draw: int
    div6_per_draw: int


def winning_counts_per_full_space_draw() -> dict[int, int]:
    """Exact Bullseye winning-selection counts when all 000000..999999 are owned once.

    The number space is circular. Divisions are exact winning number; +/-1..5;
    +/-6..50; +/-51..500; +/-501..5000; +/-5001..50000.
    """
    return {1: 1, 2: 10, 3: 90, 4: 900, 5: 9_000, 6: 90_000}


def multidraw_cost(draws: int, selections: int = 1_000_000) -> float:
    if draws <= 0 or selections <= 0:
        raise ValueError("draws and selections must be positive")
    if draws == 7:
        return selections * 10.0
    if draws == 14:
        return selections * 20.0
    return selections * 2.0 * draws


def full_space_coverage(draws: int) -> BullseyeCoverage:
    selections = 1_000_000
    standard = selections * 2.0 * draws
    cost = multidraw_cost(draws, selections)
    counts = winning_counts_per_full_space_draw()
    return BullseyeCoverage(
        draws=draws,
        selections=selections,
        cost_nzd=cost,
        standard_cost_nzd=standard,
        discount_fraction=1.0 - cost / standard,
        div1_per_draw=counts[1],
        div2_per_draw=counts[2],
        div3_per_draw=counts[3],
        div4_per_draw=counts[4],
        div5_per_draw=counts[5],
        div6_per_draw=counts[6],
    )


def strict_cash_guarantee_possible_with_unbounded_external_duplicates() -> bool:
    """Necessary-condition result for the current pari-mutuel structure.

    Divisions 1-5 are shared when multiple winning selections exist; division 2
    also has a 250k total cap. Without a useful pre-draw hard cap on external
    duplicate winning selections, a full-space owner's cash share can be made
    arbitrarily small. Division 6 is a bonus ticket rather than guaranteed cash.
    Therefore positive cash profit cannot be guaranteed from coverage alone.
    """
    return False
