from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable, Sequence


@dataclass(frozen=True)
class BookLevel:
    price: float
    size: float


@dataclass(frozen=True)
class CompleteSetFill:
    quantity: float
    gross_cost: float
    fees: float
    extra_costs: float
    redemption: float
    guaranteed_profit: float
    roi: float
    profitable: bool


def _validate_levels(levels: Sequence[BookLevel]) -> None:
    if not levels:
        raise ValueError("orderbook side cannot be empty")
    for level in levels:
        if not (0.0 < level.price < 1.0):
            raise ValueError("binary token prices must be in (0,1)")
        if level.size <= 0:
            raise ValueError("level size must be positive")


def taker_fee(shares: float, price: float, fee_rate: float) -> float:
    """Polymarket V2-style taker fee for one fill.

    Official current documentation gives fee = C * feeRate * p * (1-p),
    where C is shares and p is execution price.  The caller supplies the
    per-market rate because it is dynamic/category dependent.
    """
    if shares < 0 or not (0.0 <= price <= 1.0) or fee_rate < 0:
        raise ValueError("invalid fee inputs")
    return shares * fee_rate * price * (1.0 - price)


def _walk_asks(levels: Sequence[BookLevel], quantity: float, fee_rate: float) -> tuple[float, float]:
    _validate_levels(levels)
    if quantity <= 0:
        raise ValueError("quantity must be positive")

    remaining = quantity
    notional = 0.0
    fees = 0.0
    for level in sorted(levels, key=lambda x: x.price):
        fill = min(remaining, level.size)
        if fill <= 0:
            continue
        notional += fill * level.price
        fees += taker_fee(fill, level.price, fee_rate)
        remaining -= fill
        if remaining <= 1e-12:
            break
    if remaining > 1e-12:
        raise ValueError("insufficient depth")
    return notional, fees


def fee_aware_binary_complete_set(
    yes_asks: Sequence[BookLevel],
    no_asks: Sequence[BookLevel],
    quantity: float,
    *,
    yes_fee_rate: float = 0.0,
    no_fee_rate: float = 0.0,
    extra_costs: float = 0.0,
    redemption_per_pair: float = 1.0,
) -> CompleteSetFill:
    """Evaluate acquiring equal YES+NO quantities from executable asks.

    The result is deterministic only after both legs are filled and the two
    tokens share the same complete-set settlement/merge definition.
    """
    if quantity <= 0 or extra_costs < 0 or redemption_per_pair <= 0:
        raise ValueError("invalid quantity/cost/redemption")
    yes_cost, yes_fees = _walk_asks(yes_asks, quantity, yes_fee_rate)
    no_cost, no_fees = _walk_asks(no_asks, quantity, no_fee_rate)
    gross_cost = yes_cost + no_cost
    fees = yes_fees + no_fees
    redemption = quantity * redemption_per_pair
    capital = gross_cost + fees + extra_costs
    profit = redemption - capital
    return CompleteSetFill(
        quantity=quantity,
        gross_cost=gross_cost,
        fees=fees,
        extra_costs=extra_costs,
        redemption=redemption,
        guaranteed_profit=profit,
        roi=profit / capital if capital > 0 else float("inf"),
        profitable=profit > 0,
    )


def max_profitable_quantity(
    yes_asks: Sequence[BookLevel],
    no_asks: Sequence[BookLevel],
    *,
    yes_fee_rate: float = 0.0,
    no_fee_rate: float = 0.0,
    extra_costs: float = 0.0,
    redemption_per_pair: float = 1.0,
) -> CompleteSetFill | None:
    """Search exact orderbook breakpoints for the largest profitable pair size.

    Candidate quantities are cumulative ask-depth breakpoints from either side,
    capped by total depth available on both sides.  This avoids treating a
    top-of-book quote as executable for more shares than are actually offered.
    """
    _validate_levels(yes_asks)
    _validate_levels(no_asks)
    if extra_costs < 0:
        raise ValueError("extra_costs cannot be negative")

    yes_total = sum(x.size for x in yes_asks)
    no_total = sum(x.size for x in no_asks)
    cap = min(yes_total, no_total)
    if cap <= 0:
        return None

    breakpoints = {cap}
    for levels in (yes_asks, no_asks):
        running = 0.0
        for level in sorted(levels, key=lambda x: x.price):
            running += level.size
            if 0 < running <= cap + 1e-12:
                breakpoints.add(min(running, cap))

    best: CompleteSetFill | None = None
    for quantity in sorted(breakpoints):
        fill = fee_aware_binary_complete_set(
            yes_asks,
            no_asks,
            quantity,
            yes_fee_rate=yes_fee_rate,
            no_fee_rate=no_fee_rate,
            extra_costs=extra_costs,
            redemption_per_pair=redemption_per_pair,
        )
        if fill.profitable and (best is None or fill.quantity > best.quantity):
            best = fill
    return best


def kalshi_market_buy_complete_set_cost(best_yes_bid: float, best_no_bid: float) -> float:
    """Implied pre-fee cost to market-buy both sides from Kalshi bid-only book.

    Kalshi documents that a YES bid at x is equivalent to a NO ask at 1-x.
    Thus YES ask = 1-best_no_bid and NO ask = 1-best_yes_bid.
    """
    if not (0.0 <= best_yes_bid <= 1.0 and 0.0 <= best_no_bid <= 1.0):
        raise ValueError("bids must be in [0,1]")
    return (1.0 - best_no_bid) + (1.0 - best_yes_bid)


def kalshi_crossed_book_required(best_yes_bid: float, best_no_bid: float) -> bool:
    """A sub-$1 market-buy complete set requires YES_bid + NO_bid > 1.

    Such a state is crossed/matchable rather than a structural subsidy; fees
    further tighten the condition.
    """
    return best_yes_bid + best_no_bid > 1.0
