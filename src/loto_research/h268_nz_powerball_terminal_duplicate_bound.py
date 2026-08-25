"""H268: NZ Powerball terminal/must-be-won full-cover duplicate stress bound.

This is not a strategy generator.  It tests whether complete outcome coverage can
turn a must-be-won/rolldown jackpot into a strict guaranteed-profit portfolio.
The adversarial legal market state used below is deliberately simple: external
players buy m copies of the actual Division-1 line.  Those copies dilute our
Division-1 shares while their turnover still feeds the lower prize pools.

Two matrices are evaluated:
* current rules before 2026-09-13: 10 Powerballs, Powerball pool >=60%, reserve
  set-aside up to 10%, fixed PB Division 7 = NZ$15;
* enacted 2026-09-13 rules: 14 Powerballs, Powerball pool >=55%, same 10%
  reserve set-aside, fixed PB D7 = NZ$20 and D8 = NZ$12.

Standard Lotto is unchanged in the relevant respects: 6/40, NZ$0.70 per
selection, prize pool >=60%, reserve set-aside up to 5%, fixed D7 monetary
equivalent NZ$2.80 (paid as four bonus selections).  For a strict cash floor we
value those future bonus selections at zero while still deducting their
rules-defined value before allocating the pari-mutuel pool.
"""
from __future__ import annotations

import json
from math import comb
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "data" / "derived" / "h268_nz_powerball_terminal_duplicate_bound.json"

MAIN = comb(40, 6)
STD_PRICE = 0.70
PB_PRICE = 0.80
LINE_PRICE = STD_PRICE + PB_PRICE
STD_AVAILABLE_FRACTION = 0.60 - 0.05
STD_D1_SHARE = 0.3252
STD_D7_VALUE = 2.80
NONBONUS_OTHERS = 33  # 40 minus six winning numbers minus bonus
STD_D7_MAIN_COUNT = comb(6, 3) * comb(NONBONUS_OTHERS, 3)


def case(*, powerballs: int, jackpot: float, pb_pool_min: float,
         pb_reserve_max: float, pb_d1_share: float, pb_d7: float,
         pb_d8: float = 0.0, scan_limit: int = 200_000) -> dict:
    n = MAIN * powerballs
    cost = n * LINE_PRICE

    std_fixed_count = STD_D7_MAIN_COUNT * powerballs
    std_fixed_value = std_fixed_count * STD_D7_VALUE

    pb_d7_count = STD_D7_MAIN_COUNT
    pb_d7_value = pb_d7_count * pb_d7
    pb_d8_count = comb(6, 2) * comb(NONBONUS_OTHERS, 3) if pb_d8 else 0
    pb_d8_value = pb_d8_count * pb_d8
    pb_fixed_value = pb_d7_value + pb_d8_value
    pb_available_fraction = pb_pool_min - pb_reserve_max

    def gross(m: int) -> float:
        # m external entries are exact copies of the realised D1 main+PB line.
        # Our complete cover owns `powerballs` Standard-Lotto D1 entries (one
        # for each PB attached to the winning six) but only one Powerball D1.
        std_pari = STD_AVAILABLE_FRACTION * STD_PRICE * (n + m) - std_fixed_value
        pb_pari = pb_available_fraction * PB_PRICE * (n + m) - pb_fixed_value

        std_non_d1 = (1.0 - STD_D1_SHARE) * std_pari
        std_d1_ours = (powerballs / (powerballs + m)) * STD_D1_SHARE * std_pari
        pb_non_d1 = (1.0 - pb_d1_share) * pb_pari
        pb_d1_ours = (1.0 / (1 + m)) * (pb_d1_share * pb_pari + jackpot)

        # PB fixed prizes are immediate cash. Standard D7 is deliberately not
        # added: it is paid as future bonus selections and has zero strict cash
        # floor because all those future selections can legally lose.
        return std_non_d1 + std_d1_ours + pb_non_d1 + pb_d1_ours + pb_fixed_value

    best_m = 0
    best_gross = gross(0)
    for m in range(1, scan_limit + 1):
        g = gross(m)
        if g < best_gross:
            best_m, best_gross = m, g

    return {
        "powerballs": powerballs,
        "main_combinations": MAIN,
        "paired_outcome_lines": n,
        "line_price_nzd": LINE_PRICE,
        "full_cover_cost_nzd": cost,
        "jackpot_stress_nzd": jackpot,
        "standard_d7_count": std_fixed_count,
        "standard_d7_rules_value_nzd": std_fixed_value,
        "standard_d7_cash_floor_used_nzd": 0.0,
        "powerball_d7_count": pb_d7_count,
        "powerball_d7_cash_nzd": pb_d7_value,
        "powerball_d8_count": pb_d8_count,
        "powerball_d8_cash_nzd": pb_d8_value,
        "adversarial_duplicate_scan_limit": scan_limit,
        "worst_duplicate_count_in_scan": best_m,
        "gross_at_worst_duplicate_count_nzd": best_gross,
        "profit_at_worst_duplicate_count_nzd": best_gross - cost,
        "gross_ratio_at_worst_duplicate_count": best_gross / cost,
        "gross_with_zero_external_duplicates_nzd": gross(0),
        "structural_rolldown_gate": (
            "Any nonempty portfolio contains a legal realised D1 line, so the "
            "portfolio cannot force the no-D1 rolldown branch in every draw state."
        ),
    }


def main() -> None:
    result = {
        "packet": "H268",
        "topic": "New Zealand Powerball terminal/must-be-won full-cover duplicate bound",
        "status": "REJECTED_FOR_STRICT_GUARANTEE",
        "current_pre_2026_09_13": case(
            powerballs=10,
            jackpot=50_000_000,
            pb_pool_min=0.60,
            pb_reserve_max=0.10,
            pb_d1_share=0.9472,
            pb_d7=15.0,
        ),
        "current_sensitivity_60m": case(
            powerballs=10,
            jackpot=60_000_000,
            pb_pool_min=0.60,
            pb_reserve_max=0.10,
            pb_d1_share=0.9472,
            pb_d7=15.0,
        ),
        "enacted_from_2026_09_13": case(
            powerballs=14,
            jackpot=60_000_000,
            pb_pool_min=0.55,
            pb_reserve_max=0.10,
            pb_d1_share=0.9462,
            pb_d7=20.0,
            pb_d8=12.0,
        ),
        "interpretation": (
            "Complete outcome coverage does not provide a strict guaranteed-profit "
            "takeover. It necessarily creates a D1 winner, preventing forced rolldown, "
            "and a legal finite block of external duplicates of the realised D1 line "
            "drives the portfolio far below acquisition cost even at NZ$50m/NZ$60m "
            "jackpot stress levels."
        ),
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
