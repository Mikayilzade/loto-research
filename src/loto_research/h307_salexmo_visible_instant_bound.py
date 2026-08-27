"""H307 exact worst-case bound for Salexmo visible instant-win identifiers.

The checked competition publicly lists remaining instant-win ticket numbers, but
Salexmo Terms §4.1(B) randomly allocate entry numbers only after completion and
payment.  This script verifies that the remaining non-instant inventory is large
enough to absorb the entire per-user cap, so the strict instant-win cash floor is
zero.
"""

TOTAL_ENTRIES = 40_000
SOLD = 5_583
REMAINING = TOTAL_ENTRIES - SOLD
TOTAL_INSTANTS = 10
INSTANTS_REMAINING = 9
MAX_PER_USER = 10_000
TICKET_PRICE_GBP = 0.03
INSTANT_PRIZE_GBP = 30.0

NON_INSTANT_REMAINING_LOWER_BOUND = REMAINING - INSTANTS_REMAINING
MAX_PAID_SPEND_GBP = MAX_PER_USER * TICKET_PRICE_GBP

assert REMAINING == 34_417
assert NON_INSTANT_REMAINING_LOWER_BOUND == 34_408
assert NON_INSTANT_REMAINING_LOWER_BOUND >= MAX_PER_USER
assert MAX_PAID_SPEND_GBP == 300.0

RESULT = {
    "packet": "H307",
    "candidate": "Salexmo £300 CASH FOR 3P, PLUS CASH INSTANT WINS 11/9/26",
    "total_entries": TOTAL_ENTRIES,
    "sold_snapshot": SOLD,
    "remaining_snapshot": REMAINING,
    "instant_wins_total": TOTAL_INSTANTS,
    "instant_wins_remaining_snapshot": INSTANTS_REMAINING,
    "non_instant_remaining_lower_bound": NON_INSTANT_REMAINING_LOWER_BOUND,
    "max_entries_per_user": MAX_PER_USER,
    "ticket_price_gbp": TICKET_PRICE_GBP,
    "instant_prize_gbp": INSTANT_PRIZE_GBP,
    "max_paid_spend_gbp": MAX_PAID_SPEND_GBP,
    "allocation_rule": "random entry number on completion/payment",
    "legal_all_noninstant_allocation_exists": True,
    "strict_instant_win_cash_floor_gbp": 0.0,
    "main_draw_strict_floor_gbp": 0.0,
    "strict_total_cash_floor_gbp": 0.0,
    "closure": "TARGETING_BLOCKED",
}

if __name__ == "__main__":
    import json
    print(json.dumps(RESULT, indent=2))
