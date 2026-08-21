"""H154: exact complete-cover arithmetic for KenoGO 1-Spot states."""

PRICE_JACKPOT = 2.0
PRICE_CLASSIC = 1.0
N_NUMBERS = 80
N_DRAWN = 20

jackpot_prizes = {
    "regular": 3.0,
    "minor": 10.0,
    "major": 25.0,
}


def cover_row(game: str, price: float, prize: float):
    cost = N_NUMBERS * price
    gross = N_DRAWN * prize
    return {
        "game": game,
        "ticket_price": price,
        "one_spot_prize": prize,
        "cover_cost": cost,
        "guaranteed_gross_conditional_on_state": gross,
        "gross_ratio": gross / cost,
        "surplus": gross - cost,
    }


if __name__ == "__main__":
    rows = [cover_row("classic", PRICE_CLASSIC, 3.0)]
    rows += [cover_row(f"jackpot_{k}", PRICE_JACKPOT, v) for k, v in jackpot_prizes.items()]
    for row in rows:
        print(row)

    # Full Jackpot cover must survive every permitted jackpot level.
    strict_floor = min(r["gross_ratio"] for r in rows if r["game"].startswith("jackpot_"))
    assert abs(strict_floor - 0.375) < 1e-12
    assert abs(cover_row("jackpot_minor", 2.0, 10.0)["gross_ratio"] - 1.25) < 1e-12
    assert abs(cover_row("jackpot_major", 2.0, 25.0)["gross_ratio"] - 3.125) < 1e-12
    assert abs(cover_row("classic", 1.0, 3.0)["gross_ratio"] - 0.75) < 1e-12
