"""H308 exact acquisition comparison for CrazyWins zero-sold finite-pool candidate."""

POOL = 2_000
PAID_TICKET_GBP = 0.10
SECOND_CLASS_POSTAGE_GBP = 0.91

paid_full_pool = POOL * PAID_TICKET_GBP
postal_full_pool = POOL * SECOND_CLASS_POSTAGE_GBP
postal_to_paid_ratio = postal_full_pool / paid_full_pool

assert paid_full_pool == 200.0
assert postal_full_pool == 1820.0
assert abs(postal_to_paid_ratio - 9.1) < 1e-12

result = {
    "packet": "H308",
    "candidate": "CrazyWins HAMSTER FRENZY indexed zero-sold finite pool",
    "pool_entries": POOL,
    "paid_ticket_gbp": PAID_TICKET_GBP,
    "paid_full_pool_gbp": paid_full_pool,
    "second_class_postage_gbp": SECOND_CLASS_POSTAGE_GBP,
    "postal_full_pool_postage_only_gbp": postal_full_pool,
    "postal_to_paid_cost_ratio": postal_to_paid_ratio,
    "free_route_separate_post_required": True,
    "proof_of_posting_guarantees_entry": False,
    "entry_rejected_if_cap_fills_before_receipt": True,
    "entry_numbers_randomly_allocated": True,
    "atomic_full_pool_reservation_established": False,
    "strict_takeover_certified": False,
    "status": "CLOSED / EXECUTION-BLOCKED",
}

if __name__ == "__main__":
    import json
    print(json.dumps(result, indent=2))
