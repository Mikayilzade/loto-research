"""H259: deterministic full-pack screen for finite pull-tab boxes.

A sealed pull-tab box with a fixed prize schedule is one of the rare lottery
products where purchasing the complete finite population removes draw/RNG and
sharing risk. This module computes the deterministic gross return and the
minimum universal free prize uplift required to reach break-even.
"""
from __future__ import annotations
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "data" / "derived" / "h259_fixed_pulltab_pack_screen.json"


def evaluate(ticket_count: int, ticket_price: float, prizes: list[tuple[float, int]]) -> dict:
    cost = ticket_count * ticket_price
    payout = sum(value * count for value, count in prizes)
    gross_return = payout / cost
    break_even_uplift = cost / payout - 1.0
    return {
        "ticket_count": ticket_count,
        "ticket_price": ticket_price,
        "full_pack_cost": cost,
        "full_pack_fixed_prize_total": payout,
        "gross_return": gross_return,
        "guaranteed_loss": cost - payout,
        "minimum_universal_free_prize_uplift_for_break_even": break_even_uplift,
    }


def main() -> None:
    result = {
        "packet": "H259",
        "game": "Wisconsin Lottery GONE FISHIN' Pull-Tab #2752",
        "official_effective_date": "2026-01-05",
        "source": "https://wilottery.com/games/instant-games/gone-fishin-features-procedures",
        "prizes": [
            {"value": 0.50, "count": 200},
            {"value": 1.00, "count": 25},
            {"value": 5.00, "count": 10},
            {"value": 15.00, "count": 2},
            {"value": 25.00, "count": 2},
            {"value": 75.00, "count": 1},
        ],
    }
    result.update(evaluate(1050, 0.50, [(0.5,200),(1,25),(5,10),(15,2),(25,2),(75,1)]))
    result["strict_guarantee"] = False
    result["status"] = "REJECTED current ordinary full-pack buyout"
    result["reopen_condition"] = "A deterministic player-eligible discount/subsidy or universal prize uplift exceeding 59.0909% after all costs, or another fixed pack whose guaranteed prize total exceeds acquisition cost."
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
