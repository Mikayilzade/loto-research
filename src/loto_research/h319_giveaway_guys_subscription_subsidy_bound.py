"""H319: Giveaway Guys 20% subscription-credit subsidy upper bound.

This intentionally grants stronger-than-real assumptions:
- the advertised 20% extra site-credit rate scales without limit;
- every pound of advertised prize-pot/site-credit face value is withdrawable cash;
- one player can acquire the entire finite pool from inception despite sold tickets,
  checkout limits, free-entry competition, or other execution friction.

If the resulting cash-return bound is still < 1, strict guaranteed profit is
impossible for that full-pool/subscription construction.
"""
from __future__ import annotations
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "data" / "derived" / "h319_giveaway_guys_subscription_subsidy_bound.json"

EXTRA_CREDIT = 0.20
LEVERAGE = 1.0 + EXTRA_CREDIT

# Current live pools shown on Giveaway Guys in late Aug 2026.
# `liability_upper` deliberately uses the advertised title/pot at full cash face.
DRAWS = [
    ("Mega Instants", 90_000, 1.00, 30_000.0),
    ("Daily Instants", 1_000, 1.00, 500.0),
    ("Weekly Cash Grab", 2_000, 1.00, 1_000.0),
    ("Simpsons Hit & Run", 25_000, 0.99, 17_500.0),
    ("UNO Wild Card", 6_000, 2.50, 10_000.0),
    ("Cashopoly", 30_000, 1.00, 15_000.0),
    ("Big Brother Cash House", 2_000, 5.00, 5_000.0),
    ("Lucky 7s", 1_000, 0.99, 250.0),
]

# High Roller publishes its individual instant schedule, so use exact face value:
# 1x£500 cash + 2x£100 credit + 5x£50 credit + 10x£20 cash + 20x£10 credit.
HIGH_ROLLER_FACE = 500 + 2*100 + 5*50 + 10*20 + 20*10
DRAWS.append(("High Roller Hit", 500, 4.99, float(HIGH_ROLLER_FACE)))


def row(name: str, n: int, price: float, liability_upper: float) -> dict:
    face_cost = n * price
    impossible_subsidized_cash_cost = face_cost / LEVERAGE
    base_ratio = liability_upper / face_cost
    subsidized_ratio = liability_upper / impossible_subsidized_cash_cost
    return {
        "name": name,
        "tickets": n,
        "ticket_price_gbp": price,
        "face_full_pool_cost_gbp": face_cost,
        "liability_upper_gbp": liability_upper,
        "base_upper_return_ratio": base_ratio,
        "impossible_unlimited_20pct_credit_cash_cost_gbp": impossible_subsidized_cash_cost,
        "subsidized_upper_return_ratio": subsidized_ratio,
        "strict_profit_even_under_favourable_upper_bound": subsidized_ratio > 1.0,
    }


def main() -> None:
    rows = [row(*x) for x in DRAWS]
    best = max(rows, key=lambda r: r["subsidized_upper_return_ratio"])
    assert HIGH_ROLLER_FACE == 1350
    assert all(r["subsidized_upper_return_ratio"] < 1.0 for r in rows)
    assert best["name"] == "Simpsons Hit & Run"
    assert abs(best["subsidized_upper_return_ratio"] - (17_500 / (25_000 * .99) * 1.2)) < 1e-12
    out = {
        "packet": "H319",
        "state": "CLOSED / ARITHMETIC-BOUND",
        "extra_site_credit_rate": EXTRA_CREDIT,
        "impossible_favourable_credit_leverage": LEVERAGE,
        "assumption": "Unlimited scaling of the 20% extra credit and 100% cash valuation of all advertised liabilities.",
        "rows": rows,
        "best": best,
        "conclusion": "Even the strongest deliberately favourable full-pool upper bound remains below break-even.",
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(out, indent=2) + "\n")
    print(json.dumps(out, indent=2))


if __name__ == "__main__":
    main()
