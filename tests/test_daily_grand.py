import unittest

from loto_research.daily_grand import (
    daily_grand_full_space_counts,
    daily_grand_full_space_screen,
)


class DailyGrandCoverageTests(unittest.TestCase):
    def test_main_match_counts_partition_5of49_space(self):
        counts = daily_grand_full_space_counts()
        self.assertEqual(sum(counts.values()), 1_906_884)
        self.assertEqual(counts[5], 1)
        self.assertEqual(counts[4], 220)
        self.assertEqual(counts[3], 9_460)
        self.assertEqual(counts[2], 132_440)
        self.assertEqual(counts[1], 678_755)
        self.assertEqual(counts[0], 1_086_008)

    def test_full_space_face_value_bound_is_large_loss(self):
        result = daily_grand_full_space_screen(value_free_play_at_face=True)
        self.assertEqual(result["variants"], 13_348_188.0)
        self.assertEqual(result["cost"], 40_044_564.0)
        self.assertEqual(result["gross"], 17_758_644.0)
        self.assertAlmostEqual(result["roi"], 0.4434720278138126, places=12)
        self.assertLess(result["net"], 0)

    def test_strict_cash_floor_is_even_lower(self):
        result = daily_grand_full_space_screen(value_free_play_at_face=False)
        self.assertEqual(result["gross"], 14_500_620.0)
        self.assertAlmostEqual(result["roi"], 0.3621120709417638, places=12)

    def test_even_impossible_overgenerous_second_prize_bound_loses(self):
        result = daily_grand_full_space_screen(
            value_free_play_at_face=True,
            respect_top_pool_caps=False,
        )
        self.assertEqual(result["gross"], 20_258_644.0)
        self.assertAlmostEqual(result["roi"], 0.5059024740536568, places=12)
        self.assertLess(result["net"], 0)


if __name__ == "__main__":
    unittest.main()
