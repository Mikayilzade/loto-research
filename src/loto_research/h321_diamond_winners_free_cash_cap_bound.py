"""H321: exact one-player guarantee bound for Diamond Winners £100 free giveaway.

The live competition advertises a 100% off electronic discount code, but caps
entries at one per person.  The main draw is from valid Entrants, not from
unsold ticket identifiers.  A strict one-player cash guarantee therefore
requires owning every valid entry at draw time.  Once any external valid entry
exists, an external-winner state is legal and the player's cash floor is zero.
"""
from __future__ import annotations
import json
from pathlib import Path

TOTAL_TICKET_CAP = 1000
MAX_PER_PERSON = 1
CASH_PRIZE_GBP = 100.0
LIST_PRICE_GBP = 10.0
DISCOUNT_FRACTION = 1.0
# Fresh 2026-08-28 snapshot seen on the operator page during H321.
OBSERVED_ENTRIES = 178


def main() -> None:
    effective_entry_cost = LIST_PRICE_GBP * (1.0 - DISCOUNT_FRACTION)
    minimum_external_entries_now = max(0, OBSERVED_ENTRIES - MAX_PER_PERSON)
    max_identifier_share = MAX_PER_PERSON / TOTAL_TICKET_CAP

    # Stronger than needed: even if the player already owned one of the
    # observed entries, at least 177 observed valid entries remain external.
    assert minimum_external_entries_now == 177
    assert max_identifier_share == 0.001
    assert effective_entry_cost == 0.0

    # Main-draw rules choose among valid entrants.  With >=1 external entrant,
    # there is a legal state where that external entrant wins, giving us £0.
    external_winner_state_exists = minimum_external_entries_now >= 1
    strict_withdrawable_cash_floor = 0.0 if external_winner_state_exists else CASH_PRIZE_GBP
    assert external_winner_state_exists
    assert strict_withdrawable_cash_floor == 0.0

    out = {
        "packet": "H321",
        "mechanism": "electronic_100pct_discount_finite_cash_draw",
        "snapshot_date": "2026-08-28",
        "total_ticket_cap": TOTAL_TICKET_CAP,
        "max_entries_per_person": MAX_PER_PERSON,
        "observed_valid_entries": OBSERVED_ENTRIES,
        "minimum_external_entries_even_if_player_already_holds_one": minimum_external_entries_now,
        "list_price_gbp": LIST_PRICE_GBP,
        "discount_fraction": DISCOUNT_FRACTION,
        "effective_entry_cost_gbp": effective_entry_cost,
        "cash_prize_gbp": CASH_PRIZE_GBP,
        "max_share_of_advertised_identifier_space": max_identifier_share,
        "external_winner_state_exists": external_winner_state_exists,
        "strict_withdrawable_cash_floor_gbp": strict_withdrawable_cash_floor,
        "terminal": True,
        "closure_reason": "one-entry person cap plus already-existing external entrants leaves a legal external-winner state",
    }
    root = Path(__file__).resolve().parents[2]
    p = root / "data" / "derived" / "h321_diamond_winners_free_cash_cap_bound.json"
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(out, indent=2) + "\n")
    print(json.dumps(out, indent=2))


if __name__ == "__main__":
    main()
