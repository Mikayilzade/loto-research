from math import comb

PRICE = 2.50
PRIZE_FUND_PER_PLAY = 1.30
RESERVE_SHARE = 0.4521
BOOST_T1 = 30_000 * 12 * 30
T2 = 2_000 * 12 * 5
T6 = 2.50


def solve():
    main = comb(40, 6)
    plays = main * 5
    cost = plays * PRICE

    partition = {
        k: comb(6, k) * comb(34, 6 - k) * 5
        for k in range(7)
    }
    assert sum(partition.values()) == plays
    assert partition[6] == 5

    own_t1 = 1
    own_t2 = 4
    tier6_winners = partition[2]

    prize_fund = plays * PRIZE_FUND_PER_PLAY
    reserve = prize_fund * RESERVE_SHARE
    tier6_gross = tier6_winners * T6
    variable_pool = prize_fund - reserve - tier6_gross

    isolated_boost_gross = (
        own_t1 * BOOST_T1
        + own_t2 * T2
        + tier6_gross
        + variable_pool
    )
    net = isolated_boost_gross - cost
    ret = isolated_boost_gross / cost

    assert plays == 19_191_900
    assert tier6_winners == 3_478_200
    assert abs(prize_fund - 24_949_470.0) < 1e-9
    assert abs(variable_pool - 4_974_314.613) < 1e-6
    assert ret < 1.0

    return {
        "main_combinations": main,
        "plays": plays,
        "cost_eur": cost,
        "partition_by_main_matches": partition,
        "own_tier1_winners": own_t1,
        "own_tier2_winners": own_t2,
        "tier6_winners": tier6_winners,
        "prize_fund_eur": prize_fund,
        "reserve_eur": reserve,
        "tier6_gross_eur": tier6_gross,
        "variable_pool_eur": variable_pool,
        "isolated_boost_gross_eur": isolated_boost_gross,
        "net_eur": net,
        "return_ratio": ret,
        "arithmetic_inconclusive": 0,
        "closure_relevant_inconclusive": 0,
        "closed": ret < 1.0,
    }


if __name__ == "__main__":
    import json
    print(json.dumps(solve(), indent=2, sort_keys=True))
