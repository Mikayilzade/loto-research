"""H263: Uganda LOTTO fixed-tier / special-roll-down structural screen.

Current Uganda LOTTO rules (v1.6) use a 6/52 matrix at UGX 1,000 per entry.
Prize divisions 7 (Match 3) and 8 (Match 2 + Bonus) are fixed at UGX 10,000 and
UGX 4,000 per winning entry.  The special jackpot roll-down rule explicitly
excludes fixed-payout divisions, so accumulated jackpot money cannot create the
NEXT-ACTION target of an external pool paid as a deterministic fixed amount per
lower-tier winning selection.

This script also computes the exact fixed-tier return of a one-copy full 6/52
cover for auditability.  It is not an executable full-cover proposal: the rules
also impose a UGX 500,000 per-participant daily wager cap.
"""
from __future__ import annotations

import json
from math import comb
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "data" / "derived" / "h263_uganda_lotto_fixed_tier_rolldown.json"


def main() -> None:
    total_entries = comb(52, 6)
    price = 1_000
    losing_nonbonus = 52 - 6 - 1

    counts = {
        "match6": 1,
        "match5_bonus": comb(6, 5),
        "match5": comb(6, 5) * losing_nonbonus,
        "match4_bonus": comb(6, 4) * losing_nonbonus,
        "match4": comb(6, 4) * comb(losing_nonbonus, 2),
        "match3_bonus": comb(6, 3) * comb(losing_nonbonus, 2),
        "match3": comb(6, 3) * comb(losing_nonbonus, 3),
        "match2_bonus": comb(6, 2) * comb(losing_nonbonus, 3),
    }

    fixed_gross = counts["match3"] * 10_000 + counts["match2_bonus"] * 4_000
    full_cover_cost = total_entries * price

    out = {
        "packet": "H263",
        "game": "Uganda National Lottery LOTTO",
        "rules_version": "1.6",
        "matrix": "6/52 + bonus",
        "entry_price_ugx": price,
        "participant_daily_wager_cap_ugx": 500_000,
        "full_cover_entries": total_entries,
        "full_cover_cost_ugx": full_cover_cost,
        "exact_category_counts_under_one_copy_full_cover": counts,
        "fixed_tiers": {
            "division_7_match3_ugx": 10_000,
            "division_8_match2_bonus_ugx": 4_000,
        },
        "fixed_tier_full_cover_gross_ugx": fixed_gross,
        "fixed_tier_return_ratio": fixed_gross / full_cover_cost,
        "special_roll_down_reaches_fixed_tiers": False,
        "reason": (
            "Rules 7.2 and 7.3 explicitly exclude fixed payout divisions from the "
            "special Division-1 roll-down. Ordinary Division-6 no-winner funds roll "
            "to next draw Division 1 rather than Division 7."
        ),
        "status": "REJECTED_AS_FIXED_PER_SELECTION_EXTERNAL_SUBSIDY_MECHANISM",
    }
    assert total_entries == 20_358_520
    assert counts["match3"] == 283_800
    assert counts["match2_bonus"] == 212_850
    assert fixed_gross == 3_689_400_000
    assert abs(out["fixed_tier_return_ratio"] - 0.1812214247401088) < 1e-15

    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(out, indent=2) + "\n")
    print(json.dumps(out, indent=2))


if __name__ == "__main__":
    main()
