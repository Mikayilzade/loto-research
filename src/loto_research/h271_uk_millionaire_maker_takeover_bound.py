"""H271: UK EuroMillions Millionaire Maker takeover arithmetic.

This packet does not assume control of raffle-code assignment. It computes the
simple acquisition thresholds and records the structural counterexample: if any
valid generated raffle code is owned by an external player, that external code
is itself a legal winning draw and the portfolio's guaranteed Millionaire Maker
payout is zero.
"""
from math import comb
import json

LINE_COST_GBP = 2.50
MM_PRIZE_GBP = 1_000_000
MAIN_OUTCOMES = comb(50, 5) * comb(12, 2)


def main():
    raffle_only_break_even_lines = MM_PRIZE_GBP / LINE_COST_GBP
    strict_profit_max_lines = int(raffle_only_break_even_lines) - 1
    main_cover_cost = MAIN_OUTCOMES * LINE_COST_GBP
    out = {
        "packet": "H271",
        "game": "UK EuroMillions Millionaire Maker",
        "line_cost_gbp": LINE_COST_GBP,
        "millionaire_maker_prize_gbp": MM_PRIZE_GBP,
        "raffle_only_break_even_lines": raffle_only_break_even_lines,
        "raffle_only_strict_profit_max_lines": strict_profit_max_lines,
        "main_matrix_lines": MAIN_OUTCOMES,
        "main_matrix_cover_cost_gbp": main_cover_cost,
        "one_mm_prize_vs_main_cover_return": MM_PRIZE_GBP / main_cover_cost,
        "structural_guarantee_condition": "portfolio must own every valid generated raffle code in the draw",
        "external_code_counterexample": "if one externally owned generated code exists, selecting it is a legal raffle outcome and portfolio MM gross is 0",
        "player_selectable_codes": False,
        "takeover_certified_executable": False,
        "status": "CLOSED / REJECTED for strict guaranteed-profit takeover under checked rules",
    }
    print(json.dumps(out, indent=2))


if __name__ == "__main__":
    main()
