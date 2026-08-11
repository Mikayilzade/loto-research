"""Exact probability and baseline EV helpers for lottery research.

The functions in this module deliberately use analytical combinatorics where
possible. Simulation should be layered on top only when the game mechanics or
portfolio interactions make exact enumeration impractical.
"""

from __future__ import annotations

from math import comb
from typing import Dict, Iterable, Sequence, Tuple


PrizeTier = Tuple[float, float]

# Official 4+4 mechanics use two independent 4-from-20 boards.  The public
# game page states that 11 prize categories exist and that 1+2 / 2+1 / 0+3 /
# 3+0 are the minimum winning configurations.  These grouped match patterns
# are therefore a convenient exact probability basis; payout values are kept
# out of this module because they can vary by draw and/or pool state.
FOUR_PLUS_FOUR_CATEGORY_PATTERNS = {
    "I": ((4, 4),),
    "II": ((4, 3), (3, 4)),
    "III": ((4, 2), (2, 4)),
    "IV": ((4, 1), (1, 4)),
    "V": ((4, 0), (0, 4)),
    "VI": ((3, 3),),
    "VII": ((3, 2), (2, 3)),
    "VIII": ((3, 1), (1, 3)),
    "IX": ((3, 0), (0, 3)),
    "X": ((2, 2),),
    "XI": ((2, 1), (1, 2)),
}


def _validate_pool(pool_size: int, player_picks: int, draw_picks: int) -> None:
    if pool_size <= 0:
        raise ValueError("pool_size must be positive")
    if player_picks < 0 or draw_picks < 0:
        raise ValueError("pick counts cannot be negative")
    if player_picks > pool_size or draw_picks > pool_size:
        raise ValueError("pick counts cannot exceed pool_size")


def single_pool_match_probability(
    pool_size: int,
    player_picks: int,
    draw_picks: int,
    matches: int,
) -> float:
    """Return the exact hypergeometric probability of exactly ``matches``.

    This general form supports both ordinary lotteries and keno-style games.

    Examples
    --------
    * Beşdə 5: pool=36, player_picks=5, draw_picks=5.
    * Super Keno: pool=70, player_picks=10, draw_picks=20.
    """

    _validate_pool(pool_size, player_picks, draw_picks)

    if matches < 0:
        return 0.0

    max_matches = min(player_picks, draw_picks)
    min_matches = max(0, player_picks + draw_picks - pool_size)
    if matches < min_matches or matches > max_matches:
        return 0.0

    favorable = comb(player_picks, matches) * comb(
        pool_size - player_picks,
        draw_picks - matches,
    )
    total = comb(pool_size, draw_picks)
    return favorable / total


def multi_pool_match_probability(
    pools: Sequence[Tuple[int, int, int, int]],
) -> float:
    """Multiply exact match probabilities for independent pools/stages.

    Each item is ``(pool_size, player_picks, draw_picks, matches)``.
    This is suitable when the pools are distinct, or when a game's rules reset
    the population between stages (for example independent A/B boards).
    """

    probability = 1.0
    for pool_size, player_picks, draw_picks, matches in pools:
        probability *= single_pool_match_probability(
            pool_size,
            player_picks,
            draw_picks,
            matches,
        )
    return probability


def four_plus_four_category_probabilities() -> Dict[str, float]:
    """Return exact probabilities for the 11 grouped 4+4 match categories.

    Each board is an independent hypergeometric draw: the player selects 4 of
    20 and 4 are drawn.  Balls are returned before the B-board draw, so the
    board probabilities multiply.

    Payout amounts are deliberately not encoded here.  The research model must
    attach the draw-specific or rule-version-specific payout separately.
    """

    board_probabilities = {
        matches: single_pool_match_probability(20, 4, 4, matches)
        for matches in range(5)
    }

    return {
        category: sum(
            board_probabilities[a_matches] * board_probabilities[b_matches]
            for a_matches, b_matches in patterns
        )
        for category, patterns in FOUR_PLUS_FOUR_CATEGORY_PATTERNS.items()
    }


def four_plus_four_any_prize_probability() -> float:
    """Return probability that one 4+4 variant reaches any prize category."""

    return sum(four_plus_four_category_probabilities().values())


def jackpot_denominator_two_pool(
    main_pool: int,
    main_picks: int,
    bonus_pool: int,
    bonus_picks: int = 1,
) -> int:
    """Return the exact 1-in-N jackpot denominator for two independent pools."""

    if main_pool <= 0 or bonus_pool <= 0:
        raise ValueError("pool sizes must be positive")
    if not 0 <= main_picks <= main_pool:
        raise ValueError("invalid main_picks")
    if not 0 <= bonus_picks <= bonus_pool:
        raise ValueError("invalid bonus_picks")

    return comb(main_pool, main_picks) * comb(bonus_pool, bonus_picks)


def expected_gross_payout(prize_tiers: Iterable[PrizeTier]) -> float:
    """Return sum(probability * payout) for mutually exclusive prize tiers."""

    total = 0.0
    for probability, payout in prize_tiers:
        if not 0.0 <= probability <= 1.0:
            raise ValueError("tier probability must be between 0 and 1")
        if payout < 0:
            raise ValueError("payout cannot be negative")
        total += probability * payout
    return total


def net_expected_value(ticket_cost: float, prize_tiers: Iterable[PrizeTier]) -> float:
    """Return expected gross payout minus ticket cost."""

    if ticket_cost < 0:
        raise ValueError("ticket_cost cannot be negative")
    return expected_gross_payout(prize_tiers) - ticket_cost


def expected_roi(ticket_cost: float, prize_tiers: Iterable[PrizeTier]) -> float:
    """Return net expected value divided by ticket cost."""

    if ticket_cost <= 0:
        raise ValueError("ticket_cost must be positive")
    return net_expected_value(ticket_cost, prize_tiers) / ticket_cost


def expected_jackpot_share_fraction(
    other_tickets: int,
    other_ticket_jackpot_probability: float,
) -> float:
    """Expected fraction of a shared jackpot conditional on our ticket winning.

    Assumes every other ticket independently wins the same jackpot with
    probability ``other_ticket_jackpot_probability``. If X is the number of
    other winning tickets, this returns E[1/(1+X)].

    This is a baseline crowd model, not a claim that real player selections are
    independent or uniformly distributed. Popular-number research can replace
    the probability input with an empirically estimated collision probability.
    """

    if other_tickets < 0:
        raise ValueError("other_tickets cannot be negative")
    q = other_ticket_jackpot_probability
    if not 0.0 <= q <= 1.0:
        raise ValueError("probability must be between 0 and 1")
    if other_tickets == 0 or q == 0.0:
        return 1.0
    if q == 1.0:
        return 1.0 / (other_tickets + 1)

    return (1.0 - (1.0 - q) ** (other_tickets + 1)) / (
        (other_tickets + 1) * q
    )


def expected_jackpot_component(
    jackpot_cash_value: float,
    jackpot_win_probability: float,
    expected_share_fraction: float = 1.0,
    effective_tax_rate: float = 0.0,
) -> float:
    """Expected after-tax jackpot contribution to one ticket's gross payout."""

    if jackpot_cash_value < 0:
        raise ValueError("jackpot_cash_value cannot be negative")
    if not 0.0 <= jackpot_win_probability <= 1.0:
        raise ValueError("jackpot_win_probability must be between 0 and 1")
    if not 0.0 <= expected_share_fraction <= 1.0:
        raise ValueError("expected_share_fraction must be between 0 and 1")
    if not 0.0 <= effective_tax_rate <= 1.0:
        raise ValueError("effective_tax_rate must be between 0 and 1")

    after_tax_value = jackpot_cash_value * (1.0 - effective_tax_rate)
    return jackpot_win_probability * expected_share_fraction * after_tax_value
