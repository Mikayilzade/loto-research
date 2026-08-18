from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class RedemptionScreen:
    face_value: float
    acquisition_price: float
    execution_cost: float
    redemption_threshold: float
    threshold_is_strict: bool = True

    @property
    def threshold_eligible(self) -> bool:
        if self.threshold_is_strict:
            return self.face_value < self.redemption_threshold
        return self.face_value <= self.redemption_threshold

    @property
    def guaranteed_cash_if_valid_and_redeemable(self) -> float:
        return self.face_value if self.threshold_eligible else 0.0

    @property
    def net_floor_if_valid_and_redeemable(self) -> float:
        return (
            self.guaranteed_cash_if_valid_and_redeemable
            - self.acquisition_price
            - self.execution_cost
        )

    @property
    def max_acquisition_price_for_positive_floor(self) -> float:
        if not self.threshold_eligible:
            return 0.0
        return self.face_value - self.execution_cost


def required_discount_rate(face_value: float, execution_cost: float = 0.0) -> float:
    """Minimum face-value discount needed for a strictly positive cash floor.

    Any epsilon above this rate is required because terminal SUCCESS requires
    strictly positive, not merely break-even, profit.
    """
    if face_value <= 0:
        raise ValueError("face_value must be positive")
    if execution_cost < 0:
        raise ValueError("execution_cost cannot be negative")
    return execution_cost / face_value
