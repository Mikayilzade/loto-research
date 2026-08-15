from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class CappedCompetition:
    max_entries: int
    entry_price: float
    cash_prize: float
    external_entries: int = 0
    per_person_cap: int | None = None
    fixed_fees: float = 0.0

    def __post_init__(self) -> None:
        if self.max_entries <= 0:
            raise ValueError("max_entries must be positive")
        if self.entry_price < 0 or self.cash_prize < 0 or self.fixed_fees < 0:
            raise ValueError("prices/prizes/fees cannot be negative")
        if not 0 <= self.external_entries <= self.max_entries:
            raise ValueError("external_entries must be within entry pool")
        if self.per_person_cap is not None and self.per_person_cap < 0:
            raise ValueError("per_person_cap cannot be negative")

    @property
    def full_takeover_cost(self) -> float:
        return self.max_entries * self.entry_price + self.fixed_fees

    @property
    def cash_to_full_cost_ratio(self) -> float:
        cost = self.full_takeover_cost
        return self.cash_prize / cost if cost else float("inf")

    def exclusivity_possible(self) -> bool:
        """Necessary entry-ownership condition, ignoring race/free-entry channels."""
        if self.external_entries != 0:
            return False
        return self.per_person_cap is None or self.per_person_cap >= self.max_entries

    def positive_full_takeover_economics(self) -> bool:
        return self.cash_prize > self.full_takeover_cost

    def passes_basic_guarantee_filter(self) -> bool:
        """Necessary, not sufficient, filter for a strict buy-all guarantee.

        A True result still requires atomic acquisition/closure, no unresolved
        free-entry channel, guaranteed prize payment, eligibility and claim
        conditions, and cancellation/substitution risk analysis.
        """
        return self.exclusivity_possible() and self.positive_full_takeover_economics()
