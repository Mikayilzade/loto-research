"""Exact expected-value helpers for shared category prize pools.

A pari-mutuel/category-pool lottery does not pay a fixed amount merely because
our ticket lands in a category.  The category fund is divided among all winning
entries.  These helpers model the baseline case where other entries are
independent and have the same category probability.

Crowd-number-choice models can later replace the uniform assumptions.
"""

from __future__ import annotations

from .probability import expected_jackpot_share_fraction


def expected_shared_pool_payout(
    category_probability: float,
    pool_value: float,
    other_entries: int,
    our_pool_contribution: float = 0.0,
) -> float:
    """Expected payout to one entry from one shared prize category.

    Conditional on our entry landing in the category, let X be the number of
    other winning entries.  Under the baseline model:

        X ~ Binomial(other_entries, category_probability)

    and our share is 1/(1+X).

    ``pool_value`` is the category balance existing before our entry.  If our
    purchase itself adds a known amount to that category, pass it separately as
    ``our_pool_contribution`` so large-portfolio/self-impact models can account
    for it explicitly.
    """

    if not 0.0 <= category_probability <= 1.0:
        raise ValueError("category_probability must be between 0 and 1")
    if pool_value < 0 or our_pool_contribution < 0:
        raise ValueError("pool values cannot be negative")
    if other_entries < 0:
        raise ValueError("other_entries cannot be negative")

    if category_probability == 0.0:
        return 0.0

    share = expected_jackpot_share_fraction(other_entries, category_probability)
    return (
        category_probability
        * (pool_value + our_pool_contribution)
        * share
    )


def expected_shared_pool_payout_closed_form(
    category_probability: float,
    pool_value: float,
    total_entries_including_us: int,
) -> float:
    """Equivalent closed form for a pre-existing pool and uniform entries.

    For N total entries including ours:

        EV = B/N * [1 - (1-p)^N]

    This identity is useful because it exposes the economic meaning:
    - when Np is large, the bracket is almost 1 and EV ~= B/N;
    - when the category is rare, the bracket is below 1 because there is a
      meaningful chance nobody wins and the pool is not paid this draw.

    The fate of an unpaid pool (carryover, redistribution, reserve, etc.) is a
    separate state-transition rule and must not be guessed here.
    """

    if not 0.0 <= category_probability <= 1.0:
        raise ValueError("category_probability must be between 0 and 1")
    if pool_value < 0:
        raise ValueError("pool_value cannot be negative")
    if total_entries_including_us <= 0:
        raise ValueError("total_entries_including_us must be positive")

    p = category_probability
    n = total_entries_including_us
    return (pool_value / n) * (1.0 - (1.0 - p) ** n)


def zero_winner_probability(category_probability: float, entries: int) -> float:
    """Probability a category has no winner among ``entries`` uniform entries."""

    if not 0.0 <= category_probability <= 1.0:
        raise ValueError("category_probability must be between 0 and 1")
    if entries < 0:
        raise ValueError("entries cannot be negative")
    return (1.0 - category_probability) ** entries
