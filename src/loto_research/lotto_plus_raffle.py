from __future__ import annotations

from math import comb, exp, fsum, lgamma, log
from statistics import mean
from typing import Sequence


def _tier_count(main_matches: int, bonus_match: int, pool_size: int = 47) -> int:
    """Count 6-number selections with exact main/bonus matches in a 6+bonus draw."""
    if bonus_match not in (0, 1):
        raise ValueError("bonus_match must be 0 or 1")
    if not 0 <= main_matches <= 6:
        raise ValueError("main_matches must be 0..6")
    remaining = 6 - main_matches - bonus_match
    if remaining < 0:
        return 0
    nonwinning = pool_size - 7
    return comb(6, main_matches) * comb(1, bonus_match) * comb(nonwinning, remaining)


def fixed_plus_ev(pool_size: int = 47) -> float:
    """Expected fixed-prize value of Lotto Plus 1 + Plus 2 + ordinary raffle per Plus line.

    Uses the pre-autumn-2026 6/47 rules and published fixed prize tables.
    Top prizes are treated at their published face amounts; prize-limit clauses are ignored,
    so this is an optimistic analytical value where relevant.
    """
    if pool_size != 47:
        raise ValueError("this calibration is for the current 6/47 regime only")
    denominator = comb(pool_size, 6)
    plus1 = {
        (6, 0): 1_000_000,
        (5, 1): 5_000,
        (5, 0): 500,
        (4, 1): 50,
        (4, 0): 20,
        (3, 1): 10,
        (3, 0): 3,
        (2, 1): 2,
    }
    plus2 = {
        (6, 0): 250_000,
        (5, 1): 2_500,
        (5, 0): 250,
        (4, 1): 25,
        (4, 0): 10,
        (3, 1): 5,
        (3, 0): 3,
        (2, 1): 2,
    }

    def table_ev(table: dict[tuple[int, int], float]) -> float:
        return sum(
            _tier_count(m, b, pool_size) / denominator * prize
            for (m, b), prize in table.items()
        )

    ordinary_raffle_ev = 500.0 / 10_000.0
    return table_ev(plus1) + table_ev(plus2) + ordinary_raffle_ev


def million_event_ev_per_plus_line(total_plus_lines: float) -> float:
    """Symmetric expected €1m event subsidy per eligible Plus line."""
    if total_plus_lines <= 0:
        raise ValueError("total_plus_lines must be positive")
    return 1_000_000.0 / total_plus_lines


def incremental_plus_ev(total_plus_lines: float) -> float:
    return fixed_plus_ev() + million_event_ev_per_plus_line(total_plus_lines)


def break_even_total_plus_lines(addon_cost: float = 1.0) -> float:
    """Eligible-entry count below which the €1 Plus add-on is +EV in this model."""
    base = fixed_plus_ev()
    if addon_cost <= base:
        return float("inf")
    return 1_000_000.0 / (addon_cost - base)


def event_count_posterior(
    raffle_winner_counts: Sequence[int],
    *,
    prior_shape: float = 0.5,
    prior_rate: float = 0.0,
) -> tuple[float, float]:
    """Gamma posterior for a common Poisson special-event winner intensity.

    Jeffreys-style prior defaults to Gamma(shape=0.5, rate=0).  This deliberately
    models only between-event mean intensity; it does not remove real-world
    overdispersion or execution uncertainty.
    """
    counts = [int(value) for value in raffle_winner_counts]
    if not counts or any(value < 0 for value in counts):
        raise ValueError("raffle_winner_counts must be non-empty and non-negative")
    if prior_shape <= 0 or prior_rate < 0:
        raise ValueError("invalid Gamma prior")
    return prior_shape + sum(counts), prior_rate + len(counts)


def posterior_mean_raffle_winners(raffle_winner_counts: Sequence[int]) -> float:
    shape, rate = event_count_posterior(raffle_winner_counts)
    return shape / rate


def posterior_predictive_tail_probability(
    raffle_winner_counts: Sequence[int],
    threshold: int,
) -> float:
    """P(next special-event winner count >= threshold) under Gamma-Poisson model."""
    if threshold < 0:
        raise ValueError("threshold must be non-negative")
    if threshold == 0:
        return 1.0
    shape, rate = event_count_posterior(raffle_winner_counts)
    # Gamma-Poisson predictive is NB(r=shape, p=rate/(rate+1)).
    p = rate / (rate + 1.0)
    q = 1.0 - p
    k = threshold
    log_pmf = (
        lgamma(k + shape)
        - lgamma(shape)
        - lgamma(k + 1.0)
        + shape * log(p)
        + k * log(q)
    )
    term = exp(log_pmf)
    terms = [term]
    # Sum the upper tail directly to avoid catastrophic cancellation when tiny.
    for _ in range(100_000):
        k += 1
        term *= ((k - 1 + shape) / k) * q
        if term == 0.0:
            break
        terms.append(term)
        if term < 1e-18 * max(fsum(terms), 1e-300):
            break
    return fsum(terms)


def mean_promotion_uplift(
    event_counts: Sequence[int],
    adjacent_before_counts: Sequence[int],
    adjacent_after_counts: Sequence[int],
) -> float:
    """Mean event/adjacent-average raffle-winner ratio across matched event windows."""
    if not (
        len(event_counts)
        == len(adjacent_before_counts)
        == len(adjacent_after_counts)
        and len(event_counts) > 0
    ):
        raise ValueError("all count sequences must have equal positive length")
    ratios = []
    for event, before, after in zip(event_counts, adjacent_before_counts, adjacent_after_counts):
        if event < 0 or before < 0 or after < 0:
            raise ValueError("counts cannot be negative")
        adjacent_mean = (before + after) / 2.0
        if adjacent_mean <= 0:
            raise ValueError("adjacent mean must be positive")
        ratios.append(event / adjacent_mean)
    return mean(ratios)


def strict_guarantee_possible_with_external_entries() -> bool:
    """The event cannot guarantee our €1m because another qualifying ticket may be selected."""
    return False
