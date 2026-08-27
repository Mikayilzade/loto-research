from __future__ import annotations

N = 119_999
PRICE = 0.20
ADVERTISED_POOL = 15_000.0
SNAPSHOT_SOLD = 3_625
SECOND_CLASS_POSTAGE = 0.91

# Published cash instant-win schedule.
CASH_SCHEDULE = {
    2000: 2,
    1000: 3,
    500: 4,
    100: 10,
    75: 14,
    25: 38,
    10: 150,
}

cash_instant = sum(v * c for v, c in CASH_SCHEDULE.items())
full_paid_cost = N * PRICE
full_paid_ratio = ADVERTISED_POOL / full_paid_cost
cash_only_ratio = cash_instant / full_paid_cost
remaining = N - SNAPSHOT_SOLD
remaining_paid_cost = remaining * PRICE
full_postal_cost = N * SECOND_CLASS_POSTAGE
postal_ratio = ADVERTISED_POOL / full_postal_cost

assert cash_instant == 13_500
assert round(full_paid_cost, 2) == 23_999.80
assert full_paid_ratio < 1
assert cash_only_ratio < full_paid_ratio
assert remaining == 116_374
assert round(full_postal_cost, 2) == 109_199.09
assert postal_ratio < full_paid_ratio

if __name__ == "__main__":
    print({
        "pool_tickets": N,
        "ticket_price_gbp": PRICE,
        "full_paid_cost_gbp": round(full_paid_cost, 2),
        "advertised_total_prize_pool_gbp": ADVERTISED_POOL,
        "published_cash_instant_gbp": cash_instant,
        "full_paid_gross_ratio": full_paid_ratio,
        "cash_only_gross_ratio": cash_only_ratio,
        "snapshot_sold": SNAPSHOT_SOLD,
        "remaining_tickets": remaining,
        "remaining_paid_cost_gbp": round(remaining_paid_cost, 2),
        "full_postal_cost_gbp": round(full_postal_cost, 2),
        "full_postal_gross_ratio": postal_ratio,
    })
