from decimal import Decimal, getcontext

getcontext().prec = 28

POSTAGE = Decimal('0.91')
MIN_CASH = Decimal('1.00')
TOTAL_TICKETS = 10000
TOTAL_INSTANT_CASH = Decimal('16719')

PRIZE_COUNTS = {
    Decimal('500'): 5,
    Decimal('250'): 3,
    Decimal('100'): 6,
    Decimal('50'): 12,
    Decimal('25'): 30,
    Decimal('10'): 75,
    Decimal('5'): 150,
    Decimal('2'): 300,
    Decimal('1'): 9419,
}

assert sum(PRIZE_COUNTS.values()) == TOTAL_TICKETS
assert sum(prize * count for prize, count in PRIZE_COUNTS.items()) == TOTAL_INSTANT_CASH
assert min(PRIZE_COUNTS) == MIN_CASH
assert MIN_CASH > POSTAGE

net_floor = MIN_CASH - POSTAGE
gross_ratio = MIN_CASH / POSTAGE
break_even_postage = MIN_CASH

RESULT = {
    'tickets_reconciled': sum(PRIZE_COUNTS.values()),
    'instant_cash_reconciled_gbp': str(sum(prize * count for prize, count in PRIZE_COUNTS.items())),
    'minimum_cash_gbp': str(MIN_CASH),
    'postage_gbp': str(POSTAGE),
    'one_entry_net_floor_gbp': str(net_floor),
    'one_entry_gross_ratio': str(gross_ratio),
    'break_even_postage_gbp': str(break_even_postage),
    'arithmetic_inconclusive': 0,
    'execution_temporal_inconclusive': 1,
    'success': False,
    'reason': 'historical qualifying game; verified current postal terms post-date close and no live equivalent evidenced',
}

if __name__ == '__main__':
    import json
    print(json.dumps(RESULT, indent=2))
