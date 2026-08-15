from __future__ import annotations

from math import comb


WHITE_POOL = 69
WHITE_PICKS = 5
POWERBALL_POOL = 26
TICKET_COST = 2.0
COMBINATION_SPACE = comb(WHITE_POOL, WHITE_PICKS) * POWERBALL_POOL


def expected_jackpot_share(other_tickets: int, popularity_multiplier: float = 1.0) -> float:
    """Expected retained jackpot fraction conditional on our ticket winning.

    Other jackpot-winning tickets are modeled as independent draws over the
    combination space with exact-combination probability
    popularity_multiplier / COMBINATION_SPACE.
    """
    if other_tickets < 0:
        raise ValueError("other_tickets cannot be negative")
    if popularity_multiplier < 0:
        raise ValueError("popularity_multiplier cannot be negative")
    if popularity_multiplier == 0 or other_tickets == 0:
        return 1.0

    q = popularity_multiplier / COMBINATION_SPACE
    if q > 1:
        raise ValueError("popularity multiplier implies probability > 1")

    # If X~Binomial(n,q), E[1/(1+X)] has this closed form.
    n = other_tickets
    return (1.0 - (1.0 - q) ** (n + 1)) / ((n + 1) * q)


def required_cash_jackpot(
    lower_tier_ev: float,
    other_tickets: int,
    *,
    jackpot_retained_fraction: float = 1.0,
    popularity_multiplier: float = 1.0,
    ticket_cost: float = TICKET_COST,
) -> float:
    """Cash jackpot needed for single-ticket break-even under sharing haircut.

    `jackpot_retained_fraction` is deliberately generic: 1.0 means no tax or
    other jackpot haircut; 0.76 can be used as a 24% illustrative haircut; 0.70
    as a 30% illustrative haircut. It is not a claim about final tax liability.
    """
    if lower_tier_ev < 0:
        raise ValueError("lower_tier_ev cannot be negative")
    if ticket_cost <= 0:
        raise ValueError("ticket_cost must be positive")
    if not (0 < jackpot_retained_fraction <= 1):
        raise ValueError("jackpot_retained_fraction must be in (0,1]")

    gap = ticket_cost - lower_tier_ev
    if gap <= 0:
        return 0.0
    share = expected_jackpot_share(other_tickets, popularity_multiplier)
    return gap * COMBINATION_SPACE / (share * jackpot_retained_fraction)


def full_space_pre_jackpot_floor(lower_tier_ev: float) -> float:
    """Deterministic non-jackpot gross for buying every combination once.

    With fixed lower-tier prizes, full-space aggregation equals per-ticket
    lower-tier EV times the number of combinations.
    """
    if lower_tier_ev < 0:
        raise ValueError("lower_tier_ev cannot be negative")
    return lower_tier_ev * COMBINATION_SPACE


def full_space_required_jackpot_without_external_sharing(
    lower_tier_ev: float,
    *,
    ticket_cost: float = TICKET_COST,
) -> float:
    """Ideal full-space break-even cash jackpot before tax/execution/sharing."""
    total_cost = ticket_cost * COMBINATION_SPACE
    return max(0.0, total_cost - full_space_pre_jackpot_floor(lower_tier_ev))


def full_space_required_jackpot_with_external_winner_cap(
    lower_tier_ev: float,
    max_external_jackpot_winners: int,
    *,
    jackpot_retained_fraction: float = 1.0,
    ticket_cost: float = TICKET_COST,
) -> float:
    """Sufficient jackpot for full-space guarantee given a hard winner cap.

    If at most k external tickets can share the jackpot, our guaranteed share is
    at least 1/(k+1). Without a defensible pre-draw cap, this does not certify a
    guarantee.
    """
    if max_external_jackpot_winners < 0:
        raise ValueError("winner cap cannot be negative")
    if not (0 < jackpot_retained_fraction <= 1):
        raise ValueError("jackpot_retained_fraction must be in (0,1]")

    gap = full_space_required_jackpot_without_external_sharing(
        lower_tier_ev, ticket_cost=ticket_cost
    )
    return gap * (max_external_jackpot_winners + 1) / jackpot_retained_fraction
