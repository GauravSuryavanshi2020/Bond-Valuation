import unittest
from bond_pricing import price_bond  # assuming the pricing function is saved in bond_pricing.py

class TestBondPricing(unittest.TestCase):

    def test_regular_case(self):
        price = price_bond(face_value=1000, coupon_rate=0.05, periods=10, yield_to_maturity=0.06, freq=2)
        self.assertAlmostEqual(price, 957.35, places=2)

    def test_zero_coupon_bond(self):
        price = price_bond(face_value=1000, coupon_rate=0.0, periods=10, yield_to_maturity=0.05, freq=2)
        expected = 1000 / (1 + 0.05 / 2) ** 10
        self.assertAlmostEqual(price, expected, places=2)

    def test_at_par(self):
        # When coupon rate equals YTM, bond should be priced at par
        price = price_bond(face_value=1000, coupon_rate=0.06, periods=10, yield_to_maturity=0.06, freq=2)
        self.assertAlmostEqual(price, 1000.00, places=2)

    def test_short_term_bond(self):
        price = price_bond(face_value=1000, coupon_rate=0.04, periods=2, yield_to_maturity=0.05, freq=2)
        self.assertTrue(price > 980 and price < 1000)

    def test_invalid_inputs(self):
        with self.assertRaises(ZeroDivisionError):
            price_bond(face_value=1000, coupon_rate=0.05, periods=10, yield_to_maturity=0.0, freq=0)

if __name__ == '__main__':
    unittest.main()
