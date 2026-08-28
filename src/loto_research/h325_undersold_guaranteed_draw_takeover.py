"""H325: deterministic takeover gates for undersold guaranteed finite draws.

For a single-winner finite draw, strict one-player takeover requires control of
ALL valid identifiers.  If at least one valid external entry already exists,
a legal external-winning outcome remains.  If none exist yet, max_per_player
must be at least the full finite universe N.  Only after those structural gates
pass does prize > acquisition cost become relevant.
"""
from dataclasses import dataclass, asdict
import json

@dataclass(frozen=True)
class Draw:
    name: str
    n: int
    sold: int
    price: float
    liability: float
    max_per_player: int

DRAWS = [
    Draw("Elite £101,000 Cash", 4_999_999, 1, 0.05, 101_000.0, 20_000),
    Draw("Clubhouse £250 Flash Cash", 499, 1, 1.00, 250.0, 49),
    Draw("Competition Go £500", 180, 1, 5.00, 500.0, 12),
    Draw("Caddy £3k Mega Bundle", 21_999, 1, 0.33, 3_000.0, 1_467),
    Draw("Competition Go TUI + instants", 21_600, 1, 0.25, 3_000.0, 1_510),
]

def evaluate(d: Draw):
    full_cost = d.n * d.price
    remaining = d.n - d.sold
    full_buyout_ratio = d.liability / full_cost
    control_fraction = min(d.max_per_player, d.n) / d.n
    external_entry_block = d.sold > 0
    cap_block = d.max_per_player < d.n
    strict_takeover_possible = (not external_entry_block) and (not cap_block)
    strict_profit_possible = strict_takeover_possible and d.liability > full_cost
    return {
        **asdict(d),
        "remaining": remaining,
        "full_cost": round(full_cost, 8),
        "full_buyout_ratio": full_buyout_ratio,
        "control_fraction": control_fraction,
        "external_entry_block": external_entry_block,
        "cap_block": cap_block,
        "strict_takeover_possible": strict_takeover_possible,
        "strict_profit_possible": strict_profit_possible,
        "strict_cash_floor_if_external_winner_legal": 0.0,
    }

if __name__ == "__main__":
    out = [evaluate(d) for d in DRAWS]
    assert all(x["external_entry_block"] for x in out)
    assert all(x["cap_block"] for x in out)
    assert all(not x["strict_takeover_possible"] for x in out)
    assert all(not x["strict_profit_possible"] for x in out)
    # Even impossible full ownership is below break-even for all five screens.
    assert max(x["full_buyout_ratio"] for x in out) < 1.0
    print(json.dumps(out, indent=2))
