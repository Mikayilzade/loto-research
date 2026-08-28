from __future__ import annotations

TOTAL_IDS = 10_000
POSTAGE_GBP = 0.91
END_PRIZE_GBP = 100.0
CASH_CLASSES = [(500,5),(250,3),(100,6),(50,12),(25,30),(10,75),(5,150),(2,300),(1,9419)]

count_sum = sum(c for _, c in CASH_CLASSES)
instant_cash = sum(v*c for v,c in CASH_CLASSES)
cost = TOTAL_IDS * POSTAGE_GBP
gross = instant_cash + END_PRIZE_GBP
ret = gross / cost
surplus = gross - cost
break_even = gross / TOTAL_IDS

assert count_sum == TOTAL_IDS
assert instant_cash == 16_719
assert cost == 9_100
assert gross == 16_819
assert ret > 1.0
assert surplus == 7_719
print({"total_ids":TOTAL_IDS,"count_sum":count_sum,"instant_cash_gbp":instant_cash,"postal_cost_gbp":cost,"gross_gbp":gross,"return_pct":round(ret*100,6),"surplus_gbp":surplus,"break_even_entry_cost_gbp":break_even,"inconclusive_checks":0})
