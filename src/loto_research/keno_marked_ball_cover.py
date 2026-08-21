"""Exact deterministic full-cover formulas for 20-of-80 Keno with marked winning balls.

For a k-Spot full cover we own every k-subset of the 80 numbers.
The ordinary, one-marked-ball (Bulls-Eye), and two-marked-ball
(Double Bulls-Eye) gross payouts are therefore draw-invariant whenever
the prize table is fixed and non-shareable.
"""

from math import comb


def C(n: int, r: int) -> int:
    return comb(n, r) if 0 <= r <= n else 0


def base_full_cover(k: int, base: dict[int, float], stake: float = 1.0):
    tickets = C(80, k)
    gross = sum(base.get(j, 0.0) * C(20, j) * C(60, k-j) for j in range(k+1))
    cost = stake * tickets
    return tickets, cost, gross, gross / cost


def bullseye_full_cover(k: int, base: dict[int, float], bull: dict[int, float], stake: float = 1.0):
    """One distinguished winning ball among the 20 drawn; add-on doubles cost."""
    tickets = C(80, k)
    gross = 0.0
    for j in range(k+1):
        no_mark = C(19, j) * C(60, k-j)
        has_mark = C(19, j-1) * C(60, k-j)
        gross += base.get(j, 0.0) * no_mark + bull.get(j, 0.0) * has_mark
    cost = 2.0 * stake * tickets
    return tickets, cost, gross, gross / cost


def double_bullseye_full_cover(k: int, base: dict[int, float], bull: dict[int, float], double: dict[int, float], stake: float = 1.0):
    """Two distinguished winning balls; add-on triples cost.

    m=0 marked balls -> base table; m=1 -> Bulls-Eye table;
    m=2 -> Double Bulls-Eye table.
    Returned result is nominal and must still be reduced for any liability/share caps.
    """
    tickets = C(80, k)
    gross = 0.0
    for j in range(k+1):
        none = C(18, j) * C(60, k-j)
        one = 2 * C(18, j-1) * C(60, k-j)
        both = C(18, j-2) * C(60, k-j)
        gross += base.get(j, 0.0) * none + bull.get(j, 0.0) * one + double.get(j, 0.0) * both
    cost = 3.0 * stake * tickets
    return tickets, cost, gross, gross / cost
