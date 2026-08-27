"""H316: Punter Prizes postal-bundle no-subsidy bound.

Current CASH DASH 3 snapshot (2026-08-27): 20,000 tickets at GBP 0.10,
10 x GBP100 cash instant wins plus 10 x GBP100 ticket bundles, no end prize.
The free-entry route credits multiple entries per separately-posted letter only up
to the value of second-class postage.  With current GBP0.91 postage, a GBP0.10
competition gives at most floor(0.91/0.10)=9 entries per postal letter.
"""
from math import ceil, floor
import json

TICKET_PRICE = 0.10
POOL = 20_000
POSTAGE = 0.91
CASH_PRIZES = 10 * 100
BUNDLE_FACE = 10 * 100
TOTAL_FACE = CASH_PRIZES + BUNDLE_FACE
SOLD = 1_811
REMAINING = 18_189
REMAINING_CASH_FACE = 9 * 100
REMAINING_BUNDLE_FACE = 9 * 100
REMAINING_FACE = REMAINING_CASH_FACE + REMAINING_BUNDLE_FACE

entries_per_letter = floor(POSTAGE / TICKET_PRICE)
assert entries_per_letter == 9

paid_full_cost = POOL * TICKET_PRICE
postal_letters_full = ceil(POOL / entries_per_letter)
postal_full_cost = postal_letters_full * POSTAGE

paid_remaining_cost = REMAINING * TICKET_PRICE
postal_letters_remaining = ceil(REMAINING / entries_per_letter)
postal_remaining_cost = postal_letters_remaining * POSTAGE

assert abs(paid_full_cost - 2000.0) < 1e-9
assert abs(TOTAL_FACE - 2000.0) < 1e-9
assert postal_full_cost > TOTAL_FACE
assert paid_full_cost == TOTAL_FACE
assert postal_remaining_cost > REMAINING_FACE
assert paid_remaining_cost > REMAINING_FACE

out = {
    "packet": "H316",
    "snapshot_date": "2026-08-27",
    "competition": "Punter Prizes CASH DASH 3",
    "ticket_price_gbp": TICKET_PRICE,
    "ticket_limit": POOL,
    "tickets_sold": SOLD,
    "tickets_remaining": REMAINING,
    "advertised_total_prize_face_gbp": TOTAL_FACE,
    "remaining_advertised_prize_face_gbp": REMAINING_FACE,
    "second_class_postage_gbp": POSTAGE,
    "postal_entries_per_letter": entries_per_letter,
    "full_pool_paid_cost_gbp": paid_full_cost,
    "full_pool_paid_face_return": TOTAL_FACE / paid_full_cost,
    "full_pool_postal_letters": postal_letters_full,
    "full_pool_postal_cost_gbp": round(postal_full_cost, 2),
    "full_pool_postal_face_return": TOTAL_FACE / postal_full_cost,
    "remaining_pool_paid_cost_gbp": round(paid_remaining_cost, 2),
    "remaining_pool_paid_face_return": REMAINING_FACE / paid_remaining_cost,
    "remaining_pool_postal_letters": postal_letters_remaining,
    "remaining_pool_postal_cost_gbp": round(postal_remaining_cost, 2),
    "remaining_pool_postal_face_return": REMAINING_FACE / postal_remaining_cost,
    "strict_profit_possible_under_impossible_full_takeover": False,
    "reason": "Paid full-pool face value is exactly break-even at best; postal bundling costs more than the face value, and current external sold tickets plus non-atomic postal processing further prevent deterministic takeover.",
}
print(json.dumps(out, indent=2))
