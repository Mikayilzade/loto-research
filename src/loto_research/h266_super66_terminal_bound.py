"""H266 — Australian Super66 terminal/must-be-won exact-cover bound.

The calculation deliberately grants an impossible player-favourable exact purchase of
all 10^6 six-digit identifiers at Lotterywest's $1/game price.  Current official
Lotterywest material says numbers are automatically generated, so the exact cover is
not actually selectable; it is used only as a dominance bound.
"""
from __future__ import annotations
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "data" / "derived" / "h266_super66_terminal_bound.json"

SPACE = 10**6
COST_PER_GAME = 1.0
PRIZES = {2: 6666.0, 3: 666.0, 4: 66.0, 5: 6.60}
CURRENT_JACKPOT_2026_08_22 = 80_000.0
RECENT_JACKPOT_2026_08_08 = 449_669.85


def counts_for_exact_full_space() -> dict[int, int]:
    # Higher-division precedence is applied exactly.
    # D2: first5 OR last5, excluding the exact six-digit D1 identifier.
    d2 = (10 + 10 - 1) - 1
    # D3: first4 OR last4 = 199 identifiers, less D1+D2 = 19.
    d3 = (100 + 100 - 1) - (1 + d2)
    # D4: first3 OR last3 = 1999, less all higher divisions = 199.
    d4 = (1000 + 1000 - 1) - (1 + d2 + d3)
    # D5: first2 OR last2. Intersection fixes four edge digits but leaves two
    # middle digits arbitrary, so intersection size is 100, not 1.
    union_d5_or_better = 10_000 + 10_000 - 100
    d5 = union_d5_or_better - (1 + d2 + d3 + d4)
    return {1: 1, 2: d2, 3: d3, 4: d4, 5: d5}


def main() -> None:
    counts = counts_for_exact_full_space()
    assert counts == {1: 1, 2: 18, 3: 180, 4: 1800, 5: 17901}

    lower_fixed = sum(counts[d] * PRIZES[d] for d in (2, 3, 4, 5))
    cost = SPACE * COST_PER_GAME
    deficit_before_div1 = cost - lower_fixed
    assert abs(lower_fixed - 476_814.60) < 1e-9
    assert abs(deficit_before_div1 - 523_185.40) < 1e-9

    def sole_winner_gross(jackpot: float) -> float:
        return lower_fixed + jackpot

    result = {
        "packet": "H266",
        "game": "Australian Super66 / Lotterywest",
        "space": SPACE,
        "player_favourable_exact_full_cover_cost_aud": cost,
        "exact_division_counts": {str(k): v for k, v in counts.items()},
        "fixed_lower_division_gross_aud": lower_fixed,
        "fixed_lower_return_fraction": lower_fixed / cost,
        "division1_share_needed_for_break_even_aud": deficit_before_div1,
        "strict_profit_requires_div1_share_gt_aud": deficit_before_div1,
        "jackpot_threshold_if_no_external_div1_duplicate_aud": deficit_before_div1,
        "jackpot_threshold_if_one_external_div1_duplicate_aud": 2 * deficit_before_div1,
        "general_threshold_with_E_external_duplicates": "J > 523185.40*(E+1)",
        "current_2026_08_22_jackpot_aud": CURRENT_JACKPOT_2026_08_22,
        "current_sole_winner_full_cover_gross_aud": sole_winner_gross(CURRENT_JACKPOT_2026_08_22),
        "current_sole_winner_return_fraction": sole_winner_gross(CURRENT_JACKPOT_2026_08_22) / cost,
        "recent_2026_08_08_jackpot_aud": RECENT_JACKPOT_2026_08_08,
        "recent_sole_winner_full_cover_gross_aud": sole_winner_gross(RECENT_JACKPOT_2026_08_08),
        "recent_sole_winner_return_fraction": sole_winner_gross(RECENT_JACKPOT_2026_08_08) / cost,
        "structural_gates": {
            "exact_full_cover_forces_own_division1_winner": True,
            "therefore_terminal_no_div1_rolldown_not_compatible_with_full_cover": True,
            "any_nonempty_fixed_portfolio_has_a_legal_draw_equal_to_one_owned_entry": True,
            "therefore_no_nonempty_portfolio_can_force_no_own_division1_in_every_draw": True,
            "official_lotterywest_numbers_automatically_generated": True,
            "player_selectable_exact_identifier_takeover_established": False,
            "hard_pre_draw_external_duplicate_cap_established": False,
        },
        "conclusion": "REJECTED for strict guaranteed-profit terminal/takeover mechanism under checked current rules.",
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
