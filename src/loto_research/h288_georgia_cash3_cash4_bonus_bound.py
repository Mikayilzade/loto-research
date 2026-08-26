"""H288: Georgia Cash 3 / Cash 4 under current 50% iHOPE first-deposit bonus.

Uses the current published fixed prize tables.  For each primitive wager class we
compute exact average gross / stake.  Any nonnegative additive portfolio has
minimum outcome <= average outcome, so if the best primitive average multiplied
by the maximum 1.5x playable-balance subsidy is below 1.0, strict guaranteed
cash profit is impossible for the checked class.
"""

from __future__ import annotations
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "data" / "derived" / "h288_georgia_cash3_cash4_bonus_bound.json"

BONUS_MULTIPLIER = 1.5

cash3 = {
    "straight": 500 / 1000,
    "box_3way": (3 * 160) / 1000,
    "box_6way": (6 * 80) / 1000,
    "straight_box_3way": (330 + 2 * 80) / 1000,
    "straight_box_6way": (290 + 5 * 40) / 1000,
    "combo_3way": (3 * 500) / (1000 * 3),
    "combo_6way": (6 * 500) / (1000 * 6),
    "front_or_back_pair": 50 / 100,
    "one_off": (250 + 6 * 24 + 12 * 4 + 8 * 8) / 1000,
}

cash4 = {
    "straight": 5000 / 10000,
    "box_4way": (4 * 1200) / 10000,
    "box_6way": (6 * 800) / 10000,
    "box_12way": (12 * 400) / 10000,
    "box_24way": (24 * 200) / 10000,
    "straight_box_4way": (3100 + 3 * 600) / 10000,
    "straight_box_6way": (2900 + 5 * 400) / 10000,
    "straight_box_12way": (2700 + 11 * 200) / 10000,
    "straight_box_24way": (2600 + 23 * 100) / 10000,
    "combo_4way": (4 * 5000) / (10000 * 4),
    "combo_6way": (6 * 5000) / (10000 * 6),
    "combo_12way": (12 * 5000) / (10000 * 12),
    "combo_24way": (24 * 5000) / (10000 * 24),
    "one_off": (2500 + 8 * 124 + 24 * 24 + 32 * 14 + 16 * 32) / 10000,
}

best3_name, best3 = max(cash3.items(), key=lambda kv: kv[1])
best4_name, best4 = max(cash4.items(), key=lambda kv: kv[1])

result = {
    "packet": "H288",
    "promotion_playable_multiplier": BONUS_MULTIPLIER,
    "cash3": cash3,
    "cash4": cash4,
    "cash3_best": {"name": best3_name, "average_gross_ratio": best3, "deposit_recovery_upper_bound": best3 * BONUS_MULTIPLIER},
    "cash4_best": {"name": best4_name, "average_gross_ratio": best4, "deposit_recovery_upper_bound": best4 * BONUS_MULTIPLIER},
    "global_checked_best_deposit_recovery_upper_bound": max(best3, best4) * BONUS_MULTIPLIER,
    "strict_profit_possible_for_checked_additive_class": max(best3, best4) * BONUS_MULTIPLIER > 1.0,
}

assert abs(best3 - 0.506) < 1e-12
assert abs(best4 - 0.5028) < 1e-12
assert result["global_checked_best_deposit_recovery_upper_bound"] == 0.759
assert not result["strict_profit_possible_for_checked_additive_class"]

OUT.parent.mkdir(parents=True, exist_ok=True)
OUT.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
print(json.dumps(result, indent=2, sort_keys=True))
