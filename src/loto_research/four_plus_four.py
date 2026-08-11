"""Empirical payout-structure helpers for Azerbaijan 4+4 research.

This module deliberately separates exact combinatorics from empirical inference.
The category-pool ratios below are NOT yet promoted to official rules; they are
an observed pattern in preserved 2026 secondary draw tables and must be checked
against a larger sample and primary rules.
"""

from __future__ import annotations

from statistics import median
from typing import Mapping

from .probability import multi_pool_match_probability


# Empirically stable total-pool ratios observed in sampled 2026 draws.
# Categories V and VI are special: their combined total is approximately 2U,
# while the split between them changes from draw to draw.
STABLE_POOL_WEIGHTS = {
    3: 11.0,
    4: 5.0,
    7: 9.0,
    8: 14.0,
    9: 7.0,
}
COMBINED_5_6_WEIGHT = 2.0


def category_probability(a_matches: int, b_matches: int) -> float:
    """Exact probability of one ordered A/B match state."""

    return multi_pool_match_probability(
        [
            (20, 4, 4, a_matches),
            (20, 4, 4, b_matches),
        ]
    )


def grouped_category_probabilities() -> dict[int, float]:
    """Return exact probabilities for the 11 public grouped prize categories."""

    def sym(a: int, b: int) -> float:
        p = category_probability(a, b)
        return p if a == b else p + category_probability(b, a)

    return {
        1: category_probability(4, 4),
        2: sym(4, 3),
        3: sym(4, 2),
        4: sym(4, 1),
        5: sym(4, 0),
        6: category_probability(3, 3),
        7: sym(3, 2),
        8: sym(3, 1),
        9: sym(3, 0),
        10: category_probability(2, 2),
        11: sym(2, 1),
    }


def infer_pool_unit(category_totals: Mapping[int, float]) -> float:
    """Infer the common empirical pool unit U from stable categories.

    For sampled 2026 tables, categories III, IV, VII, VIII and IX closely follow
    11U, 5U, 9U, 14U and 7U. Median normalization is used for robustness to
    rounding and a bad source row.
    """

    missing = set(STABLE_POOL_WEIGHTS) - set(category_totals)
    if missing:
        raise ValueError(f"missing category totals: {sorted(missing)}")
    candidates = []
    for category, weight in STABLE_POOL_WEIGHTS.items():
        total = float(category_totals[category])
        if total < 0:
            raise ValueError("category totals cannot be negative")
        candidates.append(total / weight)
    return median(candidates)


def stable_pool_fit_error(category_totals: Mapping[int, float], unit: float | None = None) -> float:
    """Maximum relative deviation from the stable empirical pool-weight model."""

    if unit is None:
        unit = infer_pool_unit(category_totals)
    if unit <= 0:
        raise ValueError("unit must be positive")

    errors = []
    for category, weight in STABLE_POOL_WEIGHTS.items():
        observed = float(category_totals[category])
        expected = unit * weight
        errors.append(abs(observed - expected) / unit)
    return max(errors)


def combined_5_6_fit_error(category_totals: Mapping[int, float], unit: float | None = None) -> float:
    """Absolute deviation of categories V+VI from the empirical 2U combined pool."""

    if 5 not in category_totals or 6 not in category_totals:
        raise ValueError("categories 5 and 6 are required")
    if unit is None:
        unit = infer_pool_unit(category_totals)
    if unit <= 0:
        raise ValueError("unit must be positive")
    observed = float(category_totals[5]) + float(category_totals[6])
    return observed - COMBINED_5_6_WEIGHT * unit


def fixed_tail_expected_payout() -> float:
    """Exact EV contribution from observed fixed categories X=6 AZN and XI=4 AZN."""

    p = grouped_category_probabilities()
    return p[10] * 6.0 + p[11] * 4.0


def infer_variants_from_tail_winners(cat10_winners: int, cat11_winners: int) -> float:
    """Estimate sold variants from observed category X+XI winner counts.

    This is a method-of-moments estimator using exact category probabilities:

        N_hat = (W10 + W11) / (P10 + P11)

    It is preferable to choosing U/N by eye because it derives the variant
    volume independently from the payout pool. Real crowd selection is not
    perfectly uniform, so this remains a noisy estimate rather than official
    ticket-sales data.
    """

    if cat10_winners < 0 or cat11_winners < 0:
        raise ValueError("winner counts cannot be negative")
    p = grouped_category_probabilities()
    denominator = p[10] + p[11]
    return (cat10_winners + cat11_winners) / denominator


def empirical_unit_per_variant(
    unit: float,
    cat10_winners: int,
    cat11_winners: int,
) -> float:
    """Estimate U per sold variant from an independently inferred variant volume."""

    if unit < 0:
        raise ValueError("unit cannot be negative")
    variants = infer_variants_from_tail_winners(cat10_winners, cat11_winners)
    if variants <= 0:
        raise ValueError("tail winner counts imply zero variants")
    return unit / variants


def infer_variants_from_unit(unit: float, unit_per_variant: float = 0.01) -> float:
    """Convert U to an implied variant count under an explicit scaling assumption.

    The current empirical estimate across the first seven sampled 2026 draws is
    very close to U ~= 0.01 AZN per sold variant (median around 0.00995),
    equivalently about 0.5% of revenue if one variant costs 2 AZN. This remains
    an inference pending primary prize-allocation rules.
    """

    if unit < 0:
        raise ValueError("unit cannot be negative")
    if unit_per_variant <= 0:
        raise ValueError("unit_per_variant must be positive")
    return unit / unit_per_variant
