"""H354: exact unique-series cover for Spain Loteria Nacional Thursday draw."""

NUMBERS = 100_000
SERIES = 6
BILLETE_EUR = 30
DECIMOS_PER_BILLETE = 10
DECIMO_EUR = BILLETE_EUR / DECIMOS_PER_BILLETE
ISSUE_EUR = SERIES * NUMBERS * BILLETE_EUR
PRIZE_POOL_EUR = 12_600_000

assert ISSUE_EUR == 18_000_000
assert PRIZE_POOL_EUR / ISSUE_EUR == 0.70

# Own one fixed fraction (one decimo) of every number in one series.
cover_entries = NUMBERS
cover_cost = NUMBERS * DECIMO_EUR
series_prize_pool = PRIZE_POOL_EUR / SERIES
cover_gross = series_prize_pool / DECIMOS_PER_BILLETE
cover_net = cover_gross - cover_cost
cover_return = cover_gross / cover_cost

assert cover_entries == 100_000
assert cover_cost == 300_000
assert cover_gross == 210_000
assert cover_net == -90_000
assert cover_return == 0.70

# Stronger impossible-perfect acquisition of the entire issue has the same ratio.
full_issue_cost = ISSUE_EUR
full_issue_gross = PRIZE_POOL_EUR
assert full_issue_gross / full_issue_cost == 0.70

RESULT = {
    "cover_entries": cover_entries,
    "cover_cost_eur": cover_cost,
    "cover_gross_eur": cover_gross,
    "cover_net_eur": cover_net,
    "return_fraction": cover_return,
    "full_issue_cost_eur": full_issue_cost,
    "full_issue_gross_eur": full_issue_gross,
    "arithmetic_inconclusive": 0,
    "closure_relevant_inconclusive": 0,
}

if __name__ == "__main__":
    print(RESULT)
