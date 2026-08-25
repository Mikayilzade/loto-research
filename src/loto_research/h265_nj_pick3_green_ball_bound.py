"""H265: New Jersey Pick-3 Green Ball terminal-double-draw upper bound.

The Green Ball promotion can create a deterministic free second Pick-3 draw after
six consecutive white-ball removals leave only the Green Ball.  This module
checks the strongest version of that opportunity: assume the player can buy any
nonnegative portfolio of the published fixed-prize Pick-3 wager primitives on a
known terminal evening.

For each primitive wager, the average gross over one uniformly distributed
Pick-3 draw is computed from the official number of winning outcomes and fixed
prize.  In the terminal Green Ball state the base wager receives two Pick-3
draws for one base stake.  FIREBALL, when purchased, applies to the regular draw
but not to Green Ball winner determination, while doubling the wager cost.

Because min(outcome gross) <= average(outcome gross), if every primitive has
terminal average gross <= cost, no nonnegative mixture of those primitives can
have an everywhere-strictly-profitable payoff.  Straight/Box and Wheel are
nonnegative sums of the listed primitives/straight plays and inherit the same
bound.
"""
from __future__ import annotations

import json
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "data" / "derived" / "h265_nj_pick3_green_ball_bound.json"

# All figures are for a $0.50 base wager from the current NJ Lottery Pick-3
# published prize table.  outcome_denominator is 1000 for 3-digit bets and 100
# for pair bets.  FIREBALL winning-combination counts/prizes are the published
# add-on values; the add-on costs another $0.50.
WAGERS = {
    "straight": {
        "base_win_outcomes": 1,
        "base_outcome_denominator": 1000,
        "base_prize_cents": 25_000,
        "fireball_win_outcomes": 3,
        "fireball_outcome_denominator": 1000,
        "fireball_prize_cents": 9_000,
    },
    "3_way_box": {
        "base_win_outcomes": 3,
        "base_outcome_denominator": 1000,
        "base_prize_cents": 8_000,
        "fireball_win_outcomes": 9,
        "fireball_outcome_denominator": 1000,
        "fireball_prize_cents": 3_000,
    },
    "6_way_box": {
        "base_win_outcomes": 6,
        "base_outcome_denominator": 1000,
        "base_prize_cents": 4_000,
        "fireball_win_outcomes": 18,
        "fireball_outcome_denominator": 1000,
        "fireball_prize_cents": 1_500,
    },
    "pair": {
        "base_win_outcomes": 1,
        "base_outcome_denominator": 100,
        "base_prize_cents": 2_500,
        "fireball_win_outcomes": 3,
        "fireball_outcome_denominator": 100,
        "fireball_prize_cents": 900,
    },
}

BASE_COST = Fraction(50, 100)  # $0.50
FIREBALL_ADDON_COST = Fraction(50, 100)  # doubles the base cost


def dollars(cents: int) -> Fraction:
    return Fraction(cents, 100)


def expected(win_outcomes: int, denominator: int, prize_cents: int) -> Fraction:
    return Fraction(win_outcomes, denominator) * dollars(prize_cents)


def main() -> None:
    rows = []
    for name, w in WAGERS.items():
        base_ev = expected(
            w["base_win_outcomes"],
            w["base_outcome_denominator"],
            w["base_prize_cents"],
        )
        fb_ev = expected(
            w["fireball_win_outcomes"],
            w["fireball_outcome_denominator"],
            w["fireball_prize_cents"],
        )

        # Known terminal Green Ball evening: free second draw applies to base.
        terminal_base_gross_avg = 2 * base_ev
        terminal_base_ratio = terminal_base_gross_avg / BASE_COST

        # FIREBALL doubles total cost; Green Ball bonus excludes FIREBALL.
        terminal_fb_gross_avg = 2 * base_ev + fb_ev
        terminal_fb_cost = BASE_COST + FIREBALL_ADDON_COST
        terminal_fb_ratio = terminal_fb_gross_avg / terminal_fb_cost

        rows.append(
            {
                "wager": name,
                "base_one_draw_expected_dollars": float(base_ev),
                "fireball_regular_draw_expected_dollars": float(fb_ev),
                "terminal_double_draw_no_fireball_cost_dollars": float(BASE_COST),
                "terminal_double_draw_no_fireball_average_gross_dollars": float(terminal_base_gross_avg),
                "terminal_double_draw_no_fireball_average_return_ratio": float(terminal_base_ratio),
                "terminal_double_draw_with_fireball_cost_dollars": float(terminal_fb_cost),
                "terminal_double_draw_with_fireball_average_gross_dollars": float(terminal_fb_gross_avg),
                "terminal_double_draw_with_fireball_average_return_ratio": float(terminal_fb_ratio),
            }
        )

    max_no_fb = max(Fraction(str(r["terminal_double_draw_no_fireball_average_return_ratio"])) for r in rows)
    max_fb = max(Fraction(str(r["terminal_double_draw_with_fireball_average_return_ratio"])) for r in rows)

    # Strict-profit impossibility gates.
    assert max_no_fb <= 1
    assert max_fb < 1
    assert max_no_fb == 1

    payload = {
        "packet": "H265",
        "candidate": "New Jersey Pick-3 Green Ball terminal guaranteed Double Draw",
        "status": "CLOSED_REJECTED",
        "promotion_checked": "2026-07-06 through 2026-08-03",
        "promotion_active_on_validation_date": False,
        "terminal_state_granted": "six white balls already removed, so Green Ball is the only remaining promotion ball",
        "base_wager_dollars": 0.50,
        "fireball_addon_dollars": 0.50,
        "green_ball_fireball_included": False,
        "rows": rows,
        "max_terminal_average_return_ratio_no_fireball": float(max_no_fb),
        "max_terminal_average_return_ratio_with_fireball": float(max_fb),
        "strict_profit_guarantee_possible_from_green_ball_fixed_wagers": False,
        "proof": "For any portfolio, minimum gross over legal draw outcomes is at most its average gross. Every primitive terminal average return is <= 100%; nonnegative mixtures, Straight/Box combinations, and Wheels inherit the bound. FIREBALL is <100% because it adds cost and is excluded from Green Ball winner determination.",
        "instant_match_note": "Instant Match is a separate paid random add-on with a legal nonwinning result; it adds cost and no positive worst-case floor, so it cannot rescue a strict guarantee.",
        "official_sources": [
            "https://www.njlottery.com/en-us/drawgames/pick3.html",
            "https://www.njlottery.com/en-us/newsandevents/newsinput/2026/press-releases/P3_GreenBallPromotionResults_081826.html",
        ],
    }

    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(payload, indent=2) + "\n")
    print(json.dumps(payload, indent=2))


if __name__ == "__main__":
    main()
