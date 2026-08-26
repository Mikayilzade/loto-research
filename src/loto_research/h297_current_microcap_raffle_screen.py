"""H297: exact full-acquisition screen for current hard-capped raffles.

All models deliberately grant impossible-perfect ownership of every issued ticket.
If total player-facing liabilities still remain below full acquisition cost, the
candidate is closed for strict guaranteed-profit takeover before execution friction.
"""
from __future__ import annotations

CANDIDATES = [
    {
        "name": "Holy Cross Charities 31 Days of Cash 2026",
        "ticket_cap": 500,
        "unit_cost": 50.0,
        "liability": 10400.0,
        "currency": "USD",
        "source": "https://holycrosscharities.org/",
        "note": "54x$100 + 2x$250 + 2x$500 + 2x$750 + 2x$1,000; every ticket remains eligible for all 31 days.",
    },
    {
        "name": "NvACD Sportsman's Raffle 2026",
        "ticket_cap": 500,
        "unit_cost": 100.0,
        "liability": 15000.0,
        "currency": "USD",
        "source": "https://www.nvacd.org/?page_id=8287",
        "note": "30 daily wins; each prize may be exchanged for a $500 CAL Ranch gift certificate; winning tickets return to the draw.",
    },
    {
        "name": "UFTGFNC Footy Finals Lotto 2026",
        "ticket_cap": 400,
        "unit_cost": 50.0,
        "liability": 2500.0,
        "currency": "AUD",
        "source": "https://www.trybooking.com/events/landing/1638389",
        "note": "Three published cash prizes: $1,500 + $750 + $250.",
    },
    {
        "name": "Sister Cities of Nashville Mendoza Raffle 2026",
        "ticket_cap": 500,
        "unit_cost": 100.0,
        "liability": 5000.0,
        "currency": "USD",
        "source": "https://www.scnashville.org/",
        "note": "Published prize value: $5,000 trip for two.",
    },
]


def evaluate(row: dict) -> dict:
    cost = row["ticket_cap"] * row["unit_cost"]
    gross = row["liability"]
    ratio = gross / cost
    assert cost > 0 and gross >= 0
    assert ratio < 1.0
    return {
        **row,
        "full_acquisition_cost": cost,
        "perfect_takeover_gross": gross,
        "gross_ratio": ratio,
        "deficit": cost - gross,
        "strict_profit_possible_under_perfect_takeover": gross > cost,
    }


def main() -> None:
    rows = [evaluate(x) for x in CANDIDATES]
    assert len(rows) == 4
    assert all(not r["strict_profit_possible_under_perfect_takeover"] for r in rows)
    best = max(rows, key=lambda r: r["gross_ratio"])
    assert best["name"].startswith("Holy Cross")
    assert abs(best["gross_ratio"] - 0.416) < 1e-12
    for r in rows:
        print(r["name"], f"{100*r['gross_ratio']:.6f}%", "deficit", r["deficit"], r["currency"])


if __name__ == "__main__":
    main()
