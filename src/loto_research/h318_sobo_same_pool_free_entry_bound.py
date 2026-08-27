"""H318: SOBO finite-pool same-pool free-entry / cap bound.

Current checked draw: 'Win a £200 Local Experience'.
The operator page publishes N=299, £1 paid entries and max 25 entries/person.
The August 2026 competition rules additionally say the free route is one free
entry/person/competition and that paid+free entries share the same person cap.

This packet proves that the current draw cannot be a deterministic takeover:
274 identifiers necessarily remain outside a one-person portfolio.  It also
records the stronger impossible-perfect full-buyout economics, which remain
below break-even even if the per-person cap is ignored.
"""
from __future__ import annotations
import json
from pathlib import Path

N = 299
PRICE = 1.0
PRIZE_VALUE = 200.0
MAX_PER_PERSON = 25
MAX_FREE_PER_PERSON = 1

out = {
    "packet": "H318",
    "candidate": "SOBO Win a £200 Local Experience",
    "total_identifiers": N,
    "paid_entry_price_gbp": PRICE,
    "advertised_prize_value_gbp": PRIZE_VALUE,
    "max_entries_per_person": MAX_PER_PERSON,
    "max_free_entries_per_person": MAX_FREE_PER_PERSON,
    "max_control_fraction": MAX_PER_PERSON / N,
    "minimum_external_identifiers": N - MAX_PER_PERSON,
    "strict_main_draw_cash_floor_gbp": 0.0,
    "impossible_full_buyout_cost_gbp": N * PRICE,
    "impossible_full_buyout_prize_to_cost_ratio": PRIZE_VALUE / (N * PRICE),
    "full_buyout_deficit_gbp": N * PRICE - PRIZE_VALUE,
    "closed": True,
    "reason": "One-person cap leaves legal external winning identifiers; even ignoring the cap, full paid acquisition costs more than the advertised prize value.",
}

assert N - MAX_PER_PERSON == 274
assert MAX_FREE_PER_PERSON <= MAX_PER_PERSON < N
assert out["strict_main_draw_cash_floor_gbp"] == 0.0
assert N * PRICE == 299.0
assert PRIZE_VALUE / (N * PRICE) < 1.0
assert abs(PRIZE_VALUE / (N * PRICE) - 200/299) < 1e-15

if __name__ == "__main__":
    root = Path(__file__).resolve().parents[2]
    p = root / "data" / "derived" / "h318_sobo_same_pool_free_entry_bound.json"
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(out, indent=2) + "\n")
    print(json.dumps(out, indent=2))
