from math import comb
import json

PAYTABLE = {
    1: {1: 2},
    2: {2: 11},
    3: {3: 27, 2: 2},
    4: {4: 72, 3: 5, 2: 1},
    5: {5: 410, 4: 18, 3: 2},
    6: {6: 1100, 5: 57, 4: 7, 3: 1},
    7: {7: 2000, 6: 100, 5: 11, 4: 5, 3: 1},
    8: {8: 10000, 7: 300, 6: 50, 5: 15, 4: 2},
    9: {9: 25000, 8: 2000, 7: 100, 6: 20, 5: 5, 4: 2},
    10: {10: 250000, 9: 2500, 8: 250, 7: 25, 6: 7, 5: 2, 0: 5},
}


def full_coverage_row(spot: int):
    combinations = comb(80, spot)
    base_gross = sum(
        comb(20, hits) * comb(60, spot - hits) * prize
        for hits, prize in PAYTABLE[spot].items()
    )
    base_return = base_gross / combinations
    return {
        "spot": spot,
        "combinations": combinations,
        "base_gross": base_gross,
        "base_return": base_return,
        "universal_doubler_gross": 2 * base_gross,
        "universal_doubler_return": 2 * base_return,
        "universal_tripler_gross": 3 * base_gross,
        "universal_tripler_return": 3 * base_return,
        "base_net": base_gross - combinations,
        "universal_doubler_net": 2 * base_gross - combinations,
        "universal_tripler_net": 3 * base_gross - combinations,
    }


def main():
    result = {
        "game": "Michigan Club Keno",
        "draw_model": "20 of 80",
        "wager_per_line": 1,
        "rows": [full_coverage_row(k) for k in range(1, 11)],
        "guarantee_gate": {
            "promotion_entitlement": "random printed Doubler/Tripler message",
            "deterministic_entitlement_proven": False,
            "post_print_reject_refund_right_proven": False,
            "strict_guarantee": False,
        },
    }
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
