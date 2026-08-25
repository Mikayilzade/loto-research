"""H272: exact full-issuance bound for Japan 2026 Takarakuji Day commemorative lottery.

Official schedule: draw 1118, 20,000,000 tickets, JPY 200 each, total face value
JPY 4,000,000,000.  This script sums the complete published prize schedule and
computes the impossible-favourable full-buyout gross return.
"""
from __future__ import annotations
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "data" / "derived" / "h272_japan_takarakuji_day_full_issue_bound.json"

TICKET_PRICE = 200
UNITS = 2
TICKETS_PER_UNIT = 10_000_000
PRIZES = {
    "first": (150_000_000, 2),
    "first_adjacent": (25_000_000, 4),
    "first_different_group": (100_000, 198),
    "second": (500_000, 400),
    "third": (50_000, 2_000),
    "fourth": (10_000, 20_000),
    "fifth": (2_000, 200_000),
    "sixth": (200, 2_000_000),
    "special": (30_000, 6_000),
}

def calculate():
    tickets = UNITS * TICKETS_PER_UNIT
    cost = tickets * TICKET_PRICE
    prize_components = {k: value * count for k, (value, count) in PRIZES.items()}
    gross = sum(prize_components.values())
    assert tickets == 20_000_000
    assert cost == 4_000_000_000
    assert gross == 1_899_800_000
    return {
        "packet": "H272",
        "game": "Japan Takarakuji Day commemorative lottery, draw 1118",
        "ticket_price_jpy": TICKET_PRICE,
        "units": UNITS,
        "tickets_per_unit": TICKETS_PER_UNIT,
        "full_issue_tickets": tickets,
        "full_issue_cost_jpy": cost,
        "published_prize_components_jpy": prize_components,
        "published_prize_total_jpy": gross,
        "full_issue_return_ratio": gross / cost,
        "full_issue_return_percent": 100 * gross / cost,
        "full_issue_deficit_jpy": cost - gross,
        "strict_guaranteed_profit_possible_under_perfect_full_ownership": gross > cost,
        "interpretation": "Even impossible-perfect ownership of every issued ticket returns only the complete published prize pool, which is below acquisition cost. Real execution constraints can only weaken this bound.",
    }

def main():
    result = calculate()
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(result, indent=2, ensure_ascii=False) + "\n")
    print(json.dumps(result, indent=2, ensure_ascii=False))

if __name__ == "__main__":
    main()
