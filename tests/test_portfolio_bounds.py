import unittest

from loto_research.portfolio_bounds import (
    all_ticket_types_nonpositive_ev,
    portfolio_expected_profit,
    strict_guarantee_impossible_under_linearity,
)


class PortfolioBoundsTests(unittest.TestCase):
    def test_negative_ev_ticket_mixture_stays_negative(self):
        result = portfolio_expected_profit(
            quantities=[10, 25, 3],
            ticket_expected_payouts=[0.535555131, 0.598555794, 0.78],
            ticket_costs=[1.0, 1.0, 1.0],
        )
        self.assertLess(result, 0.0)

    def test_all_nonpositive_ev_detected(self):
        self.assertTrue(
            all_ticket_types_nonpositive_ev(
                [0.535555131, 0.598555794, 0.78],
                [1.0, 1.0, 1.0],
            )
        )

    def test_positive_ev_type_breaks_impossibility_screen(self):
        self.assertFalse(
            strict_guarantee_impossible_under_linearity(
                [0.8, 1.1],
                [1.0, 1.0],
            )
        )

    def test_zero_ev_still_cannot_imply_strict_positive_guarantee(self):
        self.assertTrue(
            strict_guarantee_impossible_under_linearity(
                [1.0],
                [1.0],
            )
        )


if __name__ == "__main__":
    unittest.main()
