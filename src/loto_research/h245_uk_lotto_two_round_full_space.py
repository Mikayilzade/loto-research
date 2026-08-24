from math import comb
import json

SPACE = comb(59, 6)
COST = 2 * SPACE
COUNTS = {
    "match6": 1,
    "match5_bonus": comb(6, 5),
    "match5": comb(6, 5) * 52,
    "match4": comb(6, 4) * comb(53, 2),
    "match3": comb(6, 3) * comb(53, 3),
    "match2": comb(6, 2) * comb(53, 4),
}
PRIZES = {
    "match5_bonus": 1_000_000,
    "match5": 1_000,
    "match4": 50,
    "match3": 10,
    "match2": 1,
}
ONE_ROUND_FIXED = sum(COUNTS[k] * PRIZES[k] for k in PRIZES)
TWO_ROUND_FIXED = 2 * ONE_ROUND_FIXED
result = {
    "space": SPACE,
    "full_space_cost_gbp": COST,
    "counts_per_round": COUNTS,
    "fixed_prizes_gbp": PRIZES,
    "fixed_cash_one_round_gbp": ONE_ROUND_FIXED,
    "fixed_cash_two_rounds_gbp": TWO_ROUND_FIXED,
    "fixed_return_ratio": TWO_ROUND_FIXED / COST,
    "fixed_deficit_gbp": COST - TWO_ROUND_FIXED,
    "must_be_won_no_jackpot_branch_possible_under_full_cover": False,
}
print(json.dumps(result, indent=2))
