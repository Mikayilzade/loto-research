from math import comb
import json

N = comb(50, 5) * comb(12, 2)
PRICE = 2.50
JACKPOT_CAP = 250_000_000.0
PRIZE_FRACTION = 0.50

full_cover_cost = N * PRICE
collection_with_one_external = full_cover_cost + PRICE
all_current_prize_money_upper = PRIZE_FRACTION * collection_with_one_external
our_jackpot_share_one_external_duplicate = JACKPOT_CAP / 2
upper_gross = all_current_prize_money_upper + our_jackpot_share_one_external_duplicate
upper_net = upper_gross - full_cover_cost
upper_return = upper_gross / full_cover_cost
remaining_needed_after_all_current_prize_money = full_cover_cost - all_current_prize_money_upper
required_total_jackpot_if_two_winners = 2 * remaining_needed_after_all_current_prize_money
no_external_crude_upper = JACKPOT_CAP + PRIZE_FRACTION * full_cover_cost

result = {
    "combination_space": N,
    "price_per_line_eur": PRICE,
    "full_cover_cost_eur": full_cover_cost,
    "jackpot_cap_eur": JACKPOT_CAP,
    "headline_prize_fraction": PRIZE_FRACTION,
    "one_external_duplicate_branch": {
        "collection_eur": collection_with_one_external,
        "all_current_prize_money_upper_eur": all_current_prize_money_upper,
        "our_jackpot_share_upper_eur": our_jackpot_share_one_external_duplicate,
        "gross_upper_eur": upper_gross,
        "net_upper_eur": upper_net,
        "return_upper": upper_return,
        "return_upper_pct": 100 * upper_return,
    },
    "equivalent_threshold": {
        "remaining_needed_after_all_current_prize_money_eur": remaining_needed_after_all_current_prize_money,
        "required_total_jackpot_if_two_winners_eur": required_total_jackpot_if_two_winners,
    },
    "no_external_crude_upper": {
        "gross_eur": no_external_crude_upper,
        "return": no_external_crude_upper / full_cover_cost,
    },
    "strict_guarantee_closed_by_one_external_5plus2_duplicate": upper_net < 0,
}

if __name__ == "__main__":
    print(json.dumps(result, indent=2, sort_keys=True))
