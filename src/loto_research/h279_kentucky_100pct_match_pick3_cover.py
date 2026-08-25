"""H279: Kentucky Lottery 100% first-deposit match + Pick 3 exact covers.

The current August 2026 promotion matches a first deposit 100% up to $250 in
Bonus funds. Kentucky Pick 3 permits $0.50 Straight and Pair wagers online.
This module computes two uniform exact covers and separates arithmetic success
from execution/eligibility certification.
"""
from __future__ import annotations
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "data" / "derived" / "h279_kentucky_100pct_match_pick3_cover.json"

PROMO_MATCH = 1.0
PROMO_CAP = 250.0


def matched_wallet(deposit: float) -> float:
    return deposit + min(PROMO_CAP, PROMO_MATCH * deposit)


def row(name: str, outcomes: int, wager: float, prize: float):
    cover_cost = outcomes * wager
    # With a 100% match, deposit exactly half the cover cost when within cap.
    required_deposit = cover_cost / 2.0
    assert required_deposit <= PROMO_CAP
    wallet = matched_wallet(required_deposit)
    assert abs(wallet - cover_cost) < 1e-9
    guaranteed_gross = prize
    profit = guaranteed_gross - required_deposit
    return {
        "name": name,
        "outcomes_covered": outcomes,
        "wager_per_selection": wager,
        "cover_cost": cover_cost,
        "required_cash_deposit": required_deposit,
        "bonus": wallet - required_deposit,
        "guaranteed_prize_gross": guaranteed_gross,
        "guaranteed_cash_profit_before_tax_fees": profit,
        "gross_over_cash_deposit": guaranteed_gross / required_deposit,
        "profit_over_cash_deposit": profit / required_deposit,
    }


def main():
    pair = row("Pick 3 Front Pair full 00-99 cover", 100, 0.50, 30.0)
    straight = row("Pick 3 Straight full 000-999 cover", 1000, 0.50, 300.0)
    # Exact arithmetic checks.
    assert pair["guaranteed_cash_profit_before_tax_fees"] == 5.0
    assert straight["guaranteed_cash_profit_before_tax_fees"] == 50.0
    assert pair["profit_over_cash_deposit"] == 0.20
    assert straight["profit_over_cash_deposit"] == 0.20
    d = {
        "packet": "H279",
        "promotion": "Kentucky Lottery August 2026 100% First-Ever Deposit Match",
        "promotion_match": PROMO_MATCH,
        "promotion_cap": PROMO_CAP,
        "arithmetic_state": "STRICT_POSITIVE_IF_FULL_COVER_PURCHASE_EXECUTES",
        "global_state": "NOT_YET_CERTIFIED_SUCCESS",
        "covers": [pair, straight],
        "execution_blockers": [
            "player must satisfy Kentucky iLottery eligibility/location requirements",
            "Pick 3 rules permit undisclosed prize-liability sales cutoffs",
            "iLottery terms reserve the right to refuse attempted purchases",
            "therefore complete same-draw acquisition is not yet a rigorous pre-purchase guarantee",
        ],
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(d, indent=2) + "\n")
    print(json.dumps(d, indent=2))


if __name__ == "__main__":
    main()
