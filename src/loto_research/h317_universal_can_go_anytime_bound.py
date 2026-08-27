from decimal import Decimal

TOTAL = 3999
SOLD = 1135
PRICE = Decimal('0.10')
INSTANT_CASH = Decimal('100')
# Deliberately player-favourable: title advertises a £100 Cash Jackpot and the body
# says a jackpot winner is drawn from entries sold up to the instant-cash hit.
JACKPOT_UPPER = Decimal('100')

full_cost = Decimal(TOTAL) * PRICE
remaining = TOTAL - SOLD
remaining_cost = Decimal(remaining) * PRICE
favourable_total_liability = INSTANT_CASH + JACKPOT_UPPER

assert TOTAL == 3999
assert remaining == 2864
assert full_cost == Decimal('399.90')
assert remaining_cost == Decimal('286.40')
assert favourable_total_liability == Decimal('200')
assert favourable_total_liability < remaining_cost
assert favourable_total_liability < full_cost

print({
    'packet': 'H317',
    'total_identifiers': TOTAL,
    'snapshot_sold': SOLD,
    'remaining_identifiers': remaining,
    'ticket_price_gbp': str(PRICE),
    'full_pool_cost_gbp': str(full_cost),
    'remaining_tail_cost_gbp': str(remaining_cost),
    'player_favourable_liability_upper_gbp': str(favourable_total_liability),
    'full_pool_gross_ratio': float(favourable_total_liability / full_cost),
    'remaining_tail_gross_ratio': float(favourable_total_liability / remaining_cost),
    'strict_profit_possible_under_full_tail_takeover': False,
})
