from math import comb

PAY = {
    1: {1: 2},
    2: {2: 11},
    3: {2: 2, 3: 27},
    4: {2: 1, 3: 5, 4: 72},
    5: {3: 2, 4: 18, 5: 410},
    6: {3: 1, 4: 7, 5: 57, 6: 1100},
    7: {3: 1, 4: 5, 5: 11, 6: 100, 7: 2000},
    8: {4: 2, 5: 15, 6: 50, 7: 300, 8: 10000},
    9: {4: 2, 5: 5, 6: 20, 7: 100, 8: 2000, 9: 25000},
    10: {0: 5, 5: 2, 6: 10, 7: 50, 8: 500, 9: 5000, 10: 100000},
}


def full_cover_ratio(k: int) -> tuple[int, int, float]:
    spend = comb(80, k)
    gross = sum(
        comb(20, j) * comb(60, k - j) * prize
        for j, prize in PAY[k].items()
        if 0 <= j <= 20 and 0 <= k - j <= 60
    )
    return spend, gross, gross / spend


def promoted_ratio(base_ratio: float, addon_cost_multiple: float, minimum_multiplier: float) -> float:
    return minimum_multiplier * base_ratio / (1 + addon_cost_multiple)


if __name__ == "__main__":
    print("spot,base_spend,base_gross,base_ratio,double_booster_floor")
    for k in range(1, 11):
        spend, gross, ratio = full_cover_ratio(k)
        floor = promoted_ratio(ratio, addon_cost_multiple=1.0, minimum_multiplier=2.0)
        print(f"{k},{spend},{gross},{ratio:.9f},{floor:.9f}")
