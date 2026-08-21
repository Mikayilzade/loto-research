from __future__ import annotations

from math import comb
from typing import Mapping


def hit_count_in_full_cover(pool_size: int, drawn: int, spot: int, hits: int) -> int:
    """Number of spot-tickets with exactly `hits` matches when every spot-subset is owned."""
    if hits < 0 or hits > spot or hits > drawn:
        return 0
    misses = spot - hits
    if misses > pool_size - drawn:
        return 0
    return comb(drawn, hits) * comb(pool_size - drawn, misses)


def deterministic_full_cover(
    *,
    pool_size: int = 80,
    drawn: int = 20,
    spot: int,
    stake: float,
    payouts: Mapping[int, float],
) -> dict[str, float]:
    """Exact all-outcome gross for buying every `spot` subset under a fixed paytable.

    payouts maps exact hit-count j -> cash payout for one ticket.
    """
    tickets = comb(pool_size, spot)
    cost = stake * tickets
    gross = 0.0
    for hits, payout in payouts.items():
        gross += payout * hit_count_in_full_cover(pool_size, drawn, spot, hits)
    return {
        "tickets": tickets,
        "cost": cost,
        "gross": gross,
        "return_ratio": gross / cost,
        "deficit_fraction": 1.0 - gross / cost,
    }


def hit_k_only_break_even_multiplier(*, pool_size: int = 80, drawn: int = 20, spot: int) -> float:
    """Required Hit-k payout divided by stake for standalone deterministic break-even."""
    return comb(pool_size, spot) / comb(drawn, spot)


if __name__ == "__main__":
    # H148 reproduction: Omaha August 2026 special, $2 3-Spot, Hit 3 = $102.
    result = deterministic_full_cover(spot=3, stake=2.0, payouts={3: 102.0})
    assert result["tickets"] == 82160
    assert abs(result["gross"] - 116280.0) < 1e-9
    assert abs(result["return_ratio"] - 0.7076448406) < 1e-9
    print(result)
