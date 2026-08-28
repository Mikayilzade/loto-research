from __future__ import annotations

TOTAL_TICKETS = 99_999
SOLD_SNAPSHOT = 316
PAID_PRICE_GBP = 0.10
POSTAL_COST_GBP = 0.91
POSTAL_TICKETS = 10
MAX_PER_USER = 999

# (cash value GBP, total identifiers in tier)
TIERS = [
    (100.0, 5),
    (50.0, 4),
    (20.0, 20),
    (10.0, 70),
    (5.0, 180),
    (2.0, 350),
    (1.0, 400),
    (0.50, 1500),
    (0.20, 1500),
    (0.10, 8000),
]

# Snapshot found counts shown on the live page: 4x £2, 1x £1,
# 5x 50p, 5x 20p, 26x 10p; no higher-tier finds shown.
FOUND_SNAPSHOT = 4 + 1 + 5 + 5 + 26


def build_result() -> dict:
    total_instant_ids = sum(n for _, n in TIERS)
    total_instant_face_gbp = sum(v * n for v, n in TIERS)
    remaining_tickets = TOTAL_TICKETS - SOLD_SNAPSHOT
    remaining_instant_ids = total_instant_ids - FOUND_SNAPSHOT
    remaining_zero_instant_ids = remaining_tickets - remaining_instant_ids

    paid_cost_for_postal_bundle = PAID_PRICE_GBP * POSTAL_TICKETS
    postal_effective_per_ticket = POSTAL_COST_GBP / POSTAL_TICKETS
    postal_discount_vs_paid = 1 - POSTAL_COST_GBP / paid_cost_for_postal_bundle

    # Strict worst-case: one valid postal entry receives 10 randomly allocated
    # identifiers.  Because remaining zero-instant identifiers exceed 10, there
    # exists a legal allocation in which all 10 are zero-cash instant outcomes.
    strict_cash_floor_gbp = 0.0

    result = {
        "total_tickets": TOTAL_TICKETS,
        "sold_snapshot": SOLD_SNAPSHOT,
        "remaining_tickets": remaining_tickets,
        "paid_price_gbp": PAID_PRICE_GBP,
        "postal_cost_gbp": POSTAL_COST_GBP,
        "postal_tickets": POSTAL_TICKETS,
        "postal_effective_per_ticket_gbp": postal_effective_per_ticket,
        "paid_cost_for_same_10_tickets_gbp": paid_cost_for_postal_bundle,
        "postal_discount_vs_paid_fraction": postal_discount_vs_paid,
        "max_per_user": MAX_PER_USER,
        "total_instant_ids": total_instant_ids,
        "total_instant_face_gbp": total_instant_face_gbp,
        "found_snapshot": FOUND_SNAPSHOT,
        "remaining_instant_ids": remaining_instant_ids,
        "remaining_zero_instant_ids": remaining_zero_instant_ids,
        "strict_withdrawable_cash_floor_gbp": strict_cash_floor_gbp,
        "closure": "CLOSED / RANDOM-ALLOCATION-AND-FREE-ROUTE-CAP BLOCKED",
    }

    assert total_instant_ids == 12_029
    assert abs(total_instant_face_gbp - 5_650.0) < 1e-9
    assert remaining_tickets == 99_683
    assert remaining_instant_ids == 11_988
    assert remaining_zero_instant_ids == 87_695
    assert remaining_zero_instant_ids >= POSTAL_TICKETS
    assert MAX_PER_USER < TOTAL_TICKETS
    assert abs(postal_effective_per_ticket - 0.091) < 1e-12
    assert abs(postal_discount_vs_paid - 0.09) < 1e-12
    assert strict_cash_floor_gbp == 0.0
    return result


if __name__ == "__main__":
    import json
    print(json.dumps(build_result(), indent=2, sort_keys=True))
