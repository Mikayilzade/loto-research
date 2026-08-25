"""H274: exact current Powerball + Double Play full-cover arithmetic.

Universe: C(69,5)*26.  For a one-copy full cover, prize multiplicities relative
to any fixed draw are invariant, so aggregate fixed-tier gross is exact rather
than simulated.
"""
from math import comb
import json

N = comb(69, 5) * 26
BASE_PRICE = 2
DOUBLE_PLAY_ADDON = 1
TOTAL_PRICE = BASE_PRICE + DOUBLE_PLAY_ADDON
CURRENT_ADVERTISED_JACKPOT = 96_000_000  # Aug 26 2026, deliberately generous annuity face value
CURRENT_CASH_VALUE = 41_200_000

# (white matches, Powerball match) -> prize. Main jackpot deliberately omitted.
MAIN_FIXED = {
    (5, 0): 1_000_000,
    (4, 1): 50_000,
    (4, 0): 100,
    (3, 1): 100,
    (3, 0): 7,
    (2, 1): 7,
    (1, 1): 4,
    (0, 1): 4,
}
DOUBLE_PLAY = {
    (5, 1): 10_000_000,
    (5, 0): 500_000,
    (4, 1): 50_000,
    (4, 0): 500,
    (3, 1): 500,
    (3, 0): 20,
    (2, 1): 20,
    (1, 1): 10,
    (0, 1): 7,
}

def multiplicities():
    out = {}
    for k in range(6):
        white = comb(5, k) * comb(64, 5-k)
        out[(k, 1)] = white
        out[(k, 0)] = white * 25
    assert sum(out.values()) == N
    return out

def solve():
    m = multiplicities()
    main_fixed = sum(m[k] * v for k, v in MAIN_FIXED.items())
    double_play = sum(m[k] * v for k, v in DOUBLE_PLAY.items())
    cost = N * TOTAL_PRICE
    fixed_total = main_fixed + double_play
    result = {
        "packet": "H274",
        "universe_lines": N,
        "line_price_with_double_play": TOTAL_PRICE,
        "full_cover_cost": cost,
        "main_fixed_gross_excluding_jackpot": main_fixed,
        "double_play_gross": double_play,
        "double_play_return_on_addon": double_play / N,
        "combined_fixed_gross": fixed_total,
        "combined_fixed_return_on_total_cost": fixed_total / cost,
        "current_advertised_jackpot": CURRENT_ADVERTISED_JACKPOT,
        "current_cash_value": CURRENT_CASH_VALUE,
        "impossible_favorable_gross_plus_full_annuity_face": fixed_total + CURRENT_ADVERTISED_JACKPOT,
        "impossible_favorable_return_plus_full_annuity_face": (fixed_total + CURRENT_ADVERTISED_JACKPOT) / cost,
        "gross_plus_full_cash_value": fixed_total + CURRENT_CASH_VALUE,
        "return_plus_full_cash_value": (fixed_total + CURRENT_CASH_VALUE) / cost,
        "fixed_deficit_before_jackpot": cost - fixed_total,
    }
    assert result["combined_fixed_return_on_total_cost"] < 1
    assert result["impossible_favorable_return_plus_full_annuity_face"] < 1
    return result

if __name__ == "__main__":
    print(json.dumps(solve(), indent=2, sort_keys=True))
