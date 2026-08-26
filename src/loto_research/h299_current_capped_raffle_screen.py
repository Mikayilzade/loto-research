"""H299: exact full-acquisition screen for current/upcoming hard-capped raffles.

This model deliberately gives the player impossible-perfect ownership of every issued
identifier.  If even that strongest takeover remains below acquisition cost, the
raffle cannot provide a strict guaranteed-profit construction through full takeover.
"""
from __future__ import annotations
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "data" / "derived" / "h299_current_capped_raffle_screen.json"

CASES = [
    {
        "name": "NAVMC Crocktoberfest Golden Ticket",
        "draw_date": "2026-10-18",
        "ticket_count": 100,
        "ticket_cost": 100.0,
        "guaranteed_liability": 1000.0,
        "source": "https://navmc.org/",
        "note": "100 tickets at $100; one $1,000 cash prize.",
    },
    {
        "name": "Golden Lake Improvement Association Sept 6 cash raffle",
        "draw_date": "2026-09-06",
        "ticket_count": 200,
        "ticket_cost": 100.0,
        "guaranteed_liability": 10000.0,
        "source": "https://goldenlakeassociation.com/drawings/",
        "note": "$7,000 + $2,000 + $1,000 cash prizes; 200 tickets at $100.",
    },
    {
        "name": "DPCA Top 20 Conformation 50/50 raffle",
        "draw_date": "2026-10-05",
        "ticket_count": 100,
        "ticket_cost": 100.0,
        "guaranteed_liability": 5000.0,
        "source": "https://dpca.org/cardio-clinic-wae-fundraisers-wine-tasting-rules/",
        "note": "100 tickets at $100; winner receives half the full pot, up to $5,000.",
    },
    {
        "name": "Millville Army Air Field Museum Dec 2 50/50 cash raffle",
        "draw_date": "2026-12-02",
        "ticket_count": 500,
        "ticket_cost": 50.0,
        "guaranteed_liability": 12500.0,
        "source": "https://p47millville.org/events/",
        "note": "Player-favourable upper reading: $10,000 first prize plus five $500 prizes.",
    },
]


def evaluate(case):
    cost = case["ticket_count"] * case["ticket_cost"]
    gross = case["guaranteed_liability"]
    ratio = gross / cost
    return {
        **case,
        "full_acquisition_cost": cost,
        "full_takeover_gross": gross,
        "gross_ratio": ratio,
        "deficit": cost - gross,
        "strict_profit_under_perfect_takeover": gross > cost,
    }


def main():
    rows = [evaluate(c) for c in CASES]
    assert all(r["ticket_count"] > 0 and r["ticket_cost"] > 0 for r in rows)
    assert all(r["full_acquisition_cost"] > 0 for r in rows)
    assert all(not r["strict_profit_under_perfect_takeover"] for r in rows)
    best = max(rows, key=lambda r: r["gross_ratio"])
    assert best["gross_ratio"] == 0.5
    packet = {
        "packet": "H299",
        "terminal_state": "CLOSED_FOR_FULL_TAKEOVER",
        "case_count": len(rows),
        "best_case": best["name"],
        "best_gross_ratio": best["gross_ratio"],
        "best_required_external_uplift_fraction_of_cost": 1.0 - best["gross_ratio"],
        "cases": rows,
        "interpretation": (
            "Even impossible-perfect ownership of every issued identifier remains at or below "
            "50% gross in the strongest screened case. Execution friction can only worsen this."
        ),
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(packet, indent=2) + "\n")
    print(json.dumps(packet, indent=2))


if __name__ == "__main__":
    main()
