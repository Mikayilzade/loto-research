"""H350: Irish Lotto Plus Raffle additive-subsidy exact bound.

This packet isolates the raffle subsidy. It deliberately grants an impossible-favourable
balanced acquisition of Lotto Plus raffle codes before applying external-owner dilution.
"""
CODE_COUNT = 10_000
RAFFLE_FIXED_EUR = 500
PLUS_COST_PER_PLAY_EUR = 1
SPECIAL_POOL_EUR = 1_000_000

def ordinary_best_guaranteed_upper_bound(n_plays: int):
    """Upper-bound the minimum ordinary raffle payout across all 10,000 winning codes."""
    q, r = divmod(n_plays, CODE_COUNT)
    gross = RAFFLE_FIXED_EUR * q
    addon_cost = PLUS_COST_PER_PLAY_EUR * n_plays
    return {
        "plays": n_plays,
        "full_code_cycles": q,
        "remainder": r,
        "ordinary_worst_code_gross_upper_eur": gross,
        "plus_addon_cost_eur": addon_cost,
        "ordinary_net_upper_eur": gross - addon_cost,
    }

def main():
    assert RAFFLE_FIXED_EUR < CODE_COUNT * PLUS_COST_PER_PLAY_EUR
    probes = [1, 9_999, 10_000, 10_001, 20_000, 100_000, 15_339_390]
    for n in probes:
        row = ordinary_best_guaranteed_upper_bound(n)
        assert row["ordinary_net_upper_eur"] < 0
        print(row)

    nonnegative = 0
    max_net = None
    max_net_n = None
    for n in range(1, 2_000_001):
        net = ordinary_best_guaranteed_upper_bound(n)["ordinary_net_upper_eur"]
        if max_net is None or net > max_net:
            max_net, max_net_n = net, n
        if net >= 0:
            nonnegative += 1

    assert nonnegative == 0
    print({
        "scan_plays": 2_000_000,
        "nonnegative_ordinary_cases": nonnegative,
        "max_ordinary_net_upper_eur": max_net,
        "max_at_n": max_net_n,
        "complete_cycle_return_ratio_on_plus_addon": RAFFLE_FIXED_EUR / (CODE_COUNT * PLUS_COST_PER_PLAY_EUR),
        "arithmetic_inconclusive": 0,
        "closure_relevant_inconclusive": 0,
    })

if __name__ == "__main__":
    main()
