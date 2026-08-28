from decimal import Decimal, ROUND_CEILING

STAMP = Decimal("0.91")
TICKET_PRICE = Decimal("0.15")
MIN_ADVERTISED_WIN = Decimal("0.03")


def validate():
    k = int((STAMP / TICKET_PRICE).to_integral_value(rounding=ROUND_CEILING))
    favorable_bundle_cash = Decimal(k) * MIN_ADVERTISED_WIN
    net_before_materials = favorable_bundle_cash - STAMP

    assert k == 7
    assert favorable_bundle_cash == Decimal("0.21")
    assert net_before_materials == Decimal("-0.70")
    assert favorable_bundle_cash < STAMP

    return {
        "stamp_gbp": str(STAMP),
        "ticket_price_gbp": str(TICKET_PRICE),
        "bundle_size": k,
        "minimum_advertised_win_gbp": str(MIN_ADVERTISED_WIN),
        "favorable_all_cash_bundle_floor_gbp": str(favorable_bundle_cash),
        "net_before_materials_gbp": str(net_before_materials),
        "strict_positive_guarantee_possible": False,
        "arithmetic_inconclusive": 0,
        "closure_relevant_inconclusive": 0,
    }


if __name__ == "__main__":
    print(validate())
