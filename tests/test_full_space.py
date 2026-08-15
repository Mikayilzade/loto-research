import unittest

from loto_research.full_space import (
    fixed_match_full_coverage,
    full_space_match_counts,
    ordered_last_hit_full_coverage,
)


class FullSpaceCoverageTests(unittest.TestCase):
    def test_besde5_match_counts_partition_space(self):
        counts = full_space_match_counts(36, 5)
        self.assertEqual(sum(counts.values()), 376_992)
        self.assertEqual(counts[5], 1)
        self.assertEqual(counts[4], 155)
        self.assertEqual(counts[3], 4_650)
        self.assertEqual(counts[2], 44_950)

    def test_besde5_full_space_is_guaranteed_loss_even_before_tax_sharing(self):
        variants, cost, gross, roi = fixed_match_full_coverage(
            36,
            5,
            1.0,
            {5: 50_000, 4: 100, 3: 10, 2: 2},
        )
        self.assertEqual(variants, 376_992)
        self.assertEqual(cost, 376_992.0)
        self.assertEqual(gross, 201_900.0)
        self.assertAlmostEqual(roi, 0.5355551311433664, places=15)

    def test_onloto_type1_full_space(self):
        multipliers = {1:10,2:7,3:5,4:5,5:4,6:3,7:2,8:2,9:1}
        variants, cost, gross, roi = ordered_last_hit_full_coverage(
            50, 1, 1.0, multipliers
        )
        self.assertEqual(variants, 50)
        self.assertEqual(cost, 50.0)
        self.assertEqual(gross, 39.0)
        self.assertAlmostEqual(roi, 0.78, places=12)

    def test_onloto_type2_full_space(self):
        multipliers = {
            2:20,3:17,4:15,5:14,6:13,7:12,8:11,9:10,10:10,
            11:7,12:6,13:5,14:5,15:4,16:3,17:2,18:1,
        }
        variants, cost, gross, roi = ordered_last_hit_full_coverage(
            50, 2, 1.0, multipliers
        )
        self.assertEqual(variants, 1_225)
        self.assertEqual(gross, 950.0)
        self.assertAlmostEqual(roi, 950/1225, places=12)

    def test_onloto_type10_full_space(self):
        multipliers = {
            10:10000,11:5000,12:4000,13:3000,14:2500,15:2000,
            16:1500,17:1200,18:1000,19:750,20:600,21:500,22:400,
            23:350,24:300,25:250,26:200,27:150,28:120,29:100,
            30:70,31:60,32:40,33:25,34:20,35:10,36:5,
        }
        variants, cost, gross, roi = ordered_last_hit_full_coverage(
            50, 10, 1.0, multipliers
        )
        self.assertEqual(variants, 10_272_278_170)
        self.assertEqual(gross, 7_938_231_510.0)
        self.assertAlmostEqual(roi, 0.7727819845439408, places=12)


if __name__ == "__main__":
    unittest.main()
