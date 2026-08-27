"""H311: exact structural bounds for Kilted Lucky Dips current finite pool.

Snapshot checked 2026-08-27 from the operator page.
This deliberately uses a player-favourable liability interpretation:
£200,000 stated instant-win prize pot PLUS the separately stated £1,000 cash
end prize.  If the £1,000 is already included in the £200,000 headline, the
full-pool gross is exactly break-even rather than +0.5%; either reading is
irrelevant to the strict-guarantee result because the 499-person cap prevents
full ownership.
"""

TOTAL_TICKETS = 10_000
PRICE_PER_TICKET = 20.0
MAX_PER_PERSON = 499
SNAPSHOT_SOLD = 1_215
STATED_INSTANT_PRIZE_POT = 200_000.0
END_CASH_PRIZE = 1_000.0

full_cost = TOTAL_TICKETS * PRICE_PER_TICKET
favourable_total_liability = STATED_INSTANT_PRIZE_POT + END_CASH_PRIZE
favourable_full_pool_ratio = favourable_total_liability / full_cost
max_control_fraction = MAX_PER_PERSON / TOTAL_TICKETS
min_external_existing_if_incumbent_player = max(0, SNAPSHOT_SOLD - MAX_PER_PERSON)
remaining = TOTAL_TICKETS - SNAPSHOT_SOLD

# Basic exact facts.
assert full_cost == 200_000.0
assert favourable_total_liability == 201_000.0
assert abs(favourable_full_pool_ratio - 1.005) < 1e-12
assert MAX_PER_PERSON < TOTAL_TICKETS
assert min_external_existing_if_incumbent_player == 716
assert remaining == 8_785

# Structural strict-guarantee blocker: even granting one player the maximum
# 499 already-sold entries, at least 716 currently sold identifiers are
# external.  The end-draw RNG can legally select one of those external IDs.
# Therefore the £1,000 end-prize contribution has worst-case floor zero for
# any single-account strategy.  Full-pool takeover is impossible under the
# published cap.
closure = {
    "packet": "H311",
    "total_tickets": TOTAL_TICKETS,
    "price_per_ticket_gbp": PRICE_PER_TICKET,
    "full_cost_gbp": full_cost,
    "max_per_person": MAX_PER_PERSON,
    "max_control_fraction": max_control_fraction,
    "snapshot_sold": SNAPSHOT_SOLD,
    "remaining": remaining,
    "min_external_existing_even_if_player_owned_499_sold": min_external_existing_if_incumbent_player,
    "stated_instant_prize_pot_gbp": STATED_INSTANT_PRIZE_POT,
    "end_cash_prize_gbp": END_CASH_PRIZE,
    "player_favourable_total_liability_gbp": favourable_total_liability,
    "player_favourable_full_pool_ratio": favourable_full_pool_ratio,
    "full_takeover_allowed": False,
    "strict_guaranteed_profit_from_takeover": False,
    "status": "CLOSED / TAKEOVER-BLOCKED",
}

if __name__ == "__main__":
    import json
    print(json.dumps(closure, indent=2, sort_keys=True))
