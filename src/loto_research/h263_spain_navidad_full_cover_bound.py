"""H263: exact full-number-space bound for Spain's 2026 Christmas Lottery.

Official SELAE 2026 programme: 205 series, each with 100,000 tickets at EUR200;
70% of issue is allocated to prizes; tickets are divided into EUR20 decimos.
A hypothetical one-decimo copy of every 5-digit number in one series therefore
costs EUR2,000,000 and receives exactly one tenth of that series' EUR14,000,000
prize schedule = EUR1,400,000, independent of the draw outcome.
"""
from __future__ import annotations
import json
from pathlib import Path

NUMBERS = 100_000
DECIMO_PRICE_EUR = 20
SERIES = 205
FULL_TICKET_PRICE_EUR = 200
PRIZE_SHARE = 0.70
PRIZES_PER_SERIES_EUR = 14_000_000


def calculate() -> dict:
    cover_cost = NUMBERS * DECIMO_PRICE_EUR
    gross = PRIZES_PER_SERIES_EUR / 10
    assert gross == cover_cost * PRIZE_SHARE
    return {
        "packet": "H263",
        "game": "Spain Loteria Nacional Sorteo Extraordinario de Navidad 2026",
        "mechanism": "fixed per-number prize schedule; hypothetical one-decimo complete number-space cover within one series",
        "numbers": NUMBERS,
        "series": SERIES,
        "decimo_price_eur": DECIMO_PRICE_EUR,
        "full_ticket_price_eur": FULL_TICKET_PRICE_EUR,
        "prizes_per_series_eur": PRIZES_PER_SERIES_EUR,
        "cover_cost_eur": cover_cost,
        "guaranteed_gross_eur": gross,
        "guaranteed_net_eur": gross - cover_cost,
        "gross_return_ratio": gross / cover_cost,
        "gross_return_pct": 100 * gross / cover_cost,
        "break_even_subsidy_eur": cover_cost - gross,
        "required_discount_on_stake_pct": 100 * (1 - gross / cover_cost),
        "strict_profit_without_external_subsidy": gross > cover_cost,
        "interpretation": "Complete number-space ownership removes draw risk but inherits the official 70% payout ratio; no strict positive gross is possible from the base prize schedule.",
    }


def main() -> None:
    d = calculate()
    out = Path(__file__).resolve().parents[2] / "data" / "derived" / "h263_spain_navidad_full_cover_bound.json"
    out.write_text(json.dumps(d, indent=2) + "\n")
    print(json.dumps(d, indent=2))


if __name__ == "__main__":
    main()
