from math import comb
from itertools import product


def c(n: int, k: int) -> int:
    return comb(n, k) if n >= k else 0


def doubled_group_payout(group_size: int, draw_hits: int) -> float:
    """Doubled 3-spot payout at $1 stake, assuming $25 for 3/3 and $2.50 for 2/3."""
    n3 = c(draw_hits, 3)
    n2 = c(draw_hits, 2) * (group_size - draw_hits)
    return 50 * n3 + 5 * n2


def evaluate_partition(parts: tuple[int, ...], draw_size: int = 20):
    assert sum(parts) == 80
    plays = sum(c(g, 3) for g in parts)
    worst = None
    worst_alloc = None
    for alloc in product(*[range(min(g, draw_size) + 1) for g in parts]):
        if sum(alloc) != draw_size:
            continue
        gross = sum(doubled_group_payout(g, s) for g, s in zip(parts, alloc))
        if worst is None or gross < worst:
            worst = gross
            worst_alloc = alloc
    return {
        "parts": parts,
        "plays": plays,
        "worst_gross": worst,
        "worst_alloc": worst_alloc,
        "floor_ratio": worst / plays,
        "surplus": worst - plays,
    }


if __name__ == "__main__":
    for parts in [
        (10,) * 8,
        (16,) * 5,
        (20,) * 4,
        (19, 20, 20, 21),
        (19, 19, 21, 21),
        (40, 40),
        (80,),
    ]:
        print(evaluate_partition(parts))
