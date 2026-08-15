import unittest

from loto_research.nebraska_coverage import (
    myday_full_space_gross_by_winning_date,
    pick5_full_space_lower_tier_cash,
    twobytwo_full_space_cash,
    twobytwo_seven_draw_package,
    valid_myday_dates,
)


class NebraskaCoverageTests(unittest.TestCase):
    def test_2by2_full_space(self):
        cost, gross = twobytwo_full_space_cash()
        self.assertEqual(cost, 105_625)
        self.assertEqual(gross, 40_168)
        self.assertLess(gross, cost)

    def test_2by2_tuesday_package(self):
        cost, gross, roi = twobytwo_seven_draw_package()
        self.assertEqual(cost, 739_375)
        self.assertEqual(gross, 321_344)
        self.assertAlmostEqual(roi, 0.43461572273879967, places=12)

    def test_myday_space_and_worst_best(self):
        self.assertEqual(len(valid_myday_dates()), 36_525)
        rows = myday_full_space_gross_by_winning_date()
        grosses = [gross for _, gross in rows]
        self.assertEqual(min(grosses), 17_580)
        self.assertEqual(max(grosses), 21_357)
        self.assertLess(max(grosses), 36_525)

    def test_pick5_hurdle(self):
        space, lower_cash, hurdle = pick5_full_space_lower_tier_cash()
        self.assertEqual(space, 658_008)
        self.assertEqual(lower_cash, 141_050)
        self.assertEqual(hurdle, 516_958)


if __name__ == "__main__":
    unittest.main()
