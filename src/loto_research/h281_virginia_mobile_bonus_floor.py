"""H281: Virginia promotional-value floor screen.

Checks two deterministic facts relevant to guaranteed-profit research:
1) a complete Virginia Pick 3 Pair cover has exactly 50% fixed gross return;
2) the current first-mobile-cashing offer grants ten free Jackpot Spectacular
   games, but a free random game has no positive guaranteed cash floor because
   non-winning outcomes exist.

This packet is intentionally a worst-case guarantee test, not an EV estimate.
"""

from __future__ import annotations
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "data" / "derived" / "h281_virginia_mobile_bonus_floor.json"


def pair_cover(stake: float) -> dict:
    selections = 100
    cost = selections * stake
    guaranteed_prize = 50.0 * stake  # official $1 Pair prize; 50c pays half
    return {
        "stake_per_pair": stake,
        "selections": selections,
        "cover_cost": cost,
        "guaranteed_prize": guaranteed_prize,
        "gross_return_ratio": guaranteed_prize / cost,
        "bonus_credit_required_for_break_even": cost - guaranteed_prize,
        "bonus_credit_required_for_strict_profit": f"> {cost - guaranteed_prize:.2f}",
    }


def main() -> None:
    rows = [pair_cover(0.50), pair_cover(1.00)]
    assert rows[0]["cover_cost"] == 50.0
    assert rows[0]["guaranteed_prize"] == 25.0
    assert rows[1]["cover_cost"] == 100.0
    assert rows[1]["guaranteed_prize"] == 50.0
    assert all(abs(r["gross_return_ratio"] - 0.5) < 1e-12 for r in rows)

    out = {
        "packet": "H281",
        "game": "Virginia Pick 3 Pair + current first-mobile-cashing bonus",
        "pair_cover": rows,
        "current_mobile_cashing_bonus_games": 10,
        "bonus_game": "Jackpot Spectacular",
        "bonus_game_published_odds_any_prize": "1 in 3.99",
        "bonus_game_positive_guaranteed_cash_floor": 0.0,
        "reason": (
            "Jackpot Spectacular has non-winning outcomes; ten uncontrolled free random games "
            "therefore do not create a strictly positive worst-case cash floor."
        ),
        "verdict": "CLOSED for strict guaranteed-profit use of the checked Virginia bonus mechanics",
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(out, indent=2) + "\n")
    print(json.dumps(out, indent=2))


if __name__ == "__main__":
    main()
