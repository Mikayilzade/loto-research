import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from loto_research.four_plus_four import (  # noqa: E402
    combined_5_6_fit_error,
    fixed_tail_expected_payout,
    infer_pool_unit,
    infer_variants_from_unit,
    stable_pool_fit_error,
)


class FourPlusFourEmpiricalTests(unittest.TestCase):
    def test_draw_795_stable_pool_ratios(self):
        totals = {
            3: 4487.34,
            4: 2039.73,
            5: 408.00,
            6: 408.00,
            7: 3672.48,
            8: 5712.12,
            9: 2857.92,
        }
        unit = infer_pool_unit(totals)
        self.assertAlmostEqual(unit, 408.00857142857143, places=10)
        self.assertLess(stable_pool_fit_error(totals, unit), 0.005)
        self.assertLess(abs(combined_5_6_fit_error(totals, unit)), 0.02)

    def test_draw_776_pair_5_6_conserves_combined_pool(self):
        totals = {
            3: 4569.95,
            4: 2077.25,
            5: 635.57,
            6: 195.54,
            7: 3740.16,
            8: 5819.40,
            9: 2910.88,
        }
        unit = infer_pool_unit(totals)
        self.assertAlmostEqual(unit, 415.5733333333333, places=10)
        self.assertLess(stable_pool_fit_error(totals, unit), 0.01)
        self.assertLess(abs(combined_5_6_fit_error(totals, unit)), 0.05)

    def test_draw_790_out_of_sample_confirms_pool_engine(self):
        # Draw 790 was added only after the 11/5/9/14/7 + combined-2U pattern
        # had been inferred from other draws. It therefore acts as a small
        # out-of-sample check rather than another fitting observation.
        totals = {
            3: 4593.40,
            4: 2087.91,
            5: 592.41,
            6: 243.04,
            7: 3758.96,
            8: 5847.84,
            9: 2923.20,
        }
        unit = infer_pool_unit(totals)
        self.assertAlmostEqual(unit, 417.6, places=10)
        self.assertLess(stable_pool_fit_error(totals, unit), 0.11)
        self.assertLess(abs(combined_5_6_fit_error(totals, unit)), 0.30)

    def test_fixed_tail_expected_payout(self):
        self.assertAlmostEqual(
            fixed_tail_expected_payout(),
            0.6821497378485368,
            places=14,
        )

    def test_working_unit_scaling(self):
        self.assertAlmostEqual(
            infer_variants_from_unit(408.0),
            40_800.0,
            places=12,
        )


if __name__ == "__main__":
    unittest.main()
