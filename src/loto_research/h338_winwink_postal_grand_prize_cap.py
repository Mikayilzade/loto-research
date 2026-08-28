from decimal import Decimal

STAMP = Decimal('0.91')
TICKET_PRICE = Decimal('0.20')
K = int(STAMP // TICKET_PRICE)

CANDIDATES = [
    {'name': 'Armageddon', 'N': 2000, 'cap': 300},
    {'name': 'Necromunda', 'N': 1000, 'cap': 150},
]

assert K == 4

results = []
for c in CANDIDATES:
    external = c['N'] - c['cap']
    assert c['cap'] < c['N']
    assert external > 0
    strict_cash_floor = Decimal('0')
    strict_net_before_materials = strict_cash_floor - STAMP
    assert strict_net_before_materials < 0
    results.append({
        'name': c['name'],
        'total_identifiers': c['N'],
        'per_person_cap': c['cap'],
        'minimum_external_identifiers': external,
        'postal_tickets_per_submission': K,
        'strict_cash_floor_gbp': str(strict_cash_floor),
        'strict_net_before_materials_gbp': str(strict_net_before_materials),
    })

RESULT = {
    'postal_tickets_per_submission': K,
    'candidates': results,
    'arithmetic_inconclusive': 0,
    'strict_guaranteed_profit': False,
}

if __name__ == '__main__':
    print(RESULT)
