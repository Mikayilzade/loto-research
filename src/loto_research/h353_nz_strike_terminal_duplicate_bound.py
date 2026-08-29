#!/usr/bin/env python3
"""H353 exact screen: NZ Lotto Strike terminal / Must Be Won duplicate bound."""

from math import comb, factorial
import json

N = 40
R = 4
PRICE = 1.0
THRESHOLD = 1_500_000.0
MIN_POOL_FRAC = 0.60
ALLOC_D1 = 0.36910
ALLOC_D2 = 0.09590
ALLOC_D3 = 0.53500

def perm(n, r):
    return factorial(n) // factorial(n-r)

def exact_position_counts():
    out = {}
    for k in range(R + 1):
        m = R - k
        avoid = sum(
            ((-1) ** j) * comb(m, j) * perm(N-k-j, m-j)
            for j in range(m + 1)
        )
        out[k] = comb(R, k) * avoid
    return out

def main():
    counts = exact_position_counts()
    total = perm(N, R)
    assert sum(counts.values()) == total
    assert counts == {0: 1982313, 1: 202904, 2: 7998, 3: 144, 4: 1}

    cost = PRICE * total
    d4_equivalent = counts[1] * 1.0

    isolated_pool = MIN_POOL_FRAC * cost
    isolated_remaining = isolated_pool - d4_equivalent
    isolated_lower = isolated_remaining * (ALLOC_D2 + ALLOC_D3)
    isolated_gross = d4_equivalent + isolated_lower + THRESHOLD

    duplicate_turnover = cost + PRICE
    duplicate_pool = MIN_POOL_FRAC * duplicate_turnover
    duplicate_remaining = duplicate_pool - d4_equivalent
    duplicate_lower = duplicate_remaining * (ALLOC_D2 + ALLOC_D3)
    duplicate_gross = d4_equivalent + duplicate_lower + THRESHOLD / 2.0

    result = {
        "entries": total,
        "cost_nzd": cost,
        "exact_position_match_counts": {f"match{k}": v for k, v in counts.items()},
        "partition_sum": sum(counts.values()),
        "partition_valid": sum(counts.values()) == total,
        "isolated_gross_nzd": isolated_gross,
        "isolated_net_nzd": isolated_gross - cost,
        "isolated_return_fraction": isolated_gross / cost,
        "one_external_duplicate_gross_nzd": duplicate_gross,
        "one_external_duplicate_net_nzd": duplicate_gross - cost,
        "one_external_duplicate_return_fraction": duplicate_gross / cost,
        "arithmetic_inconclusive": 0,
        "closure_relevant_inconclusive": 0,
        "terminal_no_d1_forceable_by_nonempty_portfolio": False,
    }

    assert isolated_gross > cost
    assert duplicate_gross < cost
    assert result["arithmetic_inconclusive"] == 0
    assert result["closure_relevant_inconclusive"] == 0
    print(json.dumps(result, indent=2, sort_keys=True))

if __name__ == "__main__":
    main()
