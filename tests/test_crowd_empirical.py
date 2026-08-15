import unittest

from loto_research.crowd_empirical import (
    anti_crowd_choice_alone_can_guarantee_profit,
    dutch_lotto_6of45_anchor,
    shrink_anchor_toward_uniform,
)


class CrowdEmpiricalTests(unittest.TestCase):
    def test_published_number_order(self):
        model = dutch_lotto_6of45_anchor()
        self.assertGreater(model.number_multipliers[11], 1.0)
        self.assertGreater(model.number_multipliers[7], 1.0)
        self.assertLess(model.number_multipliers[37], 1.0)
        self.assertLess(model.number_multipliers[38], 1.0)

    def test_known_low_vs_high_anchor_ratio(self):
        model = dutch_lotto_6of45_anchor()
        low_crowd = (1, 2, 3, 4, 37, 38)
        high_crowd = (1, 2, 3, 4, 7, 11)
        ratio = model.relative_weight(low_crowd, high_crowd)
        self.assertAlmostEqual(ratio, 0.402345, places=5)

    def test_pattern_class_anchor_is_100x(self):
        model = dutch_lotto_6of45_anchor()
        self.assertAlmostEqual(model.pattern_class_multiplier, 100.0, places=12)

    def test_shrink_to_uniform(self):
        model = shrink_anchor_toward_uniform(dutch_lotto_6of45_anchor(), 0.0)
        self.assertTrue(all(abs(x - 1.0) < 1e-12 for x in model.number_multipliers.values()))
        self.assertAlmostEqual(model.pattern_class_multiplier, 1.0, places=12)

    def test_choice_only_is_not_terminal_guarantee_with_losing_outcomes(self):
        self.assertFalse(
            anti_crowd_choice_alone_can_guarantee_profit(
                ticket_cost=2.0, zero_return_outcome_exists=True
            )
        )


if __name__ == "__main__":
    unittest.main()
