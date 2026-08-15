from __future__ import annotations

from math import comb


def euromillions_space() -> int:
    return comb(50, 5) * comb(12, 2)


def full_space_cost(price_per_line: float = 2.50) -> float:
    return euromillions_space() * price_per_line


def category_count(main_matches: int, star_matches: int) -> int:
    if not 0 <= main_matches <= 5:
        raise ValueError("main_matches must be 0..5")
    if not 0 <= star_matches <= 2:
        raise ValueError("star_matches must be 0..2")
    return (
        comb(5, main_matches)
        * comb(45, 5 - main_matches)
        * comb(2, star_matches)
        * comb(10, 2 - star_matches)
    )


def prize_category_counts() -> dict[tuple[int, int], int]:
    categories = [
        (5, 2), (5, 1), (5, 0), (4, 2), (4, 1), (3, 2), (4, 0),
        (2, 2), (3, 1), (3, 0), (1, 2), (2, 1), (2, 0),
    ]
    return {category: category_count(*category) for category in categories}


def full_coverage_forces_jackpot_winner() -> bool:
    """Every possible 5+2 outcome is in a complete-space portfolio exactly once."""
    return category_count(5, 2) == 1


def terminal_cap_rolldown_compatible_with_full_coverage() -> bool:
    """Terminal EuroMillions rolldown requires no jackpot winner.

    Complete coverage forces at least one jackpot winner, so both conditions
    cannot hold in the same draw.
    """
    return not full_coverage_forces_jackpot_winner()
