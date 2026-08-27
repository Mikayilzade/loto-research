"""H305: exact cap/full-pool screen for current The Giveaway Guys cash draws.

The strict-guarantee test is deliberately player-favourable: all published entries
up to the per-person cap are assumed obtainable.  If cap < pool size, at least one
external identifier remains a legal winner, hence the guaranteed cash floor from
the draw is zero.  We also report impossible full-buyout economics as a secondary
screen.
"""
from dataclasses import dataclass, asdict
import json
from pathlib import Path

@dataclass(frozen=True)
class Draw:
    name: str
    tickets: int
    max_per_person: int
    price_gbp: float
    cash_prize_gbp: float
    draw_date: str

DRAWS = [
    Draw("GBP 6767 cash", 20195, 500, 0.67, 6767.0, "2026-09-06"),
    Draw("GBP 4444 cash", 20195, 500, 0.44, 4444.0, "2026-09-04"),
    Draw("GBP 2500 cash", 6995, 250, 0.70, 2500.0, "2026-08-28"),
    Draw("GBP 750 cash", 1195, 30, 1.29, 750.0, "2026-08-28"),
]

def analyse(d: Draw):
    full_cost = d.tickets * d.price_gbp
    full_ratio = d.cash_prize_gbp / full_cost
    max_fraction = d.max_per_person / d.tickets
    strict_takeover_possible = d.max_per_person >= d.tickets
    guaranteed_cash_floor = d.cash_prize_gbp if strict_takeover_possible else 0.0
    return {
        **asdict(d),
        "full_buyout_cost_gbp": round(full_cost, 2),
        "impossible_full_buyout_gross_ratio": full_ratio,
        "max_player_fraction": max_fraction,
        "strict_takeover_possible_under_cap": strict_takeover_possible,
        "guaranteed_draw_cash_floor_gbp": guaranteed_cash_floor,
        "uncontrolled_identifiers_at_cap": max(0, d.tickets - d.max_per_person),
    }

def main():
    rows = [analyse(d) for d in DRAWS]
    assert all(not r["strict_takeover_possible_under_cap"] for r in rows)
    assert all(r["guaranteed_draw_cash_floor_gbp"] == 0 for r in rows)
    assert max(r["max_player_fraction"] for r in rows) < 0.04
    out = {
        "packet": "H305",
        "status": "CLOSED / TAKEOVER-BLOCKED",
        "draws": rows,
        "strongest_control_fraction": max(r["max_player_fraction"] for r in rows),
        "best_impossible_full_buyout_ratio": max(r["impossible_full_buyout_gross_ratio"] for r in rows),
        "interpretation": "Per-person caps leave legal external winning identifiers in every checked draw; strict draw-prize cash floor is therefore zero. Free postal entry uses the same per-person maximum and is accepted only if capacity remains when received.",
    }
    p = Path("data/derived/h305_giveaway_guys_cap_screen.json")
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(out, indent=2) + "\n")
    print(json.dumps(out, indent=2))

if __name__ == "__main__":
    main()
