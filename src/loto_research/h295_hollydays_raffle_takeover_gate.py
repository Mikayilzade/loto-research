"""H295: 2026 Hollydays raffle takeover arithmetic gate.

This packet checks the two currently advertised Junior League of Baton Rouge
Hollydays raffles under deliberately player-favourable full-ownership models.
It does not claim that full ownership is executable.
"""

SHOPPING_TICKETS = 500
SHOPPING_TICKET_PRICE = 50
SHOPPING_PRIZE = 10_000

MERCEDES_TICKET_PRICE = 10
MERCEDES_MSRP = 50_605

shopping_cost = SHOPPING_TICKETS * SHOPPING_TICKET_PRICE
shopping_return = SHOPPING_PRIZE / shopping_cost

# Largest integer ticket count N for which MSRP > N * ticket price.
# This deliberately ignores tax, resale friction, and absence of a cash option.
mercedes_strict_positive_max_entries = (MERCEDES_MSRP - 1) // MERCEDES_TICKET_PRICE

assert shopping_cost == 25_000
assert abs(shopping_return - 0.4) < 1e-15
assert mercedes_strict_positive_max_entries == 5_060
assert MERCEDES_MSRP > mercedes_strict_positive_max_entries * MERCEDES_TICKET_PRICE
assert MERCEDES_MSRP <= (mercedes_strict_positive_max_entries + 1) * MERCEDES_TICKET_PRICE

if __name__ == "__main__":
    print({
        "shopping_full_takeover_cost": shopping_cost,
        "shopping_prize": SHOPPING_PRIZE,
        "shopping_gross_return": shopping_return,
        "mercedes_ticket_price": MERCEDES_TICKET_PRICE,
        "mercedes_msrp": MERCEDES_MSRP,
        "mercedes_strict_positive_max_entries_before_tax_or_resale": mercedes_strict_positive_max_entries,
    })
