from decimal import Decimal

PRIZES = [
    (Decimal("20.00"), 1),
    (Decimal("1.00"), 5),
    (Decimal("0.50"), 5),
    (Decimal("0.20"), 10),
    (Decimal("0.10"), 79),
]


def validate():
    prize_identifiers = sum(count for _, count in PRIZES)
    aggregate_site_credit = sum(value * count for value, count in PRIZES)
    minimum_face_value = min(value for value, _ in PRIZES)

    total_identifiers = 100
    zero_prize_identifiers = total_identifiers - prize_identifiers

    binding_zero_cost_online_free_route = False
    unconditional_site_credit_cashout = False
    minimum_withdrawable_cash = Decimal("0.00")

    assert prize_identifiers == total_identifiers == 100
    assert zero_prize_identifiers == 0
    assert aggregate_site_credit == Decimal("37.40")
    assert minimum_face_value == Decimal("0.10")
    assert binding_zero_cost_online_free_route is False
    assert unconditional_site_credit_cashout is False
    assert minimum_withdrawable_cash == Decimal("0.00")

    return {
        "total_identifiers": total_identifiers,
        "prize_identifiers": prize_identifiers,
        "zero_prize_identifiers": zero_prize_identifiers,
        "aggregate_site_credit_gbp": str(aggregate_site_credit),
        "minimum_site_credit_face_value_gbp": str(minimum_face_value),
        "binding_zero_cost_online_free_route": binding_zero_cost_online_free_route,
        "unconditional_site_credit_cashout": unconditional_site_credit_cashout,
        "minimum_withdrawable_cash_gbp": str(minimum_withdrawable_cash),
        "strict_positive_cash_guarantee": False,
        "arithmetic_inconclusive": 0,
        "route_inconclusive_relevant_to_closure": 0,
        "prize_convertibility_inconclusive_relevant_to_closure": 0,
    }


if __name__ == "__main__":
    print(validate())
