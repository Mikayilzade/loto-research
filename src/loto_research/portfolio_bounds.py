from __future__ import annotations

from typing import Iterable, Sequence


def portfolio_expected_profit(
    quantities: Sequence[float],
    ticket_expected_payouts: Sequence[float],
    ticket_costs: Sequence[float],
) -> float:
    """Expected portfolio profit under additive ticket costs and payouts."""
    if not (len(quantities) == len(ticket_expected_payouts) == len(ticket_costs)):
        raise ValueError("all inputs must have equal length")
    total = 0.0
    for q, payout, cost in zip(quantities, ticket_expected_payouts, ticket_costs):
        if q < 0 or cost < 0 or payout < 0:
            raise ValueError("quantities, expected payouts and costs must be non-negative")
        total += q * (payout - cost)
    return total


def all_ticket_types_nonpositive_ev(
    ticket_expected_payouts: Iterable[float],
    ticket_costs: Iterable[float],
    *,
    tolerance: float = 1e-12,
) -> bool:
    payouts = tuple(ticket_expected_payouts)
    costs = tuple(ticket_costs)
    if len(payouts) != len(costs):
        raise ValueError("payout and cost lists must have equal length")
    if any(x < 0 for x in payouts + costs):
        raise ValueError("expected payouts and costs must be non-negative")
    return all(payout - cost <= tolerance for payout, cost in zip(payouts, costs))


def strict_guarantee_impossible_under_linearity(
    ticket_expected_payouts: Iterable[float],
    ticket_costs: Iterable[float],
    *,
    tolerance: float = 1e-12,
) -> bool:
    """Necessary-condition screen for strict all-outcome profit guarantees.

    If every available additive ticket type has non-positive expected profit,
    every non-negative portfolio also has non-positive expected profit. A
    portfolio that paid strictly positive profit in every positive-probability
    outcome would necessarily have positive expected profit, so such a
    guarantee is impossible under the linear/additive assumptions.
    """
    return all_ticket_types_nonpositive_ev(
        ticket_expected_payouts,
        ticket_costs,
        tolerance=tolerance,
    )
