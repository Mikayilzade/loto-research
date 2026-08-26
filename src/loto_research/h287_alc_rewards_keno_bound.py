"""H287: Atlantic Lottery AL Rewards + KENO Atlantic deterministic-subsidy bound.

Uses the published 20-of-70 KENO Atlantic paytable for spot sizes 2..10.
For each fixed spot size, symmetry makes every selection have the same
average gross. Therefore any nonnegative portfolio made from those selections
has minimum legal-outcome gross <= its average gross.

AL Rewards is granted a player-favourable upper bound of 6 points per $1 cash
spend and redeems at 1000 points = $1 Promo Cash. Promo-Cash-funded purchases
do not earn points, so the one-step extra playable balance factor is <=1.006.
"""
from fractions import Fraction
from math import comb
import json

N = 70
DRAWN = 20
POINTS_PER_DOLLAR_UPPER = 6
POINTS_PER_PROMO_DOLLAR = 1000
PROMO_FACTOR = Fraction(POINTS_PER_PROMO_DOLLAR + POINTS_PER_DOLLAR_UPPER,
                        POINTS_PER_PROMO_DOLLAR)

PAYTABLE = {
    2: {2: 7},
    3: {3: 25},
    4: {4: 75, 3: 2},
    5: {5: 250, 4: 10},
    6: {6: 1000, 5: 25, 4: 2},
    7: {7: 5000, 6: 100, 5: 5},
    8: {8: 25000, 7: 200, 6: 10, 5: 2},
    9: {9: 50000, 8: 1000, 7: 100, 6: 5, 5: 2},
    10: {10: 250000, 9: 5000, 8: 200, 7: 25, 6: 5, 0: 2},
}


def match_probability(k: int, m: int) -> Fraction:
    return Fraction(comb(DRAWN, m) * comb(N - DRAWN, k - m), comb(N, k))


def expected_gross(k: int) -> Fraction:
    return sum((Fraction(prize) * match_probability(k, m)
                for m, prize in PAYTABLE[k].items()), Fraction(0))


def build_result():
    rows = []
    for k in sorted(PAYTABLE):
        ev = expected_gross(k)
        boosted = ev * PROMO_FACTOR
        rows.append({
            "spot": k,
            "base_average_gross_per_1_dollar": float(ev),
            "base_average_percent": float(ev * 100),
            "rewards_upper_bound_average_gross_per_cash_dollar": float(boosted),
            "rewards_upper_bound_percent": float(boosted * 100),
            "exact_base_fraction": f"{ev.numerator}/{ev.denominator}",
        })
    best = max(rows, key=lambda r: r["rewards_upper_bound_average_gross_per_cash_dollar"])
    assert best["spot"] == 7
    assert best["rewards_upper_bound_average_gross_per_cash_dollar"] < 1.0
    return {
        "packet": "H287",
        "mechanism": "Atlantic Lottery AL Rewards Promo Cash applied to KENO Atlantic fixed-pay selections",
        "keno_universe": {"numbers": N, "drawn": DRAWN, "spots_checked": list(range(2, 11))},
        "rewards_player_favourable_upper_bound": {
            "points_per_cash_dollar": POINTS_PER_DOLLAR_UPPER,
            "points_per_1_dollar_promo_cash": POINTS_PER_PROMO_DOLLAR,
            "extra_playable_balance_fraction": float(PROMO_FACTOR - 1),
            "total_playable_factor": float(PROMO_FACTOR),
            "promo_cash_spend_earns_points": False,
        },
        "rows": rows,
        "best_spot": best["spot"],
        "best_base_average_percent": best["base_average_percent"],
        "best_rewards_upper_bound_percent": best["rewards_upper_bound_percent"],
        "strict_profit_possible_under_checked_additive_class": False,
        "proof": "For each symmetric fixed-pay selection class, minimum legal-outcome gross <= average gross. Any nonnegative mixture is bounded by the maximum class average. Even granting 6 points/$ and spending all resulting Promo Cash, the maximum is below cash cost.",
    }


if __name__ == "__main__":
    print(json.dumps(build_result(), indent=2))
