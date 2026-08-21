"""H159 fixed-board raffle residual-takeover worst-case floor.

If e external tickets are already sold from a fixed board of T tickets and W
winning slots, a buyer who acquires every remaining ticket can be guaranteed
only the W-e cheapest prizes when e < W. External tickets may occupy the e
most valuable winning slots. If e >= W the strict prize floor is zero.
"""

from dataclasses import dataclass


@dataclass(frozen=True)
class Raffle:
    name: str
    total_tickets: int
    ticket_price: float
    prizes: tuple[float, ...]


def residual_floor(raffle: Raffle, external_sold: int) -> tuple[float, float, float]:
    if not 0 <= external_sold <= raffle.total_tickets:
        raise ValueError("external_sold out of range")
    prizes = sorted(raffle.prizes)
    forced_slots = max(0, len(prizes) - external_sold)
    forced_payout = sum(prizes[:forced_slots])
    acquisition_cost = (raffle.total_tickets - external_sold) * raffle.ticket_price
    return forced_payout, acquisition_cost, forced_payout - acquisition_cost


def best_residual_state(raffle: Raffle):
    best = None
    for e in range(min(len(raffle.prizes), raffle.total_tickets) + 1):
        payout, cost, margin = residual_floor(raffle, e)
        row = (margin, e, payout, cost)
        if best is None or row[0] > best[0]:
            best = row
    return best


if __name__ == "__main__":
    virginia_2026 = Raffle(
        name="Virginia Commanders/Capitals 2026 design",
        total_tickets=150_000,
        ticket_price=20.0,
        prizes=tuple([100.0] * 3_000 + [500.0] * 500 + [10_000.0] * 5 + [950_000.0]),
    )
    print("winners", len(virginia_2026.prizes))
    print("board", sum(virginia_2026.prizes))
    print("full_cost", virginia_2026.total_tickets * virginia_2026.ticket_price)
    print("best", best_residual_state(virginia_2026))
