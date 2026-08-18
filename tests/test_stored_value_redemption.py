import unittest

from loto_research.stored_value_redemption import (
    max_safe_acquisition_cost,
    m10_qr_cashout_fee,
    redemption_profit,
)


class StoredValueRedemptionTests(unittest.TestCase):
    def test_face_redemption_profit(self):
        self.assertEqual(redemption_profit(100, 95), 5)

    def test_qr_cashout_minimum_fee(self):
        self.assertEqual(m10_qr_cashout_fee(100), 1)
        self.assertEqual(m10_qr_cashout_fee(500), 2.5)

    def test_safe_price_with_cashout(self):
        self.assertEqual(max_safe_acquisition_cost(100, m10_qr_cashout_fee(100)), 99)
        self.assertEqual(max_safe_acquisition_cost(500, m10_qr_cashout_fee(500)), 497.5)

    def test_negative_inputs_rejected(self):
        with self.assertRaises(ValueError):
            redemption_profit(-1, 0)


if __name__ == "__main__":
    unittest.main()
