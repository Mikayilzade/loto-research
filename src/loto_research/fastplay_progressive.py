from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable


@dataclass(frozen=True)
class PrizeTier:
    value: float
    count: int


def fixed_grid_average(tiers: Iterable[PrizeTier], grid_size: int = 150_000) -> float:
    """Average face-value payout from the published non-jackpot grid."""
    return sum(t.value * t.count for t in tiers) / grid_size


def jackpot_break_even(
    ticket_price: float,
    fixed_average: float,
    jackpot_share: float,
    jackpot_bonus: float = 0.0,
    jackpot_grid_size: int = 500_000,
) -> float:
    """Nominal jackpot required for EV=ticket_price.

    Free-ticket tiers may be supplied at face value upstream; therefore this is a
    favorable nominal threshold, not a guaranteed cash-profit threshold.
    """
    if jackpot_share <= 0:
        raise ValueError("jackpot_share must be positive")
    return ((ticket_price - fixed_average) * jackpot_grid_size - jackpot_bonus) / jackpot_share


def nominal_ev(
    jackpot: float,
    fixed_average: float,
    jackpot_share: float,
    jackpot_bonus: float = 0.0,
    jackpot_grid_size: int = 500_000,
) -> float:
    return fixed_average + (jackpot_share * jackpot + jackpot_bonus) / jackpot_grid_size
