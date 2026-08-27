"""H306: current On The Podium zero-price finite-pool takeover blocker.

This model is intentionally simple.  A strict takeover of a finite draw requires
ownership/control of every eligible identifier before the draw.  If any eligible
identifier is already controlled by another entrant, a legal outcome remains in
which that external identifier wins, so the entrant's guaranteed cash floor from
that draw is zero.
"""
from dataclasses import dataclass, asdict
import json

@dataclass(frozen=True)
class Draw:
    name: str
    pool: int
    sold_pct: float
    prize_cash_gbp: float | None
    prize_kind: str

DRAWS = [
    Draw("FREE TO ENTER £100 CASH", 1000, 16.2, 100.0, "cash"),
    Draw("2 BSB tickets - free", 1000, 5.6, None, "noncash"),
    Draw("FREE TO ENTER £25 SITE CREDIT", 1000, 6.1, None, "site_credit"),
    Draw("FREE TO ENTER £50 SITE CREDIT", 1000, 6.5, None, "site_credit"),
    Draw("FREE TO ENTER £75 SITE CREDIT", 1000, 6.2, None, "site_credit"),
]

def evaluate(d: Draw):
    assert d.pool > 0
    assert d.sold_pct > 0.0
    # A displayed positive sold percentage proves at least one identifier has
    # already been issued to the market.  The exact rounded count is unnecessary
    # for the impossibility argument.
    external_identifier_exists = True
    strict_current_takeover_possible = not external_identifier_exists
    guaranteed_draw_cash_floor = 0.0 if external_identifier_exists else d.prize_cash_gbp
    return {
        **asdict(d),
        "external_identifier_exists": external_identifier_exists,
        "strict_current_takeover_possible": strict_current_takeover_possible,
        "guaranteed_draw_cash_floor_gbp": guaranteed_draw_cash_floor,
    }

if __name__ == "__main__":
    rows = [evaluate(d) for d in DRAWS]
    assert all(not r["strict_current_takeover_possible"] for r in rows)
    assert rows[0]["guaranteed_draw_cash_floor_gbp"] == 0.0
    print(json.dumps({"packet": "H306", "rows": rows}, indent=2))
