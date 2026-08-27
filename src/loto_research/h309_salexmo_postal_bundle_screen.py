from math import ceil

STAMP_GBP = 0.91

CASES = [
    {
        'name': 'Salexmo £2,000 cash 4 Sep 2026',
        'entries': 200_000,
        'max_per_user': 50_000,
        'postal_entries_per_card': 43,
        'paid_price': 0.02,
        'total_player_liability': 2_000.0,
        'sold_snapshot': 25_650,
    },
    {
        'name': 'Salexmo £900 + 10x£90 2 Sep 2026',
        'entries': 40_000,
        'max_per_user': 10_000,
        'postal_entries_per_card': 10,
        'paid_price': 0.09,
        'total_player_liability': 1_800.0,
        'sold_snapshot': 3_808,
    },
    {
        'name': 'Salexmo £10,000 instant pot + £2,000 end prize 17 Sep 2026',
        'entries': 12_000,
        'max_per_user': 2_500,
        'postal_entries_per_card': 1,
        'paid_price': 2.00,
        'total_player_liability': 12_000.0,
        'sold_snapshot': 728,
    },
    {
        'name': 'Salexmo £12,500 instant pot + £500 end prize 7 Sep 2026',
        'entries': 866_666,
        'max_per_user': 150_000,
        'postal_entries_per_card': 29,
        'paid_price': 0.03,
        'total_player_liability': 13_000.0,
        'sold_snapshot': 39_516,
    },
]


def analyze(c):
    n = c['entries']
    bundle = c['postal_entries_per_card']
    cards_full = ceil(n / bundle)
    postal_full_cost = cards_full * STAMP_GBP
    paid_full_cost = n * c['paid_price']
    return {
        **c,
        'control_fraction_cap': c['max_per_user'] / n,
        'already_sold_fraction': c['sold_snapshot'] / n,
        'hypothetical_full_postal_cards': cards_full,
        'hypothetical_full_postal_cost': postal_full_cost,
        'hypothetical_full_postal_return_ratio': c['total_player_liability'] / postal_full_cost,
        'paid_full_cost': paid_full_cost,
        'paid_full_return_ratio': c['total_player_liability'] / paid_full_cost,
        'strict_takeover_possible_now': c['max_per_user'] >= n and c['sold_snapshot'] == 0,
    }


if __name__ == '__main__':
    rows = [analyze(c) for c in CASES]
    # Exact sanity checks used by the H309 report.
    assert rows[0]['control_fraction_cap'] == 0.25
    assert rows[1]['control_fraction_cap'] == 0.25
    assert rows[2]['control_fraction_cap'] == 2_500 / 12_000
    assert rows[2]['hypothetical_full_postal_cost'] == 10_920.0
    assert rows[2]['total_player_liability'] == 12_000.0
    assert rows[2]['hypothetical_full_postal_return_ratio'] > 1.0
    assert all(not r['strict_takeover_possible_now'] for r in rows)
    for r in rows:
        print(r)
