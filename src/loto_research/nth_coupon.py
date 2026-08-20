"""Helpers for deterministic screens of lottery 'every Nth' coupon promotions."""

from dataclasses import dataclass


@dataclass(frozen=True)
class NthCouponCase:
    qualifying_cost: float
    coupon_value: float

    @property
    def conditional_coupon_net(self) -> float:
        """Net from coupon alone if the player's purchase is known to receive it."""
        return self.coupon_value - self.qualifying_cost

    @property
    def conditional_coupon_gross(self) -> float:
        """Coupon-only gross return multiple conditional on receiving the coupon."""
        return self.coupon_value / self.qualifying_cost


def strict_coupon_floor_global_nth(*, exclusive_global_positions: bool) -> float:
    """Strict number of coupons guaranteed by a generic statewide Nth mechanism.

    Without exclusive control of the statewide qualifying positions, arbitrary
    external interleaving can occupy every coupon-bearing position, so the
    player's strict coupon floor is zero.

    The exclusive case is intentionally not assigned a numeric floor here:
    a floor then depends on the published N/phase/block rule and batch size.
    """
    if not exclusive_global_positions:
        return 0.0
    raise ValueError("Need promotion-specific N/phase/block rule for exclusive case")


def player_block_guarantees_coupon(*, player_purchases: int, n: int,
                                   statewide_counter: bool,
                                   exclusive_global_positions: bool) -> bool:
    """Whether N personal purchases prove receipt of at least one Nth coupon."""
    if player_purchases < n:
        return False
    if statewide_counter and not exclusive_global_positions:
        return False
    return True
