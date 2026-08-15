import unittest

from loto_research.cash_pop import cover_all_floor, prize_table_ev, random_overlay_guarantee_value


class CashPopTests(unittest.TestCase):
    def test_cover_all_floor_is_one_third_for_all_wagers(self):
        for wager in (1, 2, 5, 10):
            cost, payout, ratio = cover_all_floor(15, wager, 5 * wager)
            self.assertEqual(cost, 15 * wager)
            self.assertEqual(payout, 5 * wager)
            self.assertAlmostEqual(ratio, 1 / 3, places=12)

    def test_georgia_one_dollar_ev(self):
        rows = [(5,32),(7,75),(10,105),(15,165),(20,225),(25,825),(50,2250),(100,4500),(250,8250)]
        self.assertAlmostEqual(prize_table_ev(rows), 0.6296699134199134, places=12)

    def test_random_instant_bonus_has_zero_guaranteed_value(self):
        self.assertEqual(random_overlay_guarantee_value(True), 0.0)


if __name__ == "__main__":
    unittest.main()
