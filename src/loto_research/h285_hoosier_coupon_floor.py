"""H285: strict cash-floor audit for noncash single-ticket coupons.

This deliberately models only the guarantee question. A free ticket with at
least one legal losing outcome has zero guaranteed withdrawable cash value,
regardless of positive face value or expected value.
"""
from __future__ import annotations
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "data" / "derived" / "h285_hoosier_coupon_floor.json"


def main() -> None:
    result = {
        "packet": "H285",
        "mechanism": "Hoosier Lottery noncash free-ticket coupon",
        "coupon_cash_redeemable": False,
        "single_use": True,
        "per_person_limit": 1,
        "checked_example": {
            "game": "JUMBO BUCKS Fast Play",
            "ticket_price_usd": 1.0,
            "overall_win_odds_denominator": 3.69,
            "legal_nonwinning_outcome_exists": True,
        },
        "guaranteed_withdrawable_cash_usd": 0.0,
        "strict_positive_cash_floor": False,
        "status": "CLOSED_REJECTED_FOR_STRICT_GUARANTEE",
    }
    assert result["coupon_cash_redeemable"] is False
    assert result["checked_example"]["legal_nonwinning_outcome_exists"] is True
    assert result["guaranteed_withdrawable_cash_usd"] == 0.0
    assert result["strict_positive_cash_floor"] is False
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
