from math import comb

PAYOUTS = {
    1: {1: 2},
    2: {2: 10},
    3: {2: 2, 3: 25},
    4: {2: 1, 3: 5, 4: 60},
    5: {3: 2, 4: 20, 5: 330},
    6: {3: 1, 4: 6, 5: 55, 6: 1000},
    7: {3: 1, 4: 2, 5: 15, 6: 100, 7: 5000},
    8: {4: 2, 5: 6, 6: 75, 7: 550, 8: 10000},
    9: {4: 1, 5: 5, 6: 20, 7: 125, 8: 3000, 9: 30000},
    10: {0: 5, 5: 2, 6: 10, 7: 45, 8: 300, 9: 5000, 10: 100000},
}


def hit_count(spot: int, hits: int) -> int:
    return comb(20, hits) * comb(60, spot - hits)


def evaluate_spot(spot: int) -> dict:
    tickets = comb(80, spot)
    base_gross = 0.0
    universal_50_gross = 0.0
    official_exclusion_upper_gross = 0.0

    for hits, prize in PAYOUTS[spot].items():
        count = hit_count(spot, hits)
        base_gross += count * prize
        universal_50_gross += count * prize * 1.5

        eligible_for_increase = prize >= 2 and not (spot == 10 and hits == 10)
        multiplier = 1.5 if eligible_for_increase else 1.0
        official_exclusion_upper_gross += count * prize * multiplier

    return {
        "spot": spot,
        "full_space_lines": tickets,
        "base_gross_per_full_cover": base_gross,
        "base_return": base_gross / tickets,
        "universal_50_upper_gross": universal_50_gross,
        "universal_50_upper_return": universal_50_gross / tickets,
        "official_exclusion_upper_gross": official_exclusion_upper_gross,
        "official_exclusion_upper_return": official_exclusion_upper_gross / tickets,
        "required_10_draw_spend": tickets * 10,
        "required_10_draw_universal_50_upper_gross": universal_50_gross * 10,
        "required_10_draw_universal_50_net": (universal_50_gross - tickets) * 10,
    }


def main() -> None:
    rows = [evaluate_spot(s) for s in range(1, 11)]
    best = max(rows, key=lambda r: r["universal_50_upper_return"])
    assert best["universal_50_upper_return"] < 1.0
    for row in rows:
        print(row)
    print("best_upper_bound", best)


if __name__ == "__main__":
    main()
