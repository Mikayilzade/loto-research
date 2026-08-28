from decimal import Decimal

N = 999_999
PRICE = Decimal("1.29")
PRIZES_WON = 4_761
PRIZES_LEFT = 195_204
FAVOURABLE_PASS_STRESS = 209
DOCUMENTED_INSTANT_TICKETS = 15
END_PRIZE = Decimal("2000")
HEADLINE_INSTANT_VALUE = Decimal("500000")

prize_ids = PRIZES_WON + PRIZES_LEFT
zero_instant_ids = N - prize_ids
full_paid_cost = Decimal(N) * PRICE
headline_liability = HEADLINE_INSTANT_VALUE + END_PRIZE
headline_ratio = headline_liability / full_paid_cost

assert prize_ids == 199_965
assert zero_instant_ids == 800_034
assert zero_instant_ids >= FAVOURABLE_PASS_STRESS
assert zero_instant_ids >= DOCUMENTED_INSTANT_TICKETS
assert full_paid_cost == Decimal("1289998.71")

result = {
    "max_ticket_identifiers": N,
    "ticket_price_gbp": str(PRICE),
    "instant_prizes_won": PRIZES_WON,
    "instant_prizes_left": PRIZES_LEFT,
    "snapshot_prize_identifiers": prize_ids,
    "zero_instant_identifiers": zero_instant_ids,
    "favourable_pass_stress_entries": FAVOURABLE_PASS_STRESS,
    "documented_instant_entries": DOCUMENTED_INSTANT_TICKETS,
    "all_zero_allocation_exists_for_209": zero_instant_ids >= FAVOURABLE_PASS_STRESS,
    "strict_instant_cash_floor_gbp": "0",
    "strict_end_draw_cash_floor_gbp": "0",
    "full_paid_cost_gbp": str(full_paid_cost),
    "headline_liability_stress_gbp": str(headline_liability),
    "headline_ratio": str(headline_ratio),
    "state": "CLOSED / RANDOM-ALLOCATION ZERO-SUPPORT BLOCKED",
}

if __name__ == "__main__":
    import json
    print(json.dumps(result, indent=2, sort_keys=True))
