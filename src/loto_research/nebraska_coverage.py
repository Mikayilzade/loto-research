from __future__ import annotations

from collections import Counter
from math import comb


def twobytwo_full_space_cash(*, tuesday_double: bool = False) -> tuple[int, int]:
    """Return (cost, optimistic deterministic cash gross) for one 2by2 draw.

    Full space is C(26,2)^2. Free-ticket prizes are assigned zero terminal cash
    value because the replay can legally lose. Grand-prize/set-prize liability
    reductions are ignored, so this is favorable to the player.
    """
    side_overlap = {2: 1, 1: 2 * 24, 0: comb(24, 2)}
    mult = 2 if tuesday_double else 1
    gross = (
        side_overlap[2] * side_overlap[2] * 22_000
        + (side_overlap[2] * side_overlap[1] + side_overlap[1] * side_overlap[2]) * 100
        + (
            side_overlap[2] * side_overlap[0]
            + side_overlap[0] * side_overlap[2]
            + side_overlap[1] * side_overlap[1]
        ) * 3
    ) * mult
    return comb(26, 2) ** 2, gross


def twobytwo_seven_draw_package() -> tuple[int, int, float]:
    """Full-space every draw for a qualifying 7-draw package, including double Tuesday."""
    cost_one, gross_normal = twobytwo_full_space_cash(tuesday_double=False)
    _, gross_tuesday = twobytwo_full_space_cash(tuesday_double=True)
    cost = 7 * cost_one
    gross = 6 * gross_normal + gross_tuesday
    return cost, gross, gross / cost


def valid_myday_dates() -> list[tuple[int, int, int]]:
    """Enumerate valid MM-DD-YY combinations under published MyDaY leap-year rule."""
    result: list[tuple[int, int, int]] = []
    for yy in range(100):
        leap = yy % 4 == 0
        month_days = [31, 29 if leap else 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        for month, days in enumerate(month_days, start=1):
            for day in range(1, days + 1):
                result.append((month, day, yy))
    return result


def myday_full_space_gross_by_winning_date() -> list[tuple[tuple[int, int, int], int]]:
    """Exact cash gross for buying every valid MyDaY date once, for every possible draw."""
    dates = valid_myday_dates()
    count_m = Counter(m for m, d, y in dates)
    count_d = Counter(d for m, d, y in dates)
    count_y = Counter(y for m, d, y in dates)
    count_md = Counter((m, d) for m, d, y in dates)
    count_my = Counter((m, y) for m, d, y in dates)
    count_dy = Counter((d, y) for m, d, y in dates)

    out: list[tuple[tuple[int, int, int], int]] = []
    for m, d, y in dates:
        ab = count_md[(m, d)]
        ac = count_my[(m, y)]
        bc = count_dy[(d, y)]
        n_mdy = 1
        n_dy = bc - 1
        n_my = ac - 1
        n_md = ab - 1
        n_y = count_y[y] - bc - ac + 1
        n_d = count_d[d] - bc - ab + 1
        n_m = count_m[m] - ac - ab + 1
        gross = (
            5000 * n_mdy
            + 365 * n_dy
            + 52 * n_my
            + 12 * n_md
            + 7 * n_y
            + 4 * n_d
            + n_m
        )
        out.append(((m, d, y), gross))
    return out


def pick5_full_space_lower_tier_cash() -> tuple[int, int, int]:
    """Return (space/cost, fixed-table cash excluding jackpot, sole-jackpot hurdle).

    Nebraska Pick 5 is 5/40 at $1. Match-2 free plays have zero terminal cash floor.
    Published 4/5 and 3/5 prizes are treated at face value even though rules allow
    pari-mutuel reduction in unusual circumstances, making this an optimistic bound.
    """
    space = comb(40, 5)
    n4 = comb(5, 4) * comb(35, 1)
    n3 = comb(5, 3) * comb(35, 2)
    lower_cash = n4 * 500 + n3 * 9
    return space, lower_cash, space - lower_cash
