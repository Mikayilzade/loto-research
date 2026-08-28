from decimal import Decimal, getcontext

getcontext().prec = 28

POSTAGE = Decimal('0.91')
MIN_CASH = Decimal('1.00')
TOTAL_IDS = 15125
LIVE_SOLD = 2840

PRIZE_COUNTS = {
    Decimal('300'): 6,
    Decimal('200'): 6,
    Decimal('100'): 6,
    Decimal('50'): 10,
    Decimal('25'): 12,
    Decimal('15'): 15,
    Decimal('10'): 20,
    Decimal('5'): 50,
    Decimal('1'): 15000,
}

count_total = sum(PRIZE_COUNTS.values())
cash_total = sum(prize * count for prize, count in PRIZE_COUNTS.items())
min_cash = min(PRIZE_COUNTS)

assert count_total == TOTAL_IDS
assert cash_total == Decimal('20075')
assert min_cash == MIN_CASH
assert LIVE_SOLD <= TOTAL_IDS
assert MIN_CASH > POSTAGE

stamp_only_net = MIN_CASH - POSTAGE
stamp_only_ratio = MIN_CASH / POSTAGE
max_nonstamp_cost = MIN_CASH - POSTAGE

RESULT = {
    'total_ids': TOTAL_IDS,
    'live_sold_snapshot': LIVE_SOLD,
    'prize_ids_reconciled': count_total,
    'instant_cash_reconciled_gbp': str(cash_total),
    'minimum_cash_gbp': str(min_cash),
    'postage_gbp': str(POSTAGE),
    'stamp_only_net_floor_gbp': str(stamp_only_net),
    'stamp_only_gross_ratio': str(stamp_only_ratio),
    'maximum_nonstamp_cost_for_strict_profit_gbp': str(max_nonstamp_cost),
    'arithmetic_inconclusive': 0,
    'execution_inconclusive': 2,
    'success': False,
    'reason': 'all-in compliant A5-postcard execution below £1 and unconditional acceptance are not yet rigorously established; UK-resident eligibility applies',
}

if __name__ == '__main__':
    import json
    print(json.dumps(RESULT, indent=2))
