import json

PACKET = "H357"
MAX_HOLDING = 50_000
AUG_ELIGIBLE = 136_946_390_805
AUG_PRIZES = 6_224_837
AUG_PRIZE_VALUE = 433_663_575

external = AUG_ELIGIBLE - MAX_HOLDING
external_after_all_prizes = external - AUG_PRIZES
zero_prize_branch = external_after_all_prizes >= 0

result = {
    "packet": PACKET,
    "game": "UK NS&I Premium Bonds",
    "max_holding_gbp": MAX_HOLDING,
    "august_2026_eligible_bonds": AUG_ELIGIBLE,
    "august_2026_prize_count": AUG_PRIZES,
    "august_2026_prize_value_gbp": AUG_PRIZE_VALUE,
    "external_bonds_at_max_holding": external,
    "external_capacity_after_all_prizes": external_after_all_prizes,
    "zero_prize_branch_exists": zero_prize_branch,
    "redeemable_principal_floor_gbp": MAX_HOLDING,
    "nominal_prize_floor_gbp": 0,
    "nominal_profit_floor_gbp": 0,
    "strict_positive_profit_guaranteed": False,
    "announced_september_prize_fund_rate": 0.0435,
    "announced_september_odds_per_one_pound": 21_000,
    "arithmetic_inconclusive": 0,
    "closure_relevant_inconclusive": 0,
}

assert external == 136_946_340_805
assert external_after_all_prizes == 136_940_115_968
assert zero_prize_branch
assert result["redeemable_principal_floor_gbp"] + result["nominal_prize_floor_gbp"] == MAX_HOLDING
assert result["nominal_profit_floor_gbp"] == 0
assert not result["strict_positive_profit_guaranteed"]

print(json.dumps(result, indent=2, sort_keys=True))
