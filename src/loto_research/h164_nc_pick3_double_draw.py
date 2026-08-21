"""H164 North Carolina Pick 3 forced Double Draw deterministic cover.

This module only computes the mathematical identity. Execution, retailer-accounting,
tax, and promotion-state gates are documented in the research packet.
"""

from dataclasses import dataclass


@dataclass(frozen=True)
class CoverResult:
    outcomes: int
    wager_per_outcome: float
    drawings: int
    pair_prize: float
    retailer_commission_rate: float

    @property
    def face_spend(self) -> float:
        return self.outcomes * self.wager_per_outcome

    @property
    def guaranteed_prizes(self) -> float:
        return self.drawings * self.pair_prize

    @property
    def retailer_commission(self) -> float:
        return self.face_spend * self.retailer_commission_rate

    @property
    def conditional_total_value(self) -> float:
        return self.guaranteed_prizes + self.retailer_commission

    @property
    def conditional_profit(self) -> float:
        return self.conditional_total_value - self.face_spend

    @property
    def conditional_return_ratio(self) -> float:
        return self.conditional_total_value / self.face_spend


def nc_forced_double_draw_pair_cover() -> CoverResult:
    return CoverResult(
        outcomes=100,
        wager_per_outcome=0.50,
        drawings=2,
        pair_prize=25.0,
        retailer_commission_rate=0.07,
    )


if __name__ == "__main__":
    r = nc_forced_double_draw_pair_cover()
    print(f"face_spend={r.face_spend:.2f}")
    print(f"guaranteed_prizes={r.guaranteed_prizes:.2f}")
    print(f"retailer_commission={r.retailer_commission:.2f}")
    print(f"conditional_profit={r.conditional_profit:.2f}")
    print(f"conditional_return_ratio={r.conditional_return_ratio:.6f}")
