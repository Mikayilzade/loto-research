from math import comb

N = comb(45, 6)
cost = N // 3 * 2

D1 = 1
D2 = comb(6, 5) * comb(2, 1)
D3 = comb(6, 5) * comb(37, 1)
D4 = comb(6, 4) * comb(39, 2)
D5 = comb(6, 3) * (comb(2, 1) * comb(37, 2) + comb(2, 2) * comb(37, 1))
D6 = comb(6, 2) * comb(2, 2) * comb(37, 2) + comb(6, 1) * comb(2, 2) * comb(37, 3)

counts = {"D1": D1, "D2": D2, "D3": D3, "D4": D4, "D5": D5, "D6": D6}
assert N == 8_145_060
assert N % 3 == 0
assert cost == 5_430_040
assert counts == {"D1": 1, "D2": 12, "D3": 222, "D4": 11115, "D5": 27380, "D6": 56610}
assert sum(counts.values()) == 95_340

print({"space": N, "full_cover_cost_aud": cost, "counts": counts, "eligible": sum(counts.values()), "d1_max_ordinary_aud": 1_000_000, "gap_after_d1_aud": cost - 1_000_000, "inconclusive": 0})
