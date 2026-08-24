from math import comb
import json

N = comb(49, 6)
spend = N * 3
counts = {
    "6_of_6": 1,
    "5_of_6_plus_bonus": comb(6, 5),
    "5_of_6": comb(6, 5) * 42,
    "4_of_6": comb(6, 4) * comb(43, 2),
    "3_of_6": comb(6, 3) * comb(43, 3),
    "2_of_6_plus_bonus": comb(6, 2) * comb(42, 3),
    "2_of_6": comb(6, 2) * comb(42, 4),
}
fixed_cash = counts["3_of_6"] * 10 + counts["2_of_6_plus_bonus"] * 5
free_play_face = counts["2_of_6"] * 3
prize_fund = spend * 0.1833
# Deliberately favorable to the candidate: do not subtract Free Play liability.
pools_fund_upper = max(0.0, prize_fund - fixed_cash)
classic_jackpot = 5_000_000
white_gold_ball = 1_000_000
superdraw_extra = 20 * 40_000
favorable_total = (
    fixed_cash
    + free_play_face
    + pools_fund_upper
    + classic_jackpot
    + white_gold_ball
    + superdraw_extra
)
result = {
    "combinations": N,
    "spend_cad": spend,
    "counts": counts,
    "fixed_cash_cad": fixed_cash,
    "free_play_face_cad": free_play_face,
    "prize_fund_18_33pct_cad": prize_fund,
    "favorable_pools_fund_upper_cad": pools_fund_upper,
    "classic_jackpot_cad": classic_jackpot,
    "white_gold_ball_cad": white_gold_ball,
    "superdraw_extra_cad": superdraw_extra,
    "favorable_total_cad": favorable_total,
    "favorable_return_ratio": favorable_total / spend,
    "favorable_deficit_cad": spend - favorable_total,
    "strict_guarantee": False,
}
print(json.dumps(result, indent=2))
