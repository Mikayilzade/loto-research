"""H300: Net-A-Deal 'Every ticket wins' deterministic cash-floor audit.

Current August 2026 £10,000 Instant Wins competitions have 49,999 tickets,
a 1,000-entry per-person cap, and only 32 explicitly cash-paying instant-win
identifiers. Another 40 identifiers pay site credit. Every remaining ticket is
entered into a separate £5,000 rewards competition rather than receiving a
cash prize. Because a rewards entry can legally lose, its strict withdrawable
cash floor is zero.
"""

TOTAL_TICKETS = 49_999
MAX_PER_PERSON = 1_000
ENTRY_PRICE_GBP = 0.49

CASH_PRIZES = {
    500: 10,
    250: 12,
    100: 10,
}
SITE_CREDIT_PRIZES = {25: 40}

cash_ticket_count = sum(CASH_PRIZES.values())
site_credit_ticket_count = sum(SITE_CREDIT_PRIZES.values())
residual_rewards_entries = TOTAL_TICKETS - cash_ticket_count - site_credit_ticket_count
cash_prize_total = sum(value * count for value, count in CASH_PRIZES.items())
site_credit_face_total = sum(value * count for value, count in SITE_CREDIT_PRIZES.items())

# A legal allocation exists in which all of a player's allowed tickets are
# among residual identifiers, because there are far more residual identifiers
# than the 1,000-entry person cap.
assert residual_rewards_entries >= MAX_PER_PERSON
assert cash_ticket_count == 32
assert site_credit_ticket_count == 40
assert residual_rewards_entries == 49_927
assert cash_prize_total == 9_000
assert site_credit_face_total == 1_000

# The separate rewards draw is random; therefore a residual rewards entry has
# a legal non-winning state. Strict cash floor for any <=1000-ticket portfolio
# is consequently zero.
strict_cash_floor_gbp = 0.0
max_paid_spend_gbp = MAX_PER_PERSON * ENTRY_PRICE_GBP
assert max_paid_spend_gbp == 490.0

result = {
    "packet": "H300",
    "total_tickets": TOTAL_TICKETS,
    "max_per_person": MAX_PER_PERSON,
    "entry_price_gbp": ENTRY_PRICE_GBP,
    "cash_ticket_count": cash_ticket_count,
    "site_credit_ticket_count": site_credit_ticket_count,
    "residual_rewards_entries": residual_rewards_entries,
    "cash_prize_total_gbp": cash_prize_total,
    "site_credit_face_total_gbp": site_credit_face_total,
    "max_paid_spend_gbp": max_paid_spend_gbp,
    "strict_withdrawable_cash_floor_gbp": strict_cash_floor_gbp,
    "strict_profit_possible_from_checked_mechanic": False,
}

if __name__ == "__main__":
    import json
    print(json.dumps(result, indent=2))
