from decimal import Decimal

N = 75_000
PRICE = Decimal("0.25")
PRIZE_VALUE_STRESS = Decimal("10000")
END_PRIZE = Decimal("100")

full_paid_cost = Decimal(N) * PRICE
favourable_liability = PRIZE_VALUE_STRESS + END_PRIZE
favourable_full_pool_ratio = favourable_liability / full_paid_cost

# Credit-path theorem witness flags:
# a legal platform outcome can be site-credit-only with zero withdrawable cash;
# site credit is spendable on further competitions rather than direct bank cash.
legal_site_credit_only_outcome = True
site_credit_directly_withdrawable_as_cash = False

# Therefore credit recycling alone cannot prove a positive withdrawable-cash floor.
credit_recycling_forces_positive_cash = (
    legal_site_credit_only_outcome
    and site_credit_directly_withdrawable_as_cash
)

assert full_paid_cost == Decimal("18750.00")
assert favourable_liability == Decimal("10100")
assert favourable_full_pool_ratio < Decimal("1")
assert legal_site_credit_only_outcome
assert not site_credit_directly_withdrawable_as_cash
assert not credit_recycling_forces_positive_cash

result = {
    "packet": "H329",
    "state": "CLOSED / CREDIT-RECYCLING DOES NOT FORCE CASH",
    "live_pool_tickets": N,
    "ticket_price_gbp": str(PRICE),
    "full_paid_cost_gbp": str(full_paid_cost),
    "favourable_liability_stress_gbp": str(favourable_liability),
    "favourable_full_pool_ratio": str(favourable_full_pool_ratio),
    "legal_site_credit_only_outcome": legal_site_credit_only_outcome,
    "site_credit_directly_withdrawable_as_cash": site_credit_directly_withdrawable_as_cash,
    "credit_recycling_forces_positive_cash": credit_recycling_forces_positive_cash,
    "strict_cash_floor_from_credit_recycling_alone_gbp": "0",
}

if __name__ == "__main__":
    import json
    print(json.dumps(result, indent=2, sort_keys=True))
