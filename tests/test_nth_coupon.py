import pytest

from loto_research.nth_coupon import (
    NthCouponCase,
    player_block_guarantees_coupon,
    strict_coupon_floor_global_nth,
)


def test_lotto_love_conditional_inversion():
    case = NthCouponCase(qualifying_cost=104, coupon_value=208)
    assert case.conditional_coupon_net == 104
    assert case.conditional_coupon_gross == 2.0


def test_statewide_interleaving_has_zero_strict_coupon_floor():
    assert strict_coupon_floor_global_nth(exclusive_global_positions=False) == 0


def test_n_personal_purchases_do_not_force_statewide_nth_coupon():
    assert not player_block_guarantees_coupon(
        player_purchases=100,
        n=100,
        statewide_counter=True,
        exclusive_global_positions=False,
    )


def test_exclusive_case_requires_promotion_specific_rule():
    with pytest.raises(ValueError):
        strict_coupon_floor_global_nth(exclusive_global_positions=True)
