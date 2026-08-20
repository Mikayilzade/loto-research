"""Deterministic worst-case floor for buying all remaining tickets in a fixed-board raffle.

If E tickets are already owned externally, an adversarial outcome can assign the E
highest-value winning slots to those external tickets. Buying every remaining ticket
therefore guarantees at most the residual prize-board value after removing the E
highest prizes. If E is at least the number of prize slots, the strict floor is zero.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable


@dataclass(frozen=True)
class TakeoverFloor:
    external_tickets: int
    remaining_tickets: int
    purchase_cost: float
    guaranteed_prize_floor: float
    gross_return: float


def full_remaining_takeover_floor(
    *,
    ticket_cap: int,
    ticket_price: float,
    prize_values: Iterable[float],
    external_tickets: int,
) -> TakeoverFloor:
    if ticket_cap <= 0 or ticket_price < 0:
        raise ValueError("invalid ticket cap/price")
    if not 0 <= external_tickets <= ticket_cap:
        raise ValueError("external_tickets must lie in [0, ticket_cap]")

    prizes = sorted((float(x) for x in prize_values), reverse=True)
    if any(x < 0 for x in prizes):
        raise ValueError("prizes must be non-negative")

    remaining = ticket_cap - external_tickets
    cost = remaining * ticket_price
    guaranteed = max(0.0, sum(prizes) - sum(prizes[:external_tickets]))
    gross = guaranteed / cost if cost else 0.0
    return TakeoverFloor(
        external_tickets=external_tickets,
        remaining_tickets=remaining,
        purchase_cost=cost,
        guaranteed_prize_floor=guaranteed,
        gross_return=gross,
    )
