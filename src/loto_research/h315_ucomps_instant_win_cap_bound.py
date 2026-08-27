"""H315: U Comps current £50,000 instant-win competition strict one-player floor bound.

Snapshot date: 2026-08-27.
The live page reports 175,000 total tickets, 38,626 sold, 167 instant-win
identifiers of which 137 remain available, and a per-person cap of 500.

If ticket identifiers are allocated only after successful purchase rather than
reserved/selected beforehand, the remaining non-instant inventory alone is
large enough to absorb every ticket one player may buy. Therefore a legal
allocation exists with zero instant-win cash for that player. A separate final
draw also cannot create a positive worst-case floor because the player cannot
own all eligible identifiers.
"""

TOTAL = 175_000
SOLD = 38_626
INSTANT_TOTAL = 167
INSTANT_REMAINING = 137
PLAYER_CAP = 500
PRICE = 0.49
MAX_BUNDLE_DISCOUNT = 0.24

remaining = TOTAL - SOLD
remaining_noninstant_lower_bound = remaining - INSTANT_REMAINING
max_paid_cost_at_500_discounted = PLAYER_CAP * PRICE * (1 - MAX_BUNDLE_DISCOUNT)

assert remaining == 136_374
assert remaining_noninstant_lower_bound == 136_237
assert remaining_noninstant_lower_bound >= PLAYER_CAP
assert PLAYER_CAP < TOTAL
assert max_paid_cost_at_500_discounted == 186.2

RESULT = {
    "packet": "H315",
    "snapshot_date": "2026-08-27",
    "total_tickets": TOTAL,
    "tickets_sold": SOLD,
    "tickets_remaining": remaining,
    "instant_win_identifiers_total": INSTANT_TOTAL,
    "instant_win_identifiers_remaining": INSTANT_REMAINING,
    "remaining_noninstant_identifiers_lower_bound": remaining_noninstant_lower_bound,
    "max_entries_per_person": PLAYER_CAP,
    "base_ticket_price_gbp": PRICE,
    "max_bundle_discount_fraction": MAX_BUNDLE_DISCOUNT,
    "discounted_500_ticket_cost_gbp": max_paid_cost_at_500_discounted,
    "strict_instant_win_cash_floor_gbp": 0,
    "strict_total_cash_floor_gbp": 0,
    "closure_reason": "CAP_AND_POST_PURCHASE_ALLOCATION_BLOCK_FULL_CONTROL",
}

if __name__ == "__main__":
    import json
    print(json.dumps(RESULT, indent=2))
