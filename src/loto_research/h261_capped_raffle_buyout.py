import json


def min_exact_cost(ticket_cap, packs):
    # Dynamic programming over exact issued-ticket count.
    dp = [10**30] * (ticket_cap + 1)
    dp[0] = 0
    for n in range(1, ticket_cap + 1):
        for size, price in packs.items():
            if n >= size:
                cand = dp[n - size] + price
                if cand < dp[n]:
                    dp[n] = cand
    return dp[ticket_cap]


raffles = {
    "home_lottery": {
        "cap": 170_000,
        "packs": {1: 100, 3: 250, 5: 375, 10: 700},
        "prize_upper": 6_260_851.86,
        "membership_extra_robustness": 87_986,
    },
    "cash_calendar": {
        "cap": 146_888,
        "packs": {1: 25, 5: 60, 8: 85, 12: 110},
        "prize_upper": 400_000,
    },
    "holiday_for_life": {
        "cap": 239_778,
        "packs": {1: 15, 5: 30, 15: 55, 30: 80},
        "prize_upper": 240_000,
    },
}

for row in raffles.values():
    row["min_full_issuance_cost"] = min_exact_cost(row["cap"], row["packs"])
    row["return"] = row["prize_upper"] / row["min_full_issuance_cost"]
    row["return_pct"] = 100 * row["return"]
    row["deficit"] = row["min_full_issuance_cost"] - row["prize_upper"]
    row["required_discount_break_even"] = 1 - row["return"]
    row["required_discount_break_even_pct"] = 100 * row["required_discount_break_even"]

home = raffles["home_lottery"]
home["return_with_membership_double_counted"] = (
    home["prize_upper"] + home["membership_extra_robustness"]
) / home["min_full_issuance_cost"]

combined_cost = sum(r["min_full_issuance_cost"] for r in raffles.values())
combined_prize = sum(r["prize_upper"] for r in raffles.values())

result = {
    "source": "https://www.homelottery.com.au/terms-and-conditions.html",
    "raffles": raffles,
    "combined": {
        "cost": combined_cost,
        "prize_upper": combined_prize,
        "return": combined_prize / combined_cost,
        "return_pct": 100 * combined_prize / combined_cost,
        "deficit": combined_cost - combined_prize,
    },
    "strict_guaranteed_profit": False,
}

if __name__ == "__main__":
    print(json.dumps(result, indent=2, sort_keys=True))
