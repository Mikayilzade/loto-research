#!/usr/bin/env python3
"""H248: deterministic percentage-discount upper-bound screen."""

import json
from pathlib import Path

DISCOUNT = 0.25
CASES = {
    "ohio_keno_3spot": 0.652130,
    "nebraska_2by2": 0.380289,
    "nebraska_myday_best": 0.584723,
    "millionaire_for_life_optimistic": 0.528876,
    "lotto_america_strict_nonjackpot": 6991428 / 25989600,
}

rows = []
for name, base_return in CASES.items():
    discounted_return = base_return / (1 - DISCOUNT)
    rows.append({
        "case": name,
        "base_return": base_return,
        "discount": DISCOUNT,
        "discounted_return_upper_bound": discounted_return,
        "break_even_discount_strictly_greater_than": 1 - base_return,
        "profitable_under_25pct_upper_bound": discounted_return > 1,
    })

out = {
    "packet": "H248",
    "discount_assumption": DISCOUNT,
    "assumption_note": "Dominating upper bound: 25% applies to entire controlled cover, zero fees/caps.",
    "all_rejected": all(not r["profitable_under_25pct_upper_bound"] for r in rows),
    "cases": rows,
}

path = Path("data/derived/h248_lotto_com_discount_upper_bound.json")
path.parent.mkdir(parents=True, exist_ok=True)
path.write_text(json.dumps(out, indent=2) + "\n", encoding="utf-8")
print(json.dumps(out, indent=2))
