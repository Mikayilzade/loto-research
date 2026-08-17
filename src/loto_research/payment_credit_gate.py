from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class PaymentCreditCase:
    committed_principal: float
    guaranteed_principal_recovery: float
    guaranteed_withdrawable_cash_reward: float
    worst_case_costs: float

    def guaranteed_net_floor(self) -> float:
        values = (
            self.committed_principal,
            self.guaranteed_principal_recovery,
            self.guaranteed_withdrawable_cash_reward,
            self.worst_case_costs,
        )
        if any(value < 0 for value in values):
            raise ValueError("all monetary inputs must be non-negative")
        return (
            self.guaranteed_principal_recovery
            + self.guaranteed_withdrawable_cash_reward
            - self.committed_principal
            - self.worst_case_costs
        )

    def is_strict_guarantee(self) -> bool:
        return self.guaranteed_net_floor() > 0.0


def reward_floor(*, cash_withdrawable: bool, deterministic_vesting: bool, nominal_reward: float) -> float:
    """Convert a headline reward into the amount usable in a strict proof.

    Non-cash rewards and rewards with a valid zero/discretion branch must be
    assigned a zero guaranteed cash floor regardless of headline face value.
    """
    if nominal_reward < 0:
        raise ValueError("nominal_reward cannot be negative")
    if not cash_withdrawable or not deterministic_vesting:
        return 0.0
    return nominal_reward
