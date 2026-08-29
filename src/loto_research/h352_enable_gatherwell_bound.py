"""H352 strict-floor bound for Enable Lottery + Gatherwell Super Draw."""

GAME_SPACE = 1_000_000
TICKET_COST = 1
JACKPOT = 25_000


def strict_cash_upper_bound(n: int) -> int:
    if n <= 0:
        return 0
    # Weekly guaranteed raffle and Super Draw each retain a legal external-winner
    # branch because external eligible tickets/entries already exist.
    # Grant the whole advertised jackpot once a full six-digit cover is possible.
    return JACKPOT if n >= GAME_SPACE else 0


def net_upper_bound(n: int) -> int:
    return strict_cash_upper_bound(n) - TICKET_COST * n


def validate() -> dict:
    points = [1, 267, 999_999, 1_000_000, 1_000_001, 2_000_000]
    rows = [{"n": n, "net_upper_bound_gbp": net_upper_bound(n)} for n in points]
    assert all(r["net_upper_bound_gbp"] < 0 for r in rows)
    # Piecewise proof covers all positive integers, not only sampled points.
    assert JACKPOT - GAME_SPACE < 0
    return {
        "packet": "H352",
        "game_space": GAME_SPACE,
        "ticket_cost_gbp": TICKET_COST,
        "jackpot_gbp": JACKPOT,
        "boundary_rows": rows,
        "arithmetic_inconclusive": 0,
        "closure_relevant_inconclusive": 0,
        "closed": True,
        "success": False,
    }


if __name__ == "__main__":
    import json
    print(json.dumps(validate(), indent=2))
