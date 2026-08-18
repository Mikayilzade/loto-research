from __future__ import annotations

from dataclasses import dataclass
from datetime import date
from typing import Iterable


@dataclass(frozen=True)
class FxQuote:
    institution: str
    currency: str
    bid: float
    ask: float
    channel: str
    quote_date: date

    def __post_init__(self) -> None:
        if self.bid <= 0 or self.ask <= 0:
            raise ValueError("bid and ask must be positive")
        if self.bid > self.ask:
            raise ValueError("single-institution quote has bid above ask")


@dataclass(frozen=True)
class CrossResult:
    currency: str
    channel: str
    quote_date: date
    best_bid_institution: str
    best_bid: float
    lowest_ask_institution: str
    lowest_ask: float

    @property
    def gross_return(self) -> float:
        return self.best_bid / self.lowest_ask - 1.0

    @property
    def spread(self) -> float:
        return self.best_bid - self.lowest_ask

    @property
    def is_pre_fee_arbitrage(self) -> bool:
        return self.best_bid > self.lowest_ask


def screen_synchronized_quotes(quotes: Iterable[FxQuote]) -> list[CrossResult]:
    """Find best bid / lowest ask only within exactly synchronized buckets.

    Buckets are `(quote_date, channel, currency)`. Mixing dates or cash/cashless
    channels is forbidden because doing so creates false arbitrage signals.
    """
    grouped: dict[tuple[date, str, str], list[FxQuote]] = {}
    for quote in quotes:
        key = (quote.quote_date, quote.channel, quote.currency)
        grouped.setdefault(key, []).append(quote)

    results: list[CrossResult] = []
    for (quote_date, channel, currency), rows in sorted(grouped.items()):
        if len(rows) < 2:
            continue
        best_bid = max(rows, key=lambda q: q.bid)
        lowest_ask = min(rows, key=lambda q: q.ask)
        results.append(
            CrossResult(
                currency=currency,
                channel=channel,
                quote_date=quote_date,
                best_bid_institution=best_bid.institution,
                best_bid=best_bid.bid,
                lowest_ask_institution=lowest_ask.institution,
                lowest_ask=lowest_ask.ask,
            )
        )
    return results


def net_return_after_cost_rate(result: CrossResult, round_trip_cost_rate: float) -> float:
    if round_trip_cost_rate < 0:
        raise ValueError("round_trip_cost_rate cannot be negative")
    return result.best_bid / result.lowest_ask - 1.0 - round_trip_cost_rate
