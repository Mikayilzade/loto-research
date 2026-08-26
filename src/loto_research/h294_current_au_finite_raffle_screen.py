"""H294 — current Australian finite-raffle full-takeover screen.

The test is deliberately player-favourable: assume one player can acquire every
issued identifier and receives every still-relevant advertised prize. If even
that impossible-perfect takeover is below acquisition cost, the strict-profit
mechanism is closed without needing execution assumptions.
"""
from __future__ import annotations
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "data" / "derived" / "h294_current_au_finite_raffle_screen.json"

POOLS = [
    {
        "name": "yourtown Luxury Prize Home Draw 559",
        "max_tickets": 470_000,
        "ticket_price_aud": 15.0,
        # Intentionally generous: main prize plus all still/future advertised
        # member/bonus liabilities visible on 2026-08-26. This ignores
        # eligibility exclusions and therefore favours the takeover hypothesis.
        "prizes_aud": [2_940_000, 15_000, 5_000, 10_000, 50_000],
        "source": "https://www.yourtownprizehomes.com.au/win-a-home/prize-draw-noosa",
    },
    {
        "name": "yourtown Prestige Car Draw 1158",
        "max_tickets": 130_000,
        "ticket_price_aud": 10.0,
        "prizes_aud": [260_000, 5_000, 2_000, 2_000, 2_000],
        "source": "https://www.yourtownprizehomes.com.au/win-a-car/audi/",
    },
    {
        "name": "RSPCA Lottery Draw 92",
        "max_tickets": 160_000,
        "ticket_price_aud": 10.0,
        "prizes_aud": [320_000, 3_000],
        "source": "https://www.rspcalottery.com.au/rspca-lottery/terms-and-conditions",
    },
    {
        "name": "MS QLD Cash Grab Draw 2",
        "max_tickets": 10_000,
        "ticket_price_aud": 5.0,
        "prizes_aud": [10_000],
        "source": "https://www.msqlotteries.com.au/cash-grab",
    },
]


def evaluate(pool: dict) -> dict:
    cost = pool["max_tickets"] * pool["ticket_price_aud"]
    liabilities = sum(pool["prizes_aud"])
    ratio = liabilities / cost
    return {
        **pool,
        "full_takeover_cost_aud": cost,
        "player_favourable_total_liabilities_aud": liabilities,
        "full_takeover_return_ratio": ratio,
        "full_takeover_return_pct": 100 * ratio,
        "deficit_aud": cost - liabilities,
        "strict_profit_under_perfect_takeover": liabilities > cost,
    }


def main() -> None:
    rows = [evaluate(p) for p in POOLS]
    assert all(r["max_tickets"] > 0 and r["ticket_price_aud"] > 0 for r in rows)
    assert all(r["player_favourable_total_liabilities_aud"] >= 0 for r in rows)
    assert all(not r["strict_profit_under_perfect_takeover"] for r in rows)
    best = max(rows, key=lambda r: r["full_takeover_return_ratio"])
    assert best["name"] == "yourtown Luxury Prize Home Draw 559"
    assert abs(best["full_takeover_return_pct"] - 42.836879432624114) < 1e-12
    packet = {
        "packet": "H294",
        "as_of": "2026-08-26",
        "method": "impossible-perfect full ownership plus generous advertised-liability upper bound",
        "pool_count": len(rows),
        "all_closed_by_arithmetic": True,
        "best_case": best["name"],
        "best_return_pct": best["full_takeover_return_pct"],
        "rows": rows,
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(packet, indent=2) + "\n")
    print(json.dumps(packet, indent=2))


if __name__ == "__main__":
    main()
