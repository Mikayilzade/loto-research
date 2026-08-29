from math import comb
import json

N = comb(52, 5) * 10
counts = {
    "jackpot_5_plus_star": 1,
    "match5_no_star": 9,
    "match4_plus_star": comb(5, 4) * comb(47, 1),
    "match4_no_star": comb(5, 4) * comb(47, 1) * 9,
    "match3_plus_star": comb(5, 3) * comb(47, 2),
    "match3_no_star": comb(5, 3) * comb(47, 2) * 9,
    "match2_plus_star": comb(5, 2) * comb(47, 3),
    "match1_plus_star": comb(5, 1) * comb(47, 4),
    "star_only": comb(47, 5),
}
base_prizes = {
    "match5_no_star": 20000,
    "match4_plus_star": 1000,
    "match4_no_star": 100,
    "match3_plus_star": 20,
    "match3_no_star": 5,
    "match2_plus_star": 5,
    "match1_plus_star": 2,
    "star_only": 2,
}
partition = sum(comb(5, k) * comb(47, 5-k) * 10 for k in range(6))
fixed_gross = sum(counts[k] * v for k, v in base_prizes.items())
asb2_gross = 2 * fixed_gross
current_advertised_jackpot = 3_120_000
result = {
    "packet": "H356",
    "game": "Lotto America + All Star Bonus",
    "full_cover_lines": N,
    "partition_total": partition,
    "partition_matches_space": partition == N,
    "counts": counts,
    "base_cost": N,
    "base_fixed_gross": fixed_gross,
    "base_fixed_return": fixed_gross / N,
    "base_break_even_jackpot": N - fixed_gross,
    "asb_min_multiplier": 2,
    "asb_cost": 2 * N,
    "asb_min_fixed_gross": asb2_gross,
    "asb_min_fixed_return": asb2_gross / (2*N),
    "asb_break_even_jackpot": 2*N - asb2_gross,
    "current_advertised_jackpot": current_advertised_jackpot,
    "base_current_jackpot_upper_gross": fixed_gross + current_advertised_jackpot,
    "asb_current_jackpot_upper_gross": asb2_gross + current_advertised_jackpot,
    "arithmetic_inconclusive": 0,
    "closure_relevant_inconclusive": 0,
}
assert partition == N == 25_989_600
assert fixed_gross == 6_991_428
assert asb2_gross == 13_982_856
assert result["base_break_even_jackpot"] == 18_998_172
assert result["asb_break_even_jackpot"] == 37_996_344
print(json.dumps(result, indent=2, sort_keys=True))
