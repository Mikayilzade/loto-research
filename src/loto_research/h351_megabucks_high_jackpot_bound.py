from math import comb

N = comb(44, 6)
PRICE = 2
COST = N * PRICE
JACKPOT = 28_600_000
PRIZES = {5: 5000, 4: 200, 3: 4}
counts = {k: comb(6, k) * comb(38, 6-k) for k in range(7)}
assert sum(counts.values()) == N
lower = sum(counts[k] * PRIZES[k] for k in PRIZES)
assert N == 7_059_052
assert COST == 14_118_104
assert counts[6] == 1
assert counts[5] == 228
assert counts[4] == 10_545
assert counts[3] == 168_720
assert lower == 3_923_880

# Deliberately impossible-favourable stress: add 100% of our cover spend to
# the advertised jackpot before sharing. Actual rules state ~61.79% of wagers
# enter the prize pool and lower prizes are paid from that pool.
dominating_jackpot = JACKPOT + COST
rows = []
for external_duplicates in range(0, 11):
    winners = external_duplicates + 1
    gross_upper = lower + dominating_jackpot / winners
    rows.append((external_duplicates, gross_upper, gross_upper - COST))

assert rows[3][2] > 0
assert rows[4][2] < 0
assert abs(rows[4][1] - 12_467_500.8) < 1e-6
assert abs(rows[4][2] + 1_650_603.2) < 1e-6

print({
    "space": N,
    "cost": COST,
    "counts": counts,
    "lower_fixed_gross": lower,
    "advertised_jackpot": JACKPOT,
    "isolated_nominal_gross": lower + JACKPOT,
    "dominating_jackpot": dominating_jackpot,
    "first_external_duplicate_count_below_cost": 4,
    "gross_upper_at_4_external_duplicates": rows[4][1],
    "net_upper_at_4_external_duplicates": rows[4][2],
    "arithmetic_inconclusive": 0,
    "closure_relevant_inconclusive": 0,
})
