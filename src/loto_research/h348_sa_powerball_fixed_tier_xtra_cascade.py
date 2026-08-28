from math import comb

MAIN_N = 50
PICK = 5
PB_N = 16
MAIN_PRICE = 10
XTRA_PRICE = 5

MAIN_FIXED = {
    (4, False): 2000,
    (3, True): 500,
    (3, False): 100,
    (2, True): 100,
    (1, True): 20,
    (0, True): 10,
}


def cell_count(k: int, pb_hit: bool) -> int:
    main = comb(PICK, k) * comb(MAIN_N - PICK, PICK - k)
    return main if pb_hit else main * (PB_N - 1)


def compute():
    cells = {(k, pb): cell_count(k, pb) for k in range(PICK + 1) for pb in (True, False)}
    total = comb(MAIN_N, PICK) * PB_N
    assert sum(cells.values()) == total

    fixed_gross = sum(cells[key] * prize for key, prize in MAIN_FIXED.items())
    main_cost = total * MAIN_PRICE
    xtra_fixed_gross = fixed_gross // 2
    xtra_cost = total * XTRA_PRICE
    assert fixed_gross % 2 == 0
    assert fixed_gross * xtra_cost == xtra_fixed_gross * main_cost

    return {
        "legal_boards": total,
        "partition_sum": sum(cells.values()),
        "cells": {f"k{k}_pb{int(pb)}": n for (k, pb), n in sorted(cells.items())},
        "main_fixed_gross": fixed_gross,
        "main_cost": main_cost,
        "main_fixed_return": fixed_gross / main_cost,
        "xtra_fixed_gross": xtra_fixed_gross,
        "xtra_cost": xtra_cost,
        "combined_fixed_gross": fixed_gross + xtra_fixed_gross,
        "combined_cost": main_cost + xtra_cost,
        "combined_fixed_return": (fixed_gross + xtra_fixed_gross) / (main_cost + xtra_cost),
        "arithmetic_inconclusive": 0,
        "closure_relevant_inconclusive": 0,
        "cascade_forcible_by_nonempty_portfolio": False,
    }


if __name__ == "__main__":
    import json
    print(json.dumps(compute(), indent=2, sort_keys=True))
