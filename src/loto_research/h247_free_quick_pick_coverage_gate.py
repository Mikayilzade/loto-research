from math import comb
import json
from pathlib import Path

N = comb(58, 5) * 5
price = 5
paid_full_cover_cost = N * price
h026_favorable_gross = 60_584_320

result = {
    "packet": "H247",
    "game": "Millionaire for Life",
    "controlled_full_space_plays": N,
    "price_per_play": price,
    "controlled_paid_full_cover_cost": paid_full_cover_cost,
    "h026_deliberately_favorable_full_cover_gross": h026_favorable_gross,
    "h026_favorable_return_ratio": h026_favorable_gross / paid_full_cover_cost,
    "free_quick_pick_guaranteed_marginal_coverage": 0,
    "free_quick_pick_guaranteed_cash_floor": 0,
    "guaranteed_paid_coverage_count_with_uncontrolled_free_quick_picks": N,
    "guaranteed_paid_coverage_cost_with_uncontrolled_free_quick_picks": paid_full_cover_cost,
    "theorem": "Uncontrolled Quick Picks can all duplicate already-covered states; therefore their worst-case marginal coverage is zero."
}

out = Path("data/derived/h247_free_quick_pick_coverage_gate.json")
out.parent.mkdir(parents=True, exist_ok=True)
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
