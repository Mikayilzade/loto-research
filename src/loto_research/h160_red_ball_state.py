"""H160: Michigan Red Ball Double Draw deterministic-state scanner."""

COVER_COST = 1000 * 0.50
ONE_DRAW_GROSS = 250.0


def state_row(white_removed: int) -> dict:
    if not 0 <= white_removed <= 5:
        raise ValueError("white_removed must be in [0,5]")
    balls_remaining = 6 - white_removed
    p_red = 1.0 / balls_remaining
    guaranteed_extra_draw = white_removed == 5
    strict_gross = ONE_DRAW_GROSS * (2 if guaranteed_extra_draw else 1)
    expected_gross = ONE_DRAW_GROSS * (1.0 + p_red)
    return {
        "white_removed": white_removed,
        "balls_remaining": balls_remaining,
        "p_red_next": p_red,
        "guaranteed_extra_draw": guaranteed_extra_draw,
        "strict_gross": strict_gross,
        "strict_cover_ratio": strict_gross / COVER_COST,
        "expected_gross": expected_gross,
        "expected_cover_ratio": expected_gross / COVER_COST,
    }


def all_states():
    return [state_row(k) for k in range(6)]


if __name__ == "__main__":
    for row in all_states():
        print(row)
