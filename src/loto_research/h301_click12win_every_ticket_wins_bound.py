"""H301: exact full-pool face-value bound for Click12Win Every Ticket Wins #3.

This is deliberately player-favourable: all website credit and Amazon eGift Card
are counted at full face value, and the final £750 prize is added in full.
If even that full-pool liability is below acquisition cost, no complete takeover
of this finite pool can guarantee strict positive gross.
"""

TICKETS = 6757
PRICE = 5.00

PRIZES = {
    "cash_500": (2, 500.0),
    "cash_250": (5, 250.0),
    "cash_100": (10, 100.0),
    "cash_50": (20, 50.0),
    "amazon_25": (20, 25.0),
    "credit_10": (200, 10.0),
    "credit_5": (500, 5.0),
    "credit_2": (2000, 2.0),
    "credit_1": (4000, 1.0),
}
FINAL_PRIZE = 750.0

instant_count = sum(n for n, _ in PRIZES.values())
instant_face = sum(n * v for n, v in PRIZES.values())
full_cost = TICKETS * PRICE
full_face_liability = instant_face + FINAL_PRIZE
cash_only_instant = (
    2 * 500.0 + 5 * 250.0 + 10 * 100.0 + 20 * 50.0
)
cash_only_with_final = cash_only_instant + FINAL_PRIZE

assert instant_count == TICKETS
assert instant_face == 17250.0
assert full_cost == 33785.0
assert full_face_liability == 18000.0
assert full_face_liability < full_cost

result = {
    "packet": "H301",
    "candidate": "Click12Win Every Ticket Wins #3 - £18,000 Prize Pool",
    "tickets": TICKETS,
    "price_per_ticket_gbp": PRICE,
    "full_acquisition_cost_gbp": full_cost,
    "instant_prize_count": instant_count,
    "instant_face_value_gbp": instant_face,
    "final_prize_gbp": FINAL_PRIZE,
    "full_player_favourable_face_liability_gbp": full_face_liability,
    "full_face_return_ratio": full_face_liability / full_cost,
    "full_face_deficit_gbp": full_cost - full_face_liability,
    "cash_only_with_final_gbp": cash_only_with_final,
    "cash_only_return_ratio": cash_only_with_final / full_cost,
    "closure": "Even impossible-perfect ownership of every ticket returns <100% at full advertised face value.",
}

if __name__ == "__main__":
    import json
    print(json.dumps(result, indent=2))
