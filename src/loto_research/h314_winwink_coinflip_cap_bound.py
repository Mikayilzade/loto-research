"""H314: exact worst-case cap bound for WinWink £50k COIN FLIP (2026-08-27 snapshot).

The live game publishes a finite ticket space and a precommitted set of instant-win
positions.  A player cannot see/select those positions before purchase and is capped
at 21,429 tickets.  If the number of remaining non-winning positions is at least the
player cap, there is a legal allocation in which every ticket bought by the player is
non-winning, so the strict guaranteed cash floor is zero.
"""
from __future__ import annotations
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "data" / "derived" / "h314_winwink_coinflip_cap_bound.json"

TOTAL_TICKETS = 142_857
TOTAL_INSTANT_WIN_POSITIONS = 71_428
PLAYER_CAP = 21_429
TICKET_PRICE_GBP = 1.0

# Fresh operator-page snapshot captured 2026-08-27.
SOLD = 1_615
INSTANT_WINS_REMAINING = 70_598


def build_result() -> dict:
    remaining_tickets = TOTAL_TICKETS - SOLD
    total_nonwinning_positions = TOTAL_TICKETS - TOTAL_INSTANT_WIN_POSITIONS
    instant_wins_claimed = TOTAL_INSTANT_WIN_POSITIONS - INSTANT_WINS_REMAINING

    # Since every claimed instant win necessarily consumed one sold ticket, the
    # remaining non-winning count is exact from the published aggregate counts.
    nonwinning_sold = SOLD - instant_wins_claimed
    nonwinning_remaining = total_nonwinning_positions - nonwinning_sold

    assert remaining_tickets == INSTANT_WINS_REMAINING + nonwinning_remaining
    assert nonwinning_remaining >= PLAYER_CAP

    max_player_spend = PLAYER_CAP * TICKET_PRICE_GBP
    strict_cash_floor = 0.0

    return {
        "packet": "H314",
        "game": "WinWink £50k COIN FLIP",
        "snapshot_date": "2026-08-27",
        "total_tickets": TOTAL_TICKETS,
        "total_instant_win_positions": TOTAL_INSTANT_WIN_POSITIONS,
        "total_nonwinning_positions": total_nonwinning_positions,
        "sold": SOLD,
        "instant_wins_remaining": INSTANT_WINS_REMAINING,
        "instant_wins_claimed": instant_wins_claimed,
        "nonwinning_sold": nonwinning_sold,
        "remaining_tickets": remaining_tickets,
        "nonwinning_remaining": nonwinning_remaining,
        "player_cap": PLAYER_CAP,
        "ticket_price_gbp": TICKET_PRICE_GBP,
        "max_player_spend_gbp": max_player_spend,
        "nonwinning_remaining_minus_cap": nonwinning_remaining - PLAYER_CAP,
        "strict_guaranteed_cash_floor_gbp": strict_cash_floor,
        "closure": "CAP-BLOCKED / ZERO STRICT CASH FLOOR",
        "proof": (
            "The operator precommits instant-win ticket positions, keeps them hidden "
            "until purchase, and caps one player at 21,429 tickets. At the snapshot, "
            "70,644 non-winning positions remain, more than enough to contain every "
            "ticket the player is permitted to buy. Therefore a legal outcome exists "
            "where all of the player's tickets are non-winning."
        ),
    }


def main() -> None:
    d = build_result()
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(d, indent=2) + "\n")
    print(json.dumps(d, indent=2))


if __name__ == "__main__":
    main()
