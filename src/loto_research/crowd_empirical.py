from __future__ import annotations

from dataclasses import dataclass
from math import prod
from typing import Mapping, Sequence


@dataclass(frozen=True)
class PublishedCrowdAnchor:
    """Sparse relative crowd-choice anchor from published manual-pick data.

    Multipliers are relative to uniform marginal selection. Unreported numbers
    default to 1.0. This is for sensitivity/ranking only; it is not a complete
    joint ticket distribution for any current target lottery.
    """

    pool_size: int
    picks: int
    number_multipliers: Mapping[int, float]
    pattern_class_multiplier: float = 1.0

    def line_weight(self, numbers: Sequence[int], *, pattern: bool = False) -> float:
        line = tuple(sorted(int(x) for x in numbers))
        if len(line) != self.picks or len(set(line)) != self.picks:
            raise ValueError("line must contain picks distinct numbers")
        if line[0] < 1 or line[-1] > self.pool_size:
            raise ValueError("line outside pool")
        weight = prod(float(self.number_multipliers.get(n, 1.0)) for n in line)
        if pattern:
            weight *= self.pattern_class_multiplier
        return weight

    def relative_weight(self, candidate: Sequence[int], baseline: Sequence[int]) -> float:
        return self.line_weight(candidate) / self.line_weight(baseline)


def dutch_lotto_6of45_anchor() -> PublishedCrowdAnchor:
    """Published anchors from Wang et al. (2016), Dutch Lotto.

    Uniform marginal selection = 6/45 = 13.333...%.
    Published frequencies: 11=16.5%, 7=16.3%, 37=10.3%, 38=10.5%.
    Diagonal/vertical pattern class: 0.9% actual vs 0.009% random.
    """
    uniform = 6.0 / 45.0
    observed = {11: 0.165, 7: 0.163, 37: 0.103, 38: 0.105}
    return PublishedCrowdAnchor(
        pool_size=45,
        picks=6,
        number_multipliers={n: f / uniform for n, f in observed.items()},
        pattern_class_multiplier=0.009 / 0.00009,
    )


def shrink_anchor_toward_uniform(anchor: PublishedCrowdAnchor, strength: float) -> PublishedCrowdAnchor:
    """Sensitivity control for the empirically observed jackpot-size homogenization.

    `strength=1` keeps published anchor deviations; `strength=0` sets all
    multipliers to uniform. The strength parameter is intentionally not fitted.
    """
    if not 0.0 <= strength <= 1.0:
        raise ValueError("strength must be between 0 and 1")
    numbers = {
        n: 1.0 + strength * (m - 1.0)
        for n, m in anchor.number_multipliers.items()
    }
    pattern = 1.0 + strength * (anchor.pattern_class_multiplier - 1.0)
    return PublishedCrowdAnchor(anchor.pool_size, anchor.picks, numbers, pattern)


def anti_crowd_choice_alone_can_guarantee_profit(
    *, ticket_cost: float, zero_return_outcome_exists: bool
) -> bool:
    """Necessary-condition screen for terminal guaranteed-profit claims.

    Anti-crowd choice changes sharing conditional on winning but not the draw
    events that are wins/losses. With positive cost and any zero-return outcome,
    strictly positive profit across every outcome is impossible.
    """
    if ticket_cost < 0:
        raise ValueError("ticket_cost cannot be negative")
    return not (ticket_cost > 0 and zero_return_outcome_exists)
