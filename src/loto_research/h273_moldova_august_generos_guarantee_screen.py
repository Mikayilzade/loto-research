"""H273: strict-guarantee screen for Moldova National Lottery's AUGUST GENEROS 2026.

This module formalizes only claims that follow from the published promotion
structure.  It does not estimate EV and it does not assume control of other
participants.
"""
from __future__ import annotations
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "data" / "derived" / "h273_moldova_august_generos_guarantee_screen.json"

ENTRY_TURNOVER_MDL = 100
CURRENT_CASH_SUBSTITUTE_MDL = 1_000_000
FIRST_PERIOD_CASH_PRIZES_MDL = 7 * 100_000
SECOND_PERIOD_CASH_SUBSTITUTES_MDL = 7 * 60_000
ALL_SPECIAL_CASH_EQUIVALENT_MDL = (
    FIRST_PERIOD_CASH_PRIZES_MDL
    + SECOND_PERIOD_CASH_SUBSTITUTES_MDL
    + CURRENT_CASH_SUBSTITUTE_MDL
)
TOURNAMENT_BONUS_POOL_MDL = 500_000
TOURNAMENT_PAID_PLACES = 1_000


def current_special_draw_floor(own_entries: int, external_entries: int) -> int:
    """Worst-case current-period special-prize cash floor.

    There is one winner.  If any external eligible entry exists, selecting it
    is a legal outcome, so the player's strict floor from this draw is zero.
    """
    assert own_entries >= 0 and external_entries >= 0
    if own_entries > 0 and external_entries == 0:
        return CURRENT_CASH_SUBSTITUTE_MDL
    return 0


def tournament_floor(own_score: int, external_scores: list[int]) -> int:
    """Return a conservative bonus floor based only on published paid-place count.

    If at least 1,000 external competitors can finish above the player's score,
    rank can be outside all paid places and the guaranteed tournament bonus is 0.
    """
    assert own_score >= 0 and all(x >= 0 for x in external_scores)
    better = sum(x > own_score for x in external_scores)
    return 0 if better >= TOURNAMENT_PAID_PLACES else -1  # -1 = requires full prize-table rank resolution


def main() -> None:
    # Structural witnesses: one external raffle entry destroys the current
    # special-prize guarantee regardless of how many entries we buy.
    for own in (1, 10, 10_000, 10_000_000):
        assert current_special_draw_floor(own, 1) == 0

    # No published points cap: for any finite own score, a legal adversarial
    # configuration with 1,000 higher external scores leaves no tournament floor.
    for own_score in (0, 1, 10_000, 10**9):
        assert tournament_floor(own_score, [own_score + 1] * 1_000) == 0

    result = {
        "packet": "H273",
        "subject": "Moldova National Lottery / 7777.md AUGUST GENEROS 2026",
        "campaign_period": "2026-08-01 through 2026-08-31",
        "entry_turnover_mdl": ENTRY_TURNOVER_MDL,
        "special_prizes_cash_equivalent_mdl": {
            "aug_1_6": FIRST_PERIOD_CASH_PRIZES_MDL,
            "aug_7_16": SECOND_PERIOD_CASH_SUBSTITUTES_MDL,
            "aug_17_30": CURRENT_CASH_SUBSTITUTE_MDL,
            "campaign_total": ALL_SPECIAL_CASH_EQUIVALENT_MDL,
        },
        "tournament_bonus_pool_mdl": TOURNAMENT_BONUS_POOL_MDL,
        "tournament_paid_places": TOURNAMENT_PAID_PLACES,
        "strict_guarantee": {
            "current_special_draw_floor_with_one_external_entry_mdl": 0,
            "tournament_floor_with_1000_higher_external_scores_mdl": 0,
            "calendar_bonus_fixed_cash_floor_mdl": 0,
        },
        "blockers": [
            "Special-prize entries are auto-generated from turnover and the winner is selected randomly; identifiers are not player-reservable.",
            "A single external eligible entry preserves a legal current-period outcome paying the player zero special-prize cash.",
            "Tournament points have no published participant/score cap; 1,000 higher external scores can legally push any finite player score outside paid places.",
            "Tournament awards are bonus funds, not cash, and carry x10 E-ticket or x5 SPORT wagering conditions.",
            "Calendar offers are conditional/periodic and several awards are random, so they do not provide a fixed precommitted cash floor.",
        ],
        "conclusion": "CLOSED / REJECTED for strict deterministic-profit construction under the published August 2026 rules; the campaign adds real external promotional money but it is not monopolizable or deterministically allocable to a finite player portfolio.",
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(result, indent=2, ensure_ascii=False) + "\n")
    print(json.dumps(result, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
