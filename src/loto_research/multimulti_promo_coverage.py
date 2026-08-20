from math import comb

NORMAL = {
    1: {1: 4},
    2: {2: 16},
    3: {3: 54, 2: 2},
    4: {4: 84, 3: 8, 2: 2},
    5: {5: 700, 4: 20, 3: 4},
    6: {6: 1300, 5: 120, 4: 8, 3: 2},
    7: {7: 6000, 6: 200, 5: 20, 4: 4, 3: 2},
    8: {8: 22000, 7: 600, 6: 60, 5: 20, 4: 4},
    9: {9: 70000, 8: 2000, 7: 300, 6: 42, 5: 8, 4: 2},
    10: {10: 250000, 9: 10000, 8: 520, 7: 140, 6: 12, 5: 4, 4: 2},
}

PLUS = {
    1: {1: 88},
    2: {2: 120, 1: 24},
    3: {3: 214, 2: 28, 1: 18},
    4: {4: 384, 3: 48, 2: 16, 1: 16},
    5: {5: 1800, 4: 80, 3: 20, 2: 10, 1: 14},
    6: {6: 4300, 5: 320, 4: 20, 3: 12, 2: 10, 1: 14},
    7: {7: 22000, 6: 700, 5: 70, 4: 14, 3: 8, 2: 8, 1: 14},
    8: {8: 130000, 7: 1800, 6: 180, 5: 48, 4: 14, 3: 4, 2: 4, 1: 14},
    9: {9: 300000, 8: 10000, 7: 900, 6: 122, 5: 22, 4: 6, 3: 4, 2: 4, 1: 14},
    10: {10: 2500000, 9: 50000, 8: 1520, 7: 380, 6: 36, 5: 12, 4: 6, 3: 4, 2: 4, 1: 10},
}


def no_plus_return(k: int, promo_multiplier: float = 1.0) -> float:
    tickets = comb(80, k)
    gross = 0.0
    for hits, prize in NORMAL[k].items():
        count = comb(20, hits) * comb(60, k - hits)
        gross += count * prize * promo_multiplier
    return gross / (tickets * 2.5)


def plus_return(k: int, promo_multiplier: float = 1.0) -> float:
    tickets = comb(80, k)
    gross = 0.0
    for hits in range(k + 1):
        no_plus_count = comb(19, hits) * comb(60, k - hits) if hits <= 19 else 0
        plus_count = comb(19, hits - 1) * comb(60, k - hits) if hits >= 1 else 0
        gross += no_plus_count * NORMAL[k].get(hits, 0) * promo_multiplier
        gross += plus_count * PLUS[k].get(hits, 0) * promo_multiplier
    return gross / (tickets * 5.0)


def screen(multiplier: float = 1.5):
    return [
        {
            "k": k,
            "combinations": comb(80, k),
            "no_plus_base": no_plus_return(k),
            "no_plus_promo": no_plus_return(k, multiplier),
            "plus_base": plus_return(k),
            "plus_promo": plus_return(k, multiplier),
        }
        for k in range(1, 11)
    ]


if __name__ == "__main__":
    for row in screen():
        print(row)
