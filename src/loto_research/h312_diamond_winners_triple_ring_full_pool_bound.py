"""H312: exact full-pool liability bound for Diamond Winners Triple Ring Winner.

Player-favourable model: every published instant liability is valued at full face
value, including rings at the operator's stated insured value and site credit at
100% cash-equivalent face value. If even this upper bound is below acquisition
cost, the current finite-pool takeover cannot guarantee profit.
"""
from decimal import Decimal

N = 9999
PRICE = Decimal('1.99')
RING_VALUE = Decimal('2150')

LIABILITIES = {
    'rings_3x2150': Decimal(3) * RING_VALUE,
    'cash_2x500': Decimal(2) * Decimal('500'),
    'cash_4x250': Decimal(4) * Decimal('250'),
    'cash_10x100': Decimal(10) * Decimal('100'),
    'cash_20x50': Decimal(20) * Decimal('50'),
    'cash_100x10': Decimal(100) * Decimal('10'),
    'cash_1000x1': Decimal(1000) * Decimal('1'),
    'site_credit_1000x0_50': Decimal(1000) * Decimal('0.50'),
    'site_credit_5000x0_10': Decimal(5000) * Decimal('0.10'),
}

cost = Decimal(N) * PRICE
liability = sum(LIABILITIES.values(), Decimal('0'))
ratio = liability / cost
deficit = cost - liability

assert cost == Decimal('19898.01')
assert liability == Decimal('13450.00')
assert deficit == Decimal('6448.01')
assert ratio < 1

if __name__ == '__main__':
    print('tickets', N)
    print('cost', cost)
    print('favourable_liability', liability)
    print('gross_ratio', ratio)
    print('deficit', deficit)
