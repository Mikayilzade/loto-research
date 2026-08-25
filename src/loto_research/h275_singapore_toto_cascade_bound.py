"""H275: Singapore TOTO cascade/full-cover exact arithmetic.

Closes the checked strict-guarantee construction by two independent gates:
1) every nonempty portfolio contains a legal Group-1 outcome, so it cannot force
   the no-Group-1 cascade branch for every legal draw;
2) a complete one-copy C(49,6) cover necessarily wins Group 1 and therefore
   suppresses cascade.  Under unrestricted external duplicate stress, shared
   Groups 1-4 have no positive guaranteed floor, leaving only fixed Groups 5-7.
"""
from math import comb
import json

N = comb(49, 6)
COST_PER_ORDINARY = 1
cost = N * COST_PER_ORDINARY

counts = {
    "group1_6": 1,
    "group2_5_plus_additional": comb(6, 5),
    "group3_5": comb(6, 5) * comb(42, 1),
    "group4_4_plus_additional": comb(6, 4) * comb(42, 1),
    "group5_4": comb(6, 4) * comb(42, 2),
    "group6_3_plus_additional": comb(6, 3) * comb(42, 2),
    "group7_3": comb(6, 3) * comb(42, 3),
}

fixed_prizes = {"group5_4": 50, "group6_3_plus_additional": 25, "group7_3": 10}
fixed_gross = sum(counts[k] * v for k, v in fixed_prizes.items())
fixed_return = fixed_gross / cost

out = {
    "packet": "H275",
    "game": "Singapore Pools TOTO",
    "main_space": N,
    "ordinary_entry_cost_sgd": COST_PER_ORDINARY,
    "one_copy_full_cover_cost_sgd": cost,
    "winning_line_counts_for_any_draw": counts,
    "fixed_prizes_sgd": fixed_prizes,
    "fixed_lower_tier_gross_sgd": fixed_gross,
    "fixed_lower_tier_return_fraction": fixed_return,
    "fixed_lower_tier_return_percent": fixed_return * 100,
    "fixed_lower_tier_deficit_sgd": cost - fixed_gross,
    "cascade_force_gate": False,
    "cascade_force_reason": "Any purchased six-number line is itself a legal Group-1 draw outcome; therefore every nonempty portfolio has at least one legal outcome that prevents no-Group-1 cascade.",
    "full_cover_cascade_gate": False,
    "full_cover_cascade_reason": "A complete C(49,6) cover contains the winning six-number set for every draw and therefore always creates at least one Group-1 winning share.",
    "duplicate_stress_gate": False,
    "duplicate_stress_reason": "Groups 1-4 are share-based and the checked rules publish no useful hard cap on external winning shares; strict guarantee cannot assign them a positive duplicate-robust floor. Fixed Groups 5-7 alone return below cost.",
    "verdict": "REJECTED for strict guaranteed-profit cascade/full-cover takeover under checked current rules",
}

assert N == 13_983_816
assert counts["group5_4"] == 12_915
assert counts["group6_3_plus_additional"] == 17_220
assert counts["group7_3"] == 229_600
assert fixed_gross == 3_372_250
assert fixed_gross < cost

if __name__ == "__main__":
    print(json.dumps(out, indent=2, sort_keys=True))
