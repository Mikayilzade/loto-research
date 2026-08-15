import unittest
from random import Random
from statistics import mean

from loto_research.crowd_choice import (
    CrowdBiasParameters,
    anti_crowd_candidates,
    estimate_competitor_hit_probability,
    line_crowd_score,
    match_count,
    sample_crowd_line,
    sample_draw_conditioned_on_ticket_matches,
)


class CrowdChoiceTests(unittest.TestCase):
    def test_birthday_and_lucky_bias_raise_crowd_score(self):
        params = CrowdBiasParameters(
            birthday_weight=0.5,
            lucky_weight=1.0,
        )
        popular = (1, 7, 12, 18, 24, 30)
        high = (34, 39, 44, 49, 54, 59)
        self.assertGreater(
            line_crowd_score(popular, 59, 6, params),
            line_crowd_score(high, 59, 6, params),
        )

    def test_conditioned_draw_has_requested_match_count(self):
        target = (1, 2, 3, 4, 5, 6)
        rng = Random(123)
        for matches in range(7):
            draw = sample_draw_conditioned_on_ticket_matches(
                target, 59, 6, matches, rng
            )
            self.assertEqual(match_count(target, draw), matches)

    def test_strong_birthday_bias_lowers_sampled_mean_number(self):
        params = CrowdBiasParameters(
            birthday_weight=1.0,
            candidate_batch=32,
        )
        rng = Random(123)
        average_numbers = [
            sum(sample_crowd_line(59, 6, params, rng)) / 6
            for _ in range(2_000)
        ]
        self.assertLess(mean(average_numbers), 27.0)

    def test_anti_crowd_candidates_are_ranked(self):
        params = CrowdBiasParameters(
            birthday_weight=0.6,
            lucky_weight=0.8,
            center_weight=0.3,
            even_spacing_weight=0.2,
        )
        candidates = anti_crowd_candidates(
            59, 6, params, candidate_count=200, top_n=10, seed=5
        )
        scores = [score for score, _ in candidates]
        self.assertEqual(scores, sorted(scores))

    def test_intensity_estimator_returns_valid_probability_and_se(self):
        params = CrowdBiasParameters(
            birthday_weight=0.5,
            candidate_batch=8,
        )
        estimate = estimate_competitor_hit_probability(
            (35, 39, 44, 49, 54, 59),
            59,
            6,
            3,
            3,
            params,
            simulations=1_000,
            seed=7,
        )
        self.assertGreaterEqual(estimate.probability, 0.0)
        self.assertLessEqual(estimate.probability, 1.0)
        self.assertGreaterEqual(estimate.standard_error, 0.0)


if __name__ == "__main__":
    unittest.main()
