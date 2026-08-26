"""H291: exact subsidy threshold for Michigan Daily 3 full Straight cover.

The calculation is deliberately minimal and auditable.  A complete Straight cover
contains all 1,000 three-digit outcomes.  At the $0.50 wager level it costs $500
and exactly one line returns $250 for every draw, so the deterministic base-game
gross floor is 50%.

If a deposit-match bonus of fraction m is fully spendable on the cover, external
cash needed for a $500 cover is 500/(1+m).  Strict positive cash profit therefore
requires 250 > 500/(1+m), i.e. m > 1 (strictly more than a 100% match).
"""
from fractions import Fraction
import json

LINES = 1000
STAKE = Fraction(1, 2)
WIN = Fraction(250, 1)
COVER_COST = LINES * STAKE


def metrics(match: Fraction):
    cash_required = COVER_COST / (1 + match)
    return {
        "match_fraction": float(match),
        "cash_required": float(cash_required),
        "guaranteed_gross": float(WIN),
        "cash_profit_floor": float(WIN - cash_required),
        "cash_recovery_ratio": float(WIN / cash_required),
    }


def main():
    assert COVER_COST == 500
    assert WIN == 250
    assert WIN / COVER_COST == Fraction(1, 2)
    assert metrics(Fraction(1, 1))["cash_profit_floor"] == 0.0
    assert metrics(Fraction(101, 100))["cash_profit_floor"] > 0
    out = {
        "packet": "H291",
        "game": "Michigan Daily 3",
        "construction": "all 1000 Straight outcomes at $0.50",
        "cover_lines": LINES,
        "cover_cost": float(COVER_COST),
        "guaranteed_gross": float(WIN),
        "base_floor_ratio": float(WIN / COVER_COST),
        "strict_match_threshold": ">100%",
        "examples": {
            "10_percent": metrics(Fraction(1, 10)),
            "40_percent": metrics(Fraction(2, 5)),
            "100_percent": metrics(Fraction(1, 1)),
            "101_percent": metrics(Fraction(101, 100)),
        },
    }
    print(json.dumps(out, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
