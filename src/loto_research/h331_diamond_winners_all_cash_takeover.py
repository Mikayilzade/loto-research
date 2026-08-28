from __future__ import annotations

# H331 exact audit: Diamond Winners 19,999-ticket Every Ticket Wins cash pool.
# Historical competition closed 2026-06-14; checked from operator page on 2026-08-28.

TOTAL_IDS = 19_999
ENTRY_PRICE_GBP = 0.59
MAX_PER_PERSON = 19_999
END_PRIZE_GBP = 150.00

CASH_CLASSES = [
    (500.00, 2),
    (250.00, 3),
    (100.00, 6),
    (50.00, 12),
    (20.00, 30),
    (10.00, 60),
    (5.00, 120),
    (1.00, 100),
    (0.50, 400),
    (0.25, 1_200),
    (0.10, 5_000),
    (0.05, 10_000),
    (0.05, 3_066),
]

class_count = sum(count for _, count in CASH_CLASSES)
instant_cash_gbp = sum(value * count for value, count in CASH_CLASSES)
full_online_cost_gbp = TOTAL_IDS * ENTRY_PRICE_GBP
full_takeover_gross_gbp = instant_cash_gbp + END_PRIZE_GBP
full_takeover_return = full_takeover_gross_gbp / full_online_cost_gbp
break_even_price_gbp = full_takeover_gross_gbp / TOTAL_IDS
required_discount_fraction = 1.0 - break_even_price_gbp / ENTRY_PRICE_GBP

assert class_count == TOTAL_IDS
assert MAX_PER_PERSON == TOTAL_IDS
assert abs(instant_cash_gbp - 6503.30) < 1e-9
assert abs(full_online_cost_gbp - 11799.41) < 1e-9
assert abs(full_takeover_gross_gbp - 6653.30) < 1e-9
assert full_takeover_return < 1.0
assert break_even_price_gbp < ENTRY_PRICE_GBP

print({
    "total_ids": TOTAL_IDS,
    "class_count": class_count,
    "instant_cash_gbp": round(instant_cash_gbp, 2),
    "full_online_cost_gbp": round(full_online_cost_gbp, 2),
    "full_takeover_gross_gbp": round(full_takeover_gross_gbp, 2),
    "full_takeover_return_pct": round(100 * full_takeover_return, 6),
    "break_even_price_gbp": round(break_even_price_gbp, 9),
    "required_discount_pct": round(100 * required_discount_fraction, 6),
    "inconclusive_checks": 0,
})
