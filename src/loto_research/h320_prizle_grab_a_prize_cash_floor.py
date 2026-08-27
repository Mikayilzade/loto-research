"""H320: Prizle Grab A Prize guaranteed-win / site-credit cash-floor bound.

Current late-Aug-2026 page data used here:
- 8,000 instant-win ticket identifiers;
- max 1,000 entries per person;
- £4.99 per paid entry;
- every ticket guarantees an instant prize;
- instant-prize inventory contains 7,000 site-credit-only identifiers;
- the remaining 1,000 identifiers are cash/product/gift-card prizes;
- a separate £500 end draw is random.

The relevant target is guaranteed *withdrawable cash*, not marketing face value.
Because the site-credit-only class is much larger than the player cap, there is a
legal allocation in which all 1,000 player entries receive site credit and no
cash/product instant prize. The separate end draw can also be won by an external
entry. Therefore the strict withdrawable-cash floor is zero.

A secondary calculation gives the deliberately favourable minimum site-credit
face value among 1,000 distinct currently-available site-credit identifiers.
This is not cash and does not change the closure result.
"""
from __future__ import annotations
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "data" / "derived" / "h320_prizle_grab_a_prize_cash_floor.json"

TOTAL_INSTANT_IDS = 8_000
MAX_PER_PERSON = 1_000
PRICE_GBP = 4.99
END_DRAW_CASH_GBP = 500.0

# Published full instant-prize schedule.
SITE_CREDIT_FULL = [
    (25.00, 39),
    (10.00, 80),
    (5.00, 1_600),
    (3.00, 502),
    (2.00, 1_779),
    (1.00, 1_000),
    (0.50, 1_000),
    (0.25, 500),
    (0.10, 300),
    (0.05, 100),
    (0.01, 100),
]

# Snapshot 'to be won' counts from the indexed current page.
SITE_CREDIT_AVAILABLE = [
    (25.00, 39),
    (10.00, 79),
    (5.00, 1_598),
    (3.00, 500),
    (2.00, 1_774),
    (1.00, 999),
    (0.50, 998),
    (0.25, 500),
    (0.10, 298),
    (0.05, 100),
    (0.01, 100),
]

CASH_FULL = [(100.0, 1), (10.0, 20), (5.0, 50), (2.0, 400), (1.0, 500)]
PRODUCT_SINGLETON_VALUES = [
    1099.0, 450.0, 779.0, 549.0, 89.99, 380.0, 199.0, 339.0,
    129.0, 129.0, 329.0, 349.0, 229.0, 89.99, 499.0, 54.99, 219.0,
]
# 4x Just Eat £25, 4x AirTag pack £99, 4x Costa £25.
OTHER_PRODUCT_GIFT_VALUES = [25.0] * 4 + [99.0] * 4 + [25.0] * 4


def count(rows: list[tuple[float, int]]) -> int:
    return sum(n for _, n in rows)


def face(rows: list[tuple[float, int]]) -> float:
    return sum(v * n for v, n in rows)


def smallest_distinct_face(rows: list[tuple[float, int]], k: int) -> float:
    remaining = k
    total = 0.0
    for value, n in sorted(rows):
        take = min(remaining, n)
        total += value * take
        remaining -= take
        if remaining == 0:
            return total
    raise ValueError("not enough identifiers")


def main() -> None:
    site_full_count = count(SITE_CREDIT_FULL)
    site_available_count = count(SITE_CREDIT_AVAILABLE)
    cash_count = count(CASH_FULL)
    product_count = len(PRODUCT_SINGLETON_VALUES) + len(OTHER_PRODUCT_GIFT_VALUES)
    non_site_count = cash_count + product_count

    assert site_full_count == 7_000
    assert cash_count == 971
    assert product_count == 29
    assert non_site_count == 1_000
    assert site_full_count + non_site_count == TOTAL_INSTANT_IDS
    assert site_available_count == 6_985
    assert site_available_count >= MAX_PER_PERSON

    current_min_1000_credit_face = smallest_distinct_face(SITE_CREDIT_AVAILABLE, MAX_PER_PERSON)
    assert abs(current_min_1000_credit_face - 161.80) < 1e-9

    paid_cost = MAX_PER_PERSON * PRICE_GBP
    full_site_credit_face = face(SITE_CREDIT_FULL)
    cash_face = face(CASH_FULL)
    product_face = sum(PRODUCT_SINGLETON_VALUES) + sum(OTHER_PRODUCT_GIFT_VALUES)
    total_advertised_face_including_end = full_site_credit_face + cash_face + product_face + END_DRAW_CASH_GBP

    out = {
        "packet": "H320",
        "state": "CLOSED / ZERO-WITHDRAWABLE-CASH-FLOOR",
        "competition": "Prizle Grab A Prize",
        "total_instant_identifiers": TOTAL_INSTANT_IDS,
        "max_entries_per_person": MAX_PER_PERSON,
        "paid_entry_price_gbp": PRICE_GBP,
        "max_paid_spend_gbp": paid_cost,
        "full_schedule": {
            "site_credit_only_identifiers": site_full_count,
            "cash_identifiers": cash_count,
            "product_or_gift_identifiers": product_count,
            "non_site_credit_identifiers": non_site_count,
            "site_credit_face_gbp": full_site_credit_face,
            "cash_face_gbp": cash_face,
            "product_or_gift_face_gbp": product_face,
            "end_draw_cash_gbp": END_DRAW_CASH_GBP,
            "advertised_face_including_end_draw_gbp": total_advertised_face_including_end,
        },
        "current_snapshot": {
            "available_site_credit_identifiers": site_available_count,
            "available_site_credit_ids_at_least_player_cap": site_available_count >= MAX_PER_PERSON,
            "minimum_face_value_of_1000_distinct_available_site_credit_ids_gbp": current_min_1000_credit_face,
            "minimum_site_credit_face_to_paid_spend_ratio": current_min_1000_credit_face / paid_cost,
        },
        "strict_withdrawable_cash_floor_gbp": 0.0,
        "proof": [
            "There are at least 6,985 currently-available site-credit-only instant identifiers, exceeding the 1,000-entry player cap.",
            "Hence a legal allocation exists in which every player entry receives site credit and no withdrawable-cash instant prize.",
            "The separate £500 end draw can legally be won by an external entry because one player cannot control the 8,000-entry pool.",
            "Therefore the player's strict withdrawable-cash floor is £0 even though every ticket wins an instant prize.",
        ],
        "conclusion": "Guaranteed positive prize face value is not guaranteed withdrawable cash; H320 is closed for strict-profit purposes.",
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(out, indent=2) + "\n")
    print(json.dumps(out, indent=2))


if __name__ == "__main__":
    main()
