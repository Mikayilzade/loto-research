"""H257: current 2026 LOTTO MAX full-cover / overlay guarantee screen."""
from math import comb, ceil
import json

N = comb(52, 7)
PLAY_PRICE = 6
SELECTIONS_PER_PLAY = 4
MIN_PLAYS_IDEAL_PACKING = ceil(N / SELECTIONS_PER_PLAY)
MIN_COST_IDEAL_PACKING = MIN_PLAYS_IDEAL_PACKING * PLAY_PRICE

# For one copy of every 7-subset against a Main Draw of 7 main + 1 bonus:
# 4/7 means four main and three undrawn (non-bonus) numbers.
# 3/7+ means three main + bonus + three undrawn numbers.
N_4_7 = comb(7, 4) * comb(44, 3)
N_3_7_BONUS = comb(7, 3) * comb(44, 3)
FIXED_CASH_FLOOR = 20 * (N_4_7 + N_3_7_BONUS)

# 3/7 is a Free Play, not immediate cash; strict eventual cash floor is not credited.
# 7/7, 6/7+, 6/7, 5/7+, 5/7, 4/7+, MAXPLUS and MAXMILLIONS are shared pools/prizes.
# With no rule-based hard cap on external duplicate winning selections, they have no
# positive deterministic pre-draw cash floor for a strict guarantee proof.

result = {
    "packet": "H257",
    "game": "LOTTO MAX 3.0 (effective April 2026)",
    "combination_space": N,
    "selections_per_play": SELECTIONS_PER_PLAY,
    "play_price_cad": PLAY_PRICE,
    "idealized_minimum_plays_if_all_four_slots_perfectly_packable": MIN_PLAYS_IDEAL_PACKING,
    "idealized_minimum_full_cover_cost_cad": MIN_COST_IDEAL_PACKING,
    "match_4_fixed_winning_selections": N_4_7,
    "match_3_plus_bonus_fixed_winning_selections": N_3_7_BONUS,
    "fixed_cash_floor_cad": FIXED_CASH_FLOOR,
    "fixed_cash_floor_ratio": FIXED_CASH_FLOOR / MIN_COST_IDEAL_PACKING,
    "strict_shared_prize_floor_cad": 0,
    "strict_total_cash_floor_cad": FIXED_CASH_FLOOR,
    "strict_floor_deficit_cad": MIN_COST_IDEAL_PACKING - FIXED_CASH_FLOOR,
    "strict_guarantee": False,
    "reason": "All headline jackpot/MAXPLUS/MAXMILLIONS and upper main tiers are shareable by an externally unbounded number of matching selections under published rules; no useful hard pre-draw duplicate cap is available."
}

if __name__ == "__main__":
    print(json.dumps(result, indent=2))
