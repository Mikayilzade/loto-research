"""H289: Kentucky Keno exact covers under the August 2026 bonus stack.

This module proves the arithmetic of two conditional constructions.  It does
NOT claim execution: the promotion stack and complete wager acceptance remain
separate gates documented in research/H289_STATUS.md.
"""
from __future__ import annotations

import json
from math import comb


def matched_deposit(deposit: int) -> int:
    return min(deposit, 250)


def spot1_certificate() -> dict:
    # One $1 Spot-1 play on every Keno number 1..80.
    # Exactly 20 distinct numbers are drawn, hence exactly 20 plays win $2.
    numbers = 80
    draw_size = 20
    wager = 1
    payout = 2
    plays = numbers
    cost = plays * wager
    guaranteed_winners = draw_size
    gross = guaranteed_winners * payout

    deposit = 30
    match = matched_deposit(deposit)
    referral = 20
    playable = deposit + match + referral

    assert plays == 80
    assert cost == 80
    assert guaranteed_winners == 20
    assert gross == 40
    assert playable == cost
    assert gross - deposit == 10

    return {
        "plays": plays,
        "cost": cost,
        "guaranteed_winners": guaranteed_winners,
        "prize_each": payout,
        "guaranteed_gross": gross,
        "cash_deposit": deposit,
        "first_deposit_match": match,
        "referral_bonus": referral,
        "playable_funds": playable,
        "conditional_profit_vs_cash_deposit": gross - deposit,
    }


def spot2_clique_certificate() -> dict:
    # Partition 80 numbers into six disjoint groups and buy every pair within
    # each group.  For any 20-number draw, convexity minimizes the number of
    # same-group drawn pairs at distribution 4,4,3,3,3,3.
    groups = [14, 14, 13, 13, 13, 13]
    assert sum(groups) == 80
    plays = sum(comb(n, 2) for n in groups)
    guaranteed_pairs = 2 * comb(4, 2) + 4 * comb(3, 2)
    payout = 11
    cost = plays
    gross = guaranteed_pairs * payout

    deposit = 237
    match = matched_deposit(deposit)
    referral = 20
    playable = deposit + match + referral

    assert plays == 494
    assert guaranteed_pairs == 24
    assert gross == 264
    assert playable == cost
    assert gross - deposit == 27

    return {
        "group_sizes": groups,
        "plays": plays,
        "cost": cost,
        "guaranteed_matching_pairs": guaranteed_pairs,
        "prize_each": payout,
        "guaranteed_gross": gross,
        "cash_deposit": deposit,
        "first_deposit_match": match,
        "referral_bonus": referral,
        "playable_funds": playable,
        "conditional_profit_vs_cash_deposit": gross - deposit,
    }


def result() -> dict:
    return {
        "packet": "H289",
        "status": "CONDITIONAL_POSITIVE_MATH__NOT_RIGOROUS_SUCCESS",
        "h225_lane": "CLOSED_EXHAUSTED",
        "spot1": spot1_certificate(),
        "spot2_clique_certificate": spot2_clique_certificate(),
        "math_positive_if_stacking_and_acceptance": True,
        "rigorous_success": False,
        "open_gates": [
            "Official August 2026 material does not explicitly prove that the Refer-A-Friend bonus stacks with the 100% first-deposit match.",
            "Kentucky iLottery Terms reserve the right to refuse attempted purchases and to limit wagers on particular number sets without notice, so complete same-draw cover acquisition is not guaranteed.",
        ],
    }


if __name__ == "__main__":
    print(json.dumps(result(), indent=2))
