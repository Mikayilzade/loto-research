from math import inf

POOLS = {
    "chelsea_fire_liberty_street_2026": {
        "currency": "USD", "cap": 250, "ticket_price": 100,
        "prizes": [10000, 2000, 1000, 1000, 500, 500, 500, 500] + [200]*10 + [150]*10 + [100]*5,
    },
    "pacc_st_jude_2026": {
        "currency": "USD", "cap": 500, "ticket_price": 10,
        "prizes": [1500, 1000, 500],
    },
    "henley_great_white_2026": {
        "currency": "AUD", "cap": 500, "ticket_price": 100,
        "prizes": [10000],
    },
}

# Tour de Cure 100 Club: 1/$50, 3/$120, 6/$210; exact cheapest way to buy 100 entries.
def tour_min_cost(n=100):
    best = inf
    best_combo = None
    for six in range(n//6 + 2):
        for three in range(n//3 + 2):
            rem = n - 6*six - 3*three
            if rem < 0:
                continue
            one = rem
            cost = 210*six + 120*three + 50*one
            if cost < best:
                best = cost
                best_combo = (six, three, one)
    return int(best), best_combo


def main():
    results = {}
    for k, p in POOLS.items():
        cost = p["cap"] * p["ticket_price"]
        liabilities = sum(p["prizes"])
        results[k] = {
            "currency": p["currency"],
            "cap": p["cap"],
            "full_acquisition_cost": cost,
            "cash_prize_liabilities": liabilities,
            "gross_ratio": liabilities / cost,
            "deficit": cost - liabilities,
        }

    tour_cost, combo = tour_min_cost(100)
    results["tour_de_cure_100_club_2026"] = {
        "currency": "AUD", "cap": 100,
        "full_acquisition_cost": tour_cost,
        "cash_prize_liabilities": 1500,
        "gross_ratio": 1500 / tour_cost,
        "deficit": tour_cost - 1500,
        "optimal_packages": {"6_for_210": combo[0], "3_for_120": combo[1], "1_for_50": combo[2]},
    }

    assert sum(POOLS["chelsea_fire_liberty_street_2026"]["prizes"]) == 20000
    assert results["chelsea_fire_liberty_street_2026"]["gross_ratio"] == 0.8
    assert results["pacc_st_jude_2026"]["gross_ratio"] == 0.6
    assert results["henley_great_white_2026"]["gross_ratio"] == 0.2
    assert tour_cost == 3530 and combo == (16, 1, 1)
    assert all(v["gross_ratio"] < 1 for v in results.values())

    import json
    print(json.dumps({"packet": "H298", "results": results}, indent=2))

if __name__ == "__main__":
    main()
