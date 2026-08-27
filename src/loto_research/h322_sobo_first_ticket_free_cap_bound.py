"""H322: SOBO Instant Win Frenzy deterministic-floor bound.

Reproducible arithmetic only. Source facts are documented in
research/h322_sobo_first_ticket_free_cap_bound.md.
"""

TOTAL_TICKETS = 500_000
CURRENT_SOLD = 1
MAX_PER_PERSON = 2_000
TICKET_PRICE_GBP = 0.29
FREE_TICKETS_PER_PERSON = 1
ADVERTISED_INSTANT_CREDIT_IDS = 50_000
ADVERTISED_CASH_PRIZES = 5
CASH_PRIZE_GBP = 1_000

# Player-favourable assumption: every advertised instant-credit prize and every
# cash prize uses a distinct identifier. This maximizes the number of
# prize-bearing IDs and minimizes the residual no-instant set.
MAX_PRIZE_BEARING_IDS = ADVERTISED_INSTANT_CREDIT_IDS + ADVERTISED_CASH_PRIZES
MIN_ZERO_INSTANT_IDS = TOTAL_TICKETS - MAX_PRIZE_BEARING_IDS

assert MAX_PRIZE_BEARING_IDS == 50_005
assert MIN_ZERO_INSTANT_IDS == 449_995
assert MIN_ZERO_INSTANT_IDS >= MAX_PER_PERSON
assert MAX_PER_PERSON < TOTAL_TICKETS

# One free ticket only reduces acquisition cost; it cannot eliminate the legal
# allocation in which all of the player's <=2,000 randomly allocated tickets
# fall in the residual zero-instant set.
MAX_PAID_TICKETS_AT_CAP = MAX_PER_PERSON - FREE_TICKETS_PER_PERSON
MAX_CAP_SPEND_GBP = MAX_PAID_TICKETS_AT_CAP * TICKET_PRICE_GBP

RESULT = {
    "packet": "H322",
    "total_tickets": TOTAL_TICKETS,
    "current_sold_snapshot": CURRENT_SOLD,
    "max_per_person": MAX_PER_PERSON,
    "ticket_price_gbp": TICKET_PRICE_GBP,
    "free_tickets_per_person": FREE_TICKETS_PER_PERSON,
    "advertised_instant_credit_ids": ADVERTISED_INSTANT_CREDIT_IDS,
    "advertised_cash_prizes": ADVERTISED_CASH_PRIZES,
    "max_prize_bearing_ids_player_favourable": MAX_PRIZE_BEARING_IDS,
    "min_zero_instant_ids": MIN_ZERO_INSTANT_IDS,
    "residual_zero_ids_cover_player_cap": MIN_ZERO_INSTANT_IDS >= MAX_PER_PERSON,
    "max_paid_tickets_at_cap": MAX_PAID_TICKETS_AT_CAP,
    "max_cap_spend_gbp": round(MAX_CAP_SPEND_GBP, 2),
    "strict_withdrawable_cash_floor_gbp": 0,
    "state": "CLOSED / CAP-AND-RANDOM-ALLOCATION-BLOCKED",
}

if __name__ == "__main__":
    import json
    print(json.dumps(RESULT, indent=2, sort_keys=True))
