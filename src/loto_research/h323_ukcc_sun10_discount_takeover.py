"""H323: exact finite-pool economics for the current UKCC VW Crafter + Mercedes GLC draw.

This deliberately grants the player impossible-perfect ownership of every ticket at the
published SUN10 promotional price, then separately checks the real per-person cap.
"""

TOTAL_TICKETS = 499_999
BASE_PRICE_GBP = 0.79
SUN10_PRICE_GBP = 0.71
CASH_ALTERNATIVE_GBP = 140_000
MAX_PER_PERSON = 950
SNAPSHOT_SOLD = 37_281


def main():
    base_full_cost = TOTAL_TICKETS * BASE_PRICE_GBP
    discounted_full_cost = TOTAL_TICKETS * SUN10_PRICE_GBP
    full_buyout_ratio = CASH_ALTERNATIVE_GBP / discounted_full_cost
    break_even_ticket_price = CASH_ALTERNATIVE_GBP / TOTAL_TICKETS
    required_discount_from_base = 1 - break_even_ticket_price / BASE_PRICE_GBP
    required_further_discount_from_sun10 = 1 - break_even_ticket_price / SUN10_PRICE_GBP
    max_control_fraction = MAX_PER_PERSON / TOTAL_TICKETS

    assert round(base_full_cost, 2) == 394_999.21
    assert round(discounted_full_cost, 2) == 354_999.29
    assert abs(full_buyout_ratio - 0.3943669859170704) < 1e-15
    assert MAX_PER_PERSON < TOTAL_TICKETS
    assert SNAPSHOT_SOLD > MAX_PER_PERSON
    assert discounted_full_cost > CASH_ALTERNATIVE_GBP

    print({
        'packet': 'H323',
        'total_tickets': TOTAL_TICKETS,
        'sun10_full_cost_gbp': round(discounted_full_cost, 2),
        'cash_alternative_gbp': CASH_ALTERNATIVE_GBP,
        'impossible_full_buyout_gross_ratio': full_buyout_ratio,
        'break_even_ticket_price_gbp': break_even_ticket_price,
        'required_discount_from_base': required_discount_from_base,
        'required_further_discount_from_sun10': required_further_discount_from_sun10,
        'max_per_person': MAX_PER_PERSON,
        'max_control_fraction': max_control_fraction,
        'snapshot_sold': SNAPSHOT_SOLD,
        'strict_worst_case_cash_floor_gbp': 0,
    })


if __name__ == '__main__':
    main()
