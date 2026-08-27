"""H324: exact cap/takeover bounds for selected live Click Competitions pools.

The target is strict guaranteed profit, not positive EV.  For a k-winner draw,
if at least k valid external entries can remain, there is a legal outcome in
which every winner is external.  For single-winner paid draws, a per-person
cap below the finite pool similarly leaves a legal external winner; full-pool
arithmetic is also reported as a deliberately stronger-than-real check.
"""
from dataclasses import dataclass, asdict
import json

@dataclass(frozen=True)
class Case:
    name: str
    pool: int
    sold_snapshot: int
    player_cap: int
    winners: int
    ticket_price_gbp: float
    total_prize_gbp: float

CASES = [
    Case("Click free £10k / 40 winners", 300_000, 2_367, 49, 40, 0.0, 10_000.0),
    Case("Click £1k LOW ODDS", 149, 0, 5, 1, 9.99, 1_000.0),
    Case("Click £10k for 2p", 1_189_995, 43_224, 50_000, 1, 0.02, 10_000.0),
    Case("Click £20k for 2p", 1_749_999, 1_055_034, 50_000, 1, 0.02, 20_000.0),
]

def evaluate(c: Case):
    minimum_external_already_sold = max(0, c.sold_snapshot - c.player_cap)
    cap_fraction = c.player_cap / c.pool
    full_cost = c.pool * c.ticket_price_gbp
    full_buyout_ratio = None if full_cost == 0 else c.total_prize_gbp / full_cost
    # For the free 40-winner snapshot this already proves a zero cash floor.
    snapshot_external_can_fill_all_winner_slots = minimum_external_already_sold >= c.winners
    # For every case cap < pool, so a one-player takeover of all possible winning IDs is impossible.
    one_player_full_takeover_possible = c.player_cap >= c.pool
    return {
        **asdict(c),
        "minimum_external_already_sold": minimum_external_already_sold,
        "cap_fraction": cap_fraction,
        "snapshot_external_can_fill_all_winner_slots": snapshot_external_can_fill_all_winner_slots,
        "one_player_full_takeover_possible": one_player_full_takeover_possible,
        "full_pool_cost_gbp": full_cost,
        "full_buyout_ratio": full_buyout_ratio,
    }

def main():
    rows = [evaluate(c) for c in CASES]
    free = rows[0]
    assert free["minimum_external_already_sold"] == 2318
    assert free["minimum_external_already_sold"] >= 40
    assert not free["one_player_full_takeover_possible"]
    assert abs(rows[1]["full_pool_cost_gbp"] - 1488.51) < 1e-9
    assert rows[1]["full_buyout_ratio"] < 1
    assert abs(rows[2]["full_pool_cost_gbp"] - 23799.90) < 1e-9
    assert rows[2]["full_buyout_ratio"] < 1
    assert abs(rows[3]["full_pool_cost_gbp"] - 34999.98) < 1e-9
    assert rows[3]["full_buyout_ratio"] < 1
    assert all(not r["one_player_full_takeover_possible"] for r in rows)
    print(json.dumps({"packet":"H324","cases":rows}, indent=2))

if __name__ == "__main__":
    main()
