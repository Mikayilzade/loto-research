"""H310: exact takeover blocker for Reel Raffle free app cash draw.

Snapshot: 2026-08-27, current APP EXCLUSIVE £1000 Cash for FREE.
This is a guarantee analysis, not EV optimization.
"""

TOTAL_TICKETS = 99_999
MAX_PER_PERSON = 50
SNAPSHOT_ENTRIES = 10_585
ENTRY_PRICE_GBP = 0.0
CASH_PRIZE_GBP = 1_000.0

assert SNAPSHOT_ENTRIES > MAX_PER_PERSON
assert MAX_PER_PERSON < TOTAL_TICKETS

# For any single entrant, at most MAX_PER_PERSON of already-entered tickets can
# belong to that entrant. Therefore at least this many existing entered tickets
# are necessarily external to that entrant at the snapshot.
MIN_EXISTING_EXTERNAL = SNAPSHOT_ENTRIES - MAX_PER_PERSON
assert MIN_EXISTING_EXTERNAL == 10_535

# Even if the entrant receives the full allowed 50 tickets, a legal draw can
# select one of the already-existing external tickets. Hence the strict cash
# floor is zero.
STRICT_GUARANTEED_CASH_GBP = 0.0
STRICT_GUARANTEED_PROFIT_GBP = 0.0

# Ownership ceiling of the advertised finite identifier space.
MAX_IDENTIFIER_SHARE = MAX_PER_PERSON / TOTAL_TICKETS
assert MAX_IDENTIFIER_SHARE < 0.001

if __name__ == "__main__":
    print({
        "total_tickets": TOTAL_TICKETS,
        "max_per_person": MAX_PER_PERSON,
        "snapshot_entries": SNAPSHOT_ENTRIES,
        "min_existing_external": MIN_EXISTING_EXTERNAL,
        "max_identifier_share": MAX_IDENTIFIER_SHARE,
        "strict_guaranteed_cash_gbp": STRICT_GUARANTEED_CASH_GBP,
        "strict_guaranteed_profit_gbp": STRICT_GUARANTEED_PROFIT_GBP,
    })
