import unittest

from loto_research.fireball_bounds import (
    PrizeOdds,
    additive_portfolio_guarantee_possible,
    combined_ev_ratio_upper_bound,
    fireball_ev_upper_bound,
)


class FireballBoundsTests(unittest.TestCase):
    def test_pick3_exact_fireball_is_negative_ev(self):
        ev = fireball_ev_upper_bound([PrizeOdds(200, 357)])
        self.assertAlmostEqual(ev, 200 / 357, places=12)
        self.assertLess(ev, 1.0)

    def test_pick3_5050_upper_bound_remains_below_cost(self):
        # Deliberately double-count possible overlap between published Any and
        # Exact rows.  This is favorable to the player and therefore safe as a
        # rejection bound.
        ev = fireball_ev_upper_bound(
            [PrizeOdds(33, 122), PrizeOdds(133, 345)]
        )
        self.assertLess(ev, 1.0)
        self.assertAlmostEqual(ev, 0.6559990496555002, places=12)

    def test_pick4_combo_normalizes_incremental_cost(self):
        ratio = combined_ev_ratio_upper_bound(
            0.5, 24.0, [PrizeOdds(1500, 123)]
        )
        self.assertLess(ratio, 1.0)
        self.assertAlmostEqual(ratio, 0.5040650406504065, places=12)

    def test_pick5_5050_upper_bound_still_negative(self):
        ratio = combined_ev_ratio_upper_bound(
            0.5,
            1.0,
            [PrizeOdds(7200, 21277), PrizeOdds(1200, 4525)],
        )
        self.assertLess(ratio, 1.0)
        self.assertAlmostEqual(ratio, 0.551793470343953, places=12)

    def test_linear_guarantee_gate(self):
        self.assertFalse(additive_portfolio_guarantee_possible(0.578))
        self.assertTrue(additive_portfolio_guarantee_possible(1.001))


if __name__ == "__main__":
    unittest.main()
