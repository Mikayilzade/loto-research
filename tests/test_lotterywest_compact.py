import unittest

from loto_research.lotterywest_compact import (
    cash3_minimal_partition_cover,
    super66_full_space_counts,
    super66_hypothetical_full_space_floor,
)


class LotterywestCompactTests(unittest.TestCase):
    def test_super66_counts(self):
        self.assertEqual(
            super66_full_space_counts(),
            {1: 1, 2: 18, 3: 180, 4: 1800, 5: 17901},
        )

    def test_super66_floor(self):
        cost, gross, ratio = super66_hypothetical_full_space_floor()
        self.assertEqual(cost, 1_000_000.0)
        self.assertAlmostEqual(gross, 543_480.6, places=6)
        self.assertAlmostEqual(ratio, 0.5434806, places=10)

    def test_cash3_partition_cover(self):
        result = cash3_minimal_partition_cover(0.5)
        self.assertEqual(result["wagers"], 220)
        self.assertAlmostEqual(result["cost"], 110.0)
        self.assertAlmostEqual(result["min_gross"], 40.0)
        self.assertAlmostEqual(result["min_return_ratio"], 40/110, places=12)
        self.assertAlmostEqual(result["expected_gross"], 52.9)
        self.assertAlmostEqual(result["expected_return_ratio"], 52.9/110, places=12)


if __name__ == "__main__":
    unittest.main()
