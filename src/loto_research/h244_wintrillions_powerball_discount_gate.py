from math import comb
import json

N = comb(69, 5) * 26
ordinary_cost = 2 * N

counts = {
    "5_white_no_pb": 25,
    "4_plus_pb": comb(5, 4) * comb(64, 1),
    "4_only": comb(5, 4) * comb(64, 1) * 25,
    "3_plus_pb": comb(5, 3) * comb(64, 2),
    "3_only": comb(5, 3) * comb(64, 2) * 25,
    "2_plus_pb": comb(5, 2) * comb(64, 3),
    "1_plus_pb": comb(5, 1) * comb(64, 4),
    "0_plus_pb": comb(64, 5),
}
prizes = {
    "5_white_no_pb": 1_000_000,
    "4_plus_pb": 50_000,
    "4_only": 100,
    "3_plus_pb": 100,
    "3_only": 7,
    "2_plus_pb": 7,
    "1_plus_pb": 4,
    "0_plus_pb": 4,
}

lower_tier_gross = sum(counts[k] * prizes[k] for k in prizes)
discount = 0.90
discounted_cost = ordinary_cost * (1 - discount)
margin = lower_tier_gross - discounted_cost
break_even_discount = 1 - lower_tier_gross / ordinary_cost

out = {
    "combination_space": N,
    "ordinary_full_space_cost_usd": ordinary_cost,
    "deterministic_non_jackpot_gross_usd": lower_tier_gross,
    "non_jackpot_return_on_ordinary_cost": lower_tier_gross / ordinary_cost,
    "break_even_discount_fraction": break_even_discount,
    "hypothetical_discount_fraction": discount,
    "hypothetical_discounted_full_space_cost_usd": discounted_cost,
    "hypothetical_pre_jackpot_margin_usd": margin,
    "counts": counts,
    "prizes_usd": prizes,
    "strict_guarantee_contract_gate": "FAIL: operator terms permit ignoring promotional enhancement where guaranteed profits irrespective of outcome arise",
}

if __name__ == "__main__":
    print(json.dumps(out, indent=2, sort_keys=True))
