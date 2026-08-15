from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable


@dataclass(frozen=True)
class TimeBin:
    start_minute: int
    end_minute: int
    probability: float

    def __post_init__(self) -> None:
        if not (0 <= self.start_minute < self.end_minute <= 24 * 60):
            raise ValueError("invalid time bin")
        if self.probability < 0:
            raise ValueError("probability cannot be negative")


# Official Virginia Lottery published selected-time prior for Lucky Contestant.
# Minutes are on a 24-hour clock.
OFFICIAL_TIME_BINS: tuple[TimeBin, ...] = (
    TimeBin(60, 120, 0.10),       # 01:00-02:00
    TimeBin(120, 480, 0.10),      # 02:00-08:00
    TimeBin(480, 840, 0.10),      # 08:00-14:00
    TimeBin(840, 1080, 0.10),     # 14:00-18:00
    TimeBin(1080, 1200, 0.15),    # 18:00-20:00
    TimeBin(1200, 1260, 0.15),    # 20:00-21:00
    TimeBin(1260, 1320, 0.15),    # 21:00-22:00
    TimeBin(1320, 1425, 0.15),    # 22:00-23:45
)


def validate_prior(bins: Iterable[TimeBin] = OFFICIAL_TIME_BINS) -> None:
    bins = tuple(bins)
    if abs(sum(b.probability for b in bins) - 1.0) > 1e-12:
        raise ValueError("time-bin probabilities must sum to 1")
    for left, right in zip(bins, bins[1:]):
        if left.end_minute != right.start_minute:
            raise ValueError("time bins must form a contiguous support")


def prior_mass(start_minute: float, end_minute: float,
               bins: Iterable[TimeBin] = OFFICIAL_TIME_BINS) -> float:
    """Prior probability that hidden selected time T lies in [start, end).

    The official page publishes weights for intervals but no within-bin density.
    This function uses the explicit modeling assumption of uniform density inside
    each published interval. Results from this function are therefore a model,
    not an operator-published within-bin rule.
    """
    if end_minute <= start_minute:
        return 0.0
    total = 0.0
    for b in bins:
        overlap = max(0.0, min(end_minute, b.end_minute) - max(start_minute, b.start_minute))
        if overlap:
            total += b.probability * overlap / (b.end_minute - b.start_minute)
    return total


def optimistic_truncated_next_window_probability(now_minute: float, window_minutes: float) -> float:
    """P(T in next window | T >= now), under uniform-within-bin model.

    This is intentionally an *optimistic information bound*. Actual observation
    'jackpot is still alive' does not necessarily prove T >= now because public
    rules allow the jackpot to be won earlier at standard odds and do not fully
    publish the reset/termination mechanics. Use this only as a best-case
    concentration screen, never as an executable posterior without more rules.
    """
    support_end = OFFICIAL_TIME_BINS[-1].end_minute
    remaining = prior_mass(now_minute, support_end)
    if remaining <= 0:
        return 0.0
    return prior_mass(now_minute, min(support_end, now_minute + window_minutes)) / remaining


def jackpot_only_break_even_probability(stake: float, jackpot: float) -> float:
    """Necessary jackpot probability if all non-jackpot value is ignored."""
    if stake <= 0 or jackpot <= 0:
        raise ValueError("stake and jackpot must be positive")
    return stake / jackpot


def equivalent_one_in(probability: float) -> float:
    if probability <= 0:
        return float("inf")
    return 1.0 / probability


def hidden_time_alone_can_guarantee_profit(
    *,
    positive_stake: bool,
    target_time_hidden: bool,
    jackpot_can_be_won_earlier_by_others: bool,
    losing_nonjackpot_outcome_exists: bool,
) -> bool:
    """Necessary-condition screen for the H018 terminal guarantee claim.

    If another player can legally terminate the target jackpot before the hidden
    selected time, and our positive-cost play can subsequently lose, then no
    late-time strategy based solely on the hidden-time mechanism guarantees
    positive profit across all legal outcome branches.
    """
    if (
        positive_stake
        and target_time_hidden
        and jackpot_can_be_won_earlier_by_others
        and losing_nonjackpot_outcome_exists
    ):
        return False
    return True
