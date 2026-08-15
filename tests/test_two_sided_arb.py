import unittest

from loto_research.two_sided_arb import (
    back_lay_equal_profit,
    complete_set_token_arb,
    dutching_complete_set,
)


class TwoSidedArbTests(unittest.TestCase):
    def test_bookmaker_complete_set(self):
        result = dutching_complete_set([2.20, 1.98], target_return=1.0)
        self.assertTrue(result.profitable)
        self.assertAlmostEqual(result.capital, 0.9595959595959596, places=12)
        self.assertAlmostEqual(result.roi, 0.04210526315789487, places=12)

    def test_smarkets_published_style_example(self):
        lay, result = back_lay_equal_profit(2.20, 200.0, 1.98, 0.02)
        self.assertAlmostEqual(lay, 224.48979591836735, places=10)
        self.assertAlmostEqual(result.guaranteed_profit, 20.0, places=10)
        self.assertTrue(result.profitable)

    def test_complete_set_at_one_has_no_profit(self):
        result = complete_set_token_arb(0.60, 0.40)
        self.assertFalse(result.profitable)
        self.assertAlmostEqual(result.guaranteed_profit, 0.0, places=12)

    def test_complete_set_below_one_is_conditional_arb(self):
        result = complete_set_token_arb(0.48, 0.49, fees_and_gas=0.005)
        self.assertTrue(result.profitable)
        self.assertAlmostEqual(result.guaranteed_profit, 0.025, places=12)


if __name__ == "__main__":
    unittest.main()
