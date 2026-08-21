from math import comb

# Current BCLC base Keno prizes per $1 wager, July 2025 game conditions / 2026 PlayNow page.
PAY = {
    1: {1: 2},
    2: {2: 10},
    3: {3: 25, 2: 2},
    4: {4: 50, 3: 5, 2: 1},
    5: {5: 500, 4: 15, 3: 2},
    6: {6: 1500, 5: 50, 4: 5, 3: 1},
    7: {7: 5000, 6: 150, 5: 15, 4: 2, 3: 1},
    8: {8: 15000, 7: 400, 6: 50, 5: 10, 4: 2},
    9: {9: 25000, 8: 2500, 7: 200, 6: 25, 5: 4, 4: 1},
    10: {10: 200000, 9: 10000, 8: 500, 7: 50, 6: 10, 5: 3, 0: 3},
}


def cover(k: int):
    tickets = comb(80, k)
    gross = 0
    for matched, prize in PAY[k].items():
        gross += comb(20, matched) * comb(60, k - matched) * prize
    ratio = gross / tickets
    free_paid_threshold = 1 / ratio - 1
    return tickets, gross, ratio, free_paid_threshold


def bundle_ratio(base_ratio: float, paid_draws: int, free_draws: int) -> float:
    return base_ratio * (paid_draws + free_draws) / paid_draws


if __name__ == "__main__":
    print("spot,tickets,gross,base_ratio,free_paid_threshold,buy2get1,buy3get2,buy1get1")
    for k in range(1, 11):
        tickets, gross, ratio, threshold = cover(k)
        print(
            f"{k},{tickets},{gross},{ratio:.12f},{threshold:.12f},"
            f"{bundle_ratio(ratio,2,1):.12f},{bundle_ratio(ratio,3,2):.12f},"
            f"{bundle_ratio(ratio,1,1):.12f}"
        )
