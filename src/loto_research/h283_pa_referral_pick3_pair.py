"""H283 — Pennsylvania iLottery Refer-A-Friend bonus + PICK 3 Front Pair exact cover.

This is an arithmetic/execution-gate model, not a recommendation to gamble.
It proves the conditional cash floor if an eligible new PA iLottery account actually
receives the current $100 referral Bonus Money and all 100 Pair plays are accepted
for the same drawing.
"""
from __future__ import annotations
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "data" / "derived" / "h283_pa_referral_pick3_pair.json"

DEPOSIT = 10.0
REFERRAL_BONUS = 100.0
PAIR_COUNT = 100
PAIR_STAKE = 1.0
PAIR_PRIZE = 50.0
SINGLE_TICKET_MAX = 100.0


def main() -> None:
    cover_cost = PAIR_COUNT * PAIR_STAKE
    wallet = DEPOSIT + REFERRAL_BONUS
    guaranteed_cash_prize = PAIR_PRIZE
    cash_profit_vs_deposit = guaranteed_cash_prize - DEPOSIT
    assert PAIR_COUNT == 10 * 10
    assert cover_cost == 100.0
    assert cover_cost <= wallet
    assert cover_cost <= SINGLE_TICKET_MAX
    assert guaranteed_cash_prize > DEPOSIT
    assert cash_profit_vs_deposit == 40.0

    out = {
        "packet": "H283",
        "mechanism": "PA iLottery Refer-A-Friend $100 Bonus Money + PICK 3 Front Pair exact cover",
        "external_cash_deposit": DEPOSIT,
        "bonus_money": REFERRAL_BONUS,
        "starting_wallet": wallet,
        "pair_count": PAIR_COUNT,
        "pair_stake": PAIR_STAKE,
        "cover_cost": cover_cost,
        "pair_prize": PAIR_PRIZE,
        "guaranteed_cash_prize_if_full_cover_accepted": guaranteed_cash_prize,
        "cash_profit_vs_external_deposit_if_full_cover_accepted": cash_profit_vs_deposit,
        "cash_gross_multiple_vs_deposit": guaranteed_cash_prize / DEPOSIT,
        "profit_roi_vs_deposit": cash_profit_vs_deposit / DEPOSIT,
        "single_pick3_ticket_max": SINGLE_TICKET_MAX,
        "conditional_theorem": (
            "If an eligible referred new player receives the current $100 Bonus Money after a $10 first deposit, "
            "and PA iLottery accepts all 100 $1 Front Pair selections 00-99 for one PICK 3 draw, exactly one pair "
            "matches and pays $50 cash, yielding $40 gross cash profit versus the $10 external deposit."
        ),
        "rigorous_success_claimed": False,
        "remaining_gate": (
            "Official public evidence does not yet establish that the online system can atomically accept the complete "
            "100-selection Pair cover in one transaction without partial acceptance, system limits, or a promotion-specific execution block."
        ),
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(out, indent=2) + "\n")
    print(json.dumps(out, indent=2))


if __name__ == "__main__":
    main()
