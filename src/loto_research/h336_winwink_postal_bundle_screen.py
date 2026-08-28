from decimal import Decimal

STAMP = Decimal('0.91')
TICKET_PRICE = Decimal('2.50')
TOTAL_IDS = 7274

PRIZES = [
    ('Shiny Charizard GX PSA 10', 1, Decimal('916')),
    ('Charizard EX PSA 10', 1, Decimal('541')),
    ('Charizard V ACE 10', 1, Decimal('250')),
    ('Charizard SWSH260 ACE 10', 1, Decimal('217')),
    ('Charizard VStar Japanese PSA 10', 1, Decimal('167')),
    ('100 cash', 3, Decimal('100')),
    ('Crown Zenith PSA 10', 1, Decimal('75')),
    ('Charizard Promo PSA 9', 1, Decimal('67')),
    ('Rainbow PSA 9', 1, Decimal('62')),
    ('50 cash', 8, Decimal('50')),
    ('25 cash', 20, Decimal('25')),
    ('20 cash', 15, Decimal('20')),
    ('10 cash', 60, Decimal('10')),
    ('5 credit cash alternative', 200, Decimal('4')),
    ('2 credit cash alternative', 800, Decimal('2')),
    ('1 credit cash alternative', 1500, Decimal('1')),
    ('50p credit cash alternative', 1445, Decimal('0.42')),
    ('10p credit cash alternative', 3215, Decimal('0.08')),
]

count_sum = sum(n for _, n, _ in PRIZES)
cash_liability = sum(Decimal(n) * cash for _, n, cash in PRIZES)
postal_tickets = max(1, int(STAMP // TICKET_PRICE))
minimum_cash = min(cash for _, _, cash in PRIZES)
worst_net = minimum_cash - STAMP

assert count_sum == TOTAL_IDS
assert cash_liability == Decimal('9159.10')
assert postal_tickets == 1
assert minimum_cash == Decimal('0.08')
assert worst_net == Decimal('-0.83')
assert worst_net < 0

RESULT = {
    'identifier_count': count_sum,
    'all_cash_alternative_liability_gbp': str(cash_liability),
    'postal_tickets_per_submission': postal_tickets,
    'minimum_cash_gbp': str(minimum_cash),
    'stamp_gbp': str(STAMP),
    'worst_case_net_before_materials_gbp': str(worst_net),
    'arithmetic_inconclusive': 0,
    'strict_guaranteed_profit': False,
}

if __name__ == '__main__':
    print(RESULT)
