from decimal import Decimal

STAMP = Decimal('0.91')
TICKET_PRICE = Decimal('0.30')
TOTAL_IDS = 122667
INSTANT_WIN_IDS = 13673

postal_tickets = max(1, int(STAMP // TICKET_PRICE))
losing_ids = TOTAL_IDS - INSTANT_WIN_IDS
worst_bundle_cash = Decimal('0') if losing_ids >= postal_tickets else None
worst_net = worst_bundle_cash - STAMP if worst_bundle_cash is not None else None

assert postal_tickets == 3
assert losing_ids == 108994
assert losing_ids >= postal_tickets
assert worst_bundle_cash == Decimal('0')
assert worst_net == Decimal('-0.91')

RESULT = {
    'total_identifiers': TOTAL_IDS,
    'instant_win_identifiers': INSTANT_WIN_IDS,
    'zero_instant_identifiers': losing_ids,
    'stamp_gbp': str(STAMP),
    'ticket_price_gbp': str(TICKET_PRICE),
    'postal_tickets_per_submission': postal_tickets,
    'worst_bundle_withdrawable_cash_gbp': str(worst_bundle_cash),
    'worst_case_net_before_materials_gbp': str(worst_net),
    'arithmetic_inconclusive': 0,
    'strict_guaranteed_profit': False,
}

if __name__ == '__main__':
    print(RESULT)
