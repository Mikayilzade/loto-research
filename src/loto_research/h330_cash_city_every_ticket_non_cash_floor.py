from __future__ import annotations

# H330 exact audit: Cash City Ticket Bundle — EVERY TICKET WINS
# Snapshot checked 2026-08-28.

TOTAL_IDS = 150
SOLD = 53
LEFT = 97
MAX_PER_PERSON = 15
ENTRY_PRICE_GBP = 2.50
MAIN_PRIZE_SITE_CREDIT_GBP = 20.00

# Published instant-prize classes and live counts.
CLASSES = {
    "3_paw_patrol_plus_1_site_credit_ticket": {"total": 40, "left": 28},
    "3_paw_patrol_plus_1_dior_ticket": {"total": 20, "left": 14},
    "14_snoozeband_tickets": {"total": 36, "left": 25},
    "7_dior_tickets": {"total": 22, "left": 12},
    "gbp_2_50_site_credit": {"total": 32, "left": 18},
}

assert sum(v["total"] for v in CLASSES.values()) == TOTAL_IDS
assert sum(v["left"] for v in CLASSES.values()) == LEFT
assert SOLD + LEFT == TOTAL_IDS
assert MAX_PER_PERSON < TOTAL_IDS

# The operator description states that every instant outcome is either site credit
# or entries into other competitions. The main prize is also site credit.
# No cash alternative is stated for this competition. Under the governing terms,
# a cash alternative exists only when it is explicitly offered in the prize description.
# Therefore at least one legal outcome has zero withdrawable cash, and indeed the
# published prize taxonomy contains no guaranteed withdrawable-cash outcome at all.
STRICT_WITHDRAWABLE_CASH_FLOOR_GBP = 0.0
assert STRICT_WITHDRAWABLE_CASH_FLOOR_GBP == 0.0

print({
    "total_ids": TOTAL_IDS,
    "sold": SOLD,
    "left": LEFT,
    "max_per_person": MAX_PER_PERSON,
    "class_total_sum": sum(v["total"] for v in CLASSES.values()),
    "class_left_sum": sum(v["left"] for v in CLASSES.values()),
    "strict_withdrawable_cash_floor_gbp": STRICT_WITHDRAWABLE_CASH_FLOOR_GBP,
})
