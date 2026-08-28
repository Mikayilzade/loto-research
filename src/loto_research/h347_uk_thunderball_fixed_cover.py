from math import comb

MAIN_N = 39
MAIN_PICK = 5
THUNDERBALL_N = 14
LINE_PRICE_GBP = 1

PRIZE_GBP = {
    (5, True): 500_000,
    (5, False): 5_000,
    (4, True): 250,
    (4, False): 100,
    (3, True): 20,
    (3, False): 10,
    (2, True): 10,
    (1, True): 5,
    (0, True): 3,
}


def category_count(main_matches: int, thunderball_match: bool) -> int:
    main_selections = comb(MAIN_PICK, main_matches) * comb(
        MAIN_N - MAIN_PICK, MAIN_PICK - main_matches
    )
    return main_selections * (1 if thunderball_match else THUNDERBALL_N - 1)


def solve() -> dict:
    universe = comb(MAIN_N, MAIN_PICK) * THUNDERBALL_N
    rows = []
    counted = 0
    gross = 0

    for main_matches in range(MAIN_PICK, -1, -1):
        for thunderball_match in (True, False):
            count = category_count(main_matches, thunderball_match)
            prize = PRIZE_GBP.get((main_matches, thunderball_match), 0)
            category_gross = count * prize
            rows.append(
                {
                    "main_matches": main_matches,
                    "thunderball_match": thunderball_match,
                    "count": count,
                    "prize_gbp": prize,
                    "gross_gbp": category_gross,
                }
            )
            counted += count
            gross += category_gross

    cost = universe * LINE_PRICE_GBP
    deficit = cost - gross

    assert universe == 8_060_598
    assert counted == universe
    assert gross == 4_262_568
    assert cost == 8_060_598
    assert deficit == 3_798_030
    assert gross < cost

    return {
        "matrix": "5/39 + 1/14 Thunderball",
        "universe_lines": universe,
        "line_price_gbp": LINE_PRICE_GBP,
        "full_cover_cost_gbp": cost,
        "advertised_fixed_prize_full_cover_gross_gbp": gross,
        "deficit_gbp": deficit,
        "return_ratio": gross / cost,
        "return_percent": 100 * gross / cost,
        "category_count_sum": counted,
        "arithmetic_inconclusive": 0,
        "closure": "advertised fixed-prize full cover is strictly below cost; any prize-cap reduction cannot improve the floor",
        "categories": rows,
    }


if __name__ == "__main__":
    import json

    print(json.dumps(solve(), indent=2))
