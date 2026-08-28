"""H344 exact closure model for LDG Every Ticket Wins - PRIZE GRABBER."""

TOTAL_IDS = 81_020
CASH_50P_IDS = 80_000
CASH_5_IDS = 1_000
PRIZE_GRABBER_IDS = 20
TICKET_PRICE_GBP = 1.99
SECOND_CLASS_POSTAGE_GBP = 0.91
MIN_ORDINARY_CASH_GBP = 0.50


def main() -> None:
    reconciled = CASH_50P_IDS + CASH_5_IDS + PRIZE_GRABBER_IDS
    assert reconciled == TOTAL_IDS
    assert TICKET_PRICE_GBP > SECOND_CLASS_POSTAGE_GBP

    allocated_tickets_per_postal_submission = 1
    ordinary_cash_net_floor = (
        allocated_tickets_per_postal_submission * MIN_ORDINARY_CASH_GBP
        - SECOND_CLASS_POSTAGE_GBP
    )
    assert ordinary_cash_net_floor == -0.41

    # Governing terms say physical prizes have no cash alternative unless stated.
    # Therefore the strict withdrawable-cash floor over all identifiers is <= 0.
    strict_withdrawable_cash_floor = 0.0
    strict_net_floor = strict_withdrawable_cash_floor - SECOND_CLASS_POSTAGE_GBP
    assert strict_net_floor == -0.91

    print({
        "total_ids": TOTAL_IDS,
        "reconciled_ids": reconciled,
        "ordinary_cash_ids": CASH_50P_IDS + CASH_5_IDS,
        "special_noncash_capable_ids": PRIZE_GRABBER_IDS,
        "allocated_tickets_per_postal_submission": allocated_tickets_per_postal_submission,
        "ordinary_cash_net_floor_gbp": ordinary_cash_net_floor,
        "strict_net_floor_gbp": strict_net_floor,
        "arithmetic_inconclusive": 0,
        "closure_relevant_inconclusive": 0,
        "closed_not_success": True,
    })


if __name__ == "__main__":
    main()
