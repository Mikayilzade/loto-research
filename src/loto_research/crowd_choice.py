from __future__ import annotations

from dataclasses import dataclass, field
from math import comb, exp, sqrt
from random import Random
from typing import Sequence


@dataclass(frozen=True)
class CrowdBiasParameters:
    """Synthetic crowd-choice parameters.

    Positive weights make a feature more attractive to the simulated crowd.
    Literature establishes that these biases exist, but a target lottery must
    be calibrated separately before real-EV conclusions are allowed.
    """

    birthday_cutoff: int = 31
    birthday_weight: float = 0.0
    lucky_numbers: frozenset[int] = field(default_factory=lambda: frozenset({7}))
    lucky_weight: float = 0.0
    center_weight: float = 0.0
    consecutive_pair_weight: float = 0.0
    even_spacing_weight: float = 0.0
    candidate_batch: int = 32


@dataclass(frozen=True)
class IntensityEstimate:
    probability: float
    standard_error: float
    simulations: int

    def expected_other_winners(self, other_tickets: int) -> float:
        if other_tickets < 0:
            raise ValueError("other_tickets cannot be negative")
        return other_tickets * self.probability


def validate_line(line: Sequence[int], pool_size: int, picks: int) -> tuple[int, ...]:
    if pool_size <= 0:
        raise ValueError("pool_size must be positive")
    if picks <= 0 or picks > pool_size:
        raise ValueError("picks must be in 1..pool_size")

    result = tuple(sorted(int(value) for value in line))
    if len(result) != picks:
        raise ValueError("line length does not match picks")
    if len(set(result)) != picks:
        raise ValueError("line must not contain duplicates")
    if result[0] < 1 or result[-1] > pool_size:
        raise ValueError("line contains a number outside the pool")
    return result


def consecutive_pair_count(line: Sequence[int]) -> int:
    ordered = tuple(sorted(line))
    return sum(int(right - left == 1) for left, right in zip(ordered, ordered[1:]))


def even_spacing_score(line: Sequence[int]) -> float:
    """Return a simple 0..1 proxy for evenly-spaced/representative sets."""
    ordered = tuple(sorted(line))
    if len(ordered) < 3:
        return 1.0
    gaps = [right - left for left, right in zip(ordered, ordered[1:])]
    average = sum(gaps) / len(gaps)
    variance = sum((gap - average) ** 2 for gap in gaps) / len(gaps)
    return 1.0 / (1.0 + variance)


def center_score(line: Sequence[int], pool_size: int) -> float:
    """Return a 0..1-ish average preference for the center of a number range."""
    midpoint = (pool_size + 1) / 2.0
    half_range = max(pool_size / 2.0, 1.0)
    return sum(
        max(0.0, 1.0 - abs(number - midpoint) / half_range)
        for number in line
    ) / len(line)


def line_crowd_score(
    line: Sequence[int],
    pool_size: int,
    picks: int,
    params: CrowdBiasParameters,
) -> float:
    """Unnormalized log-attractiveness proxy for a manually selected line."""
    ordered = validate_line(line, pool_size, picks)
    return (
        params.birthday_weight
        * sum(int(number <= params.birthday_cutoff) for number in ordered)
        + params.lucky_weight
        * sum(int(number in params.lucky_numbers) for number in ordered)
        + params.center_weight * center_score(ordered, pool_size)
        + params.consecutive_pair_weight * consecutive_pair_count(ordered)
        + params.even_spacing_weight * even_spacing_score(ordered)
    )


def sample_uniform_line(
    pool_size: int,
    picks: int,
    rng: Random,
) -> tuple[int, ...]:
    if pool_size <= 0 or picks <= 0 or picks > pool_size:
        raise ValueError("invalid pool_size/picks")
    return tuple(sorted(rng.sample(range(1, pool_size + 1), picks)))


def _weighted_choice(
    candidates: Sequence[tuple[int, ...]],
    scores: Sequence[float],
    rng: Random,
) -> tuple[int, ...]:
    max_score = max(scores)
    weights = [exp(score - max_score) for score in scores]
    threshold = rng.random() * sum(weights)
    cumulative = 0.0
    for candidate, weight in zip(candidates, weights):
        cumulative += weight
        if threshold <= cumulative:
            return candidate
    return candidates[-1]


def sample_crowd_line(
    pool_size: int,
    picks: int,
    params: CrowdBiasParameters,
    rng: Random,
) -> tuple[int, ...]:
    """Sample from a flexible synthetic human-choice distribution.

    A small batch of uniform lines is drawn and one is selected using a softmax
    over behavioral feature scores. This avoids enumerating tens of millions of
    combinations while preserving a tunable non-uniform crowd.
    """
    batch = max(1, int(params.candidate_batch))
    candidates = [
        sample_uniform_line(pool_size, picks, rng)
        for _ in range(batch)
    ]
    scores = [
        line_crowd_score(candidate, pool_size, picks, params)
        for candidate in candidates
    ]
    return _weighted_choice(candidates, scores, rng)


def sample_draw_conditioned_on_ticket_matches(
    ticket: Sequence[int],
    pool_size: int,
    draw_picks: int,
    matches: int,
    rng: Random,
) -> tuple[int, ...]:
    """Sample a uniform draw conditional on `ticket` obtaining `matches` hits."""
    ticket_set = set(ticket)
    if len(ticket_set) != len(ticket):
        raise ValueError("ticket must contain unique numbers")
    if any(number < 1 or number > pool_size for number in ticket_set):
        raise ValueError("ticket contains a number outside the pool")
    if draw_picks <= 0 or draw_picks > pool_size:
        raise ValueError("invalid draw_picks")
    if matches < 0 or matches > min(len(ticket_set), draw_picks):
        raise ValueError("invalid matches")

    outside = [number for number in range(1, pool_size + 1) if number not in ticket_set]
    outside_needed = draw_picks - matches
    if outside_needed > len(outside):
        raise ValueError("condition is impossible")

    chosen = list(rng.sample(tuple(ticket_set), matches))
    chosen.extend(rng.sample(outside, outside_needed))
    return tuple(sorted(chosen))


def match_count(line: Sequence[int], draw: Sequence[int]) -> int:
    return len(set(line).intersection(draw))


def estimate_competitor_hit_probability(
    target_line: Sequence[int],
    pool_size: int,
    draw_picks: int,
    target_matches: int,
    competitor_matches: int,
    params: CrowdBiasParameters,
    *,
    simulations: int = 10_000,
    seed: int = 0,
) -> IntensityEstimate:
    """Estimate crowd competitor intensity conditional on our target-tier hit."""
    if simulations <= 0:
        raise ValueError("simulations must be positive")
    target = validate_line(target_line, pool_size, len(target_line))
    rng = Random(seed)
    hits = 0

    for _ in range(simulations):
        draw = sample_draw_conditioned_on_ticket_matches(
            target,
            pool_size,
            draw_picks,
            target_matches,
            rng,
        )
        competitor = sample_crowd_line(
            pool_size,
            len(target),
            params,
            rng,
        )
        hits += int(match_count(competitor, draw) == competitor_matches)

    probability = hits / simulations
    standard_error = sqrt(probability * (1.0 - probability) / simulations)
    return IntensityEstimate(probability, standard_error, simulations)


def anti_crowd_candidates(
    pool_size: int,
    picks: int,
    params: CrowdBiasParameters,
    *,
    candidate_count: int = 1_000,
    top_n: int = 20,
    seed: int = 0,
) -> list[tuple[float, tuple[int, ...]]]:
    """Generate candidate lines with the lowest synthetic crowd-attraction score."""
    if candidate_count <= 0 or top_n <= 0:
        raise ValueError("candidate_count and top_n must be positive")
    total_combinations = comb(pool_size, picks)
    if candidate_count > total_combinations:
        raise ValueError("candidate_count exceeds the combination space")

    rng = Random(seed)
    seen: set[tuple[int, ...]] = set()
    scored: list[tuple[float, tuple[int, ...]]] = []
    while len(seen) < candidate_count:
        line = sample_uniform_line(pool_size, picks, rng)
        if line in seen:
            continue
        seen.add(line)
        scored.append((line_crowd_score(line, pool_size, picks, params), line))

    scored.sort(key=lambda item: (item[0], item[1]))
    return scored[: min(top_n, len(scored))]


def relative_intensity(
    candidate: IntensityEstimate,
    baseline: IntensityEstimate,
) -> float:
    if baseline.probability <= 0.0:
        raise ValueError("baseline probability must be positive")
    return candidate.probability / baseline.probability
