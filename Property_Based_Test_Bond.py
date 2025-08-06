from hypothesis import given, strategies as st
import math

# Reusing bond valuation logic
def price_bond(face_value, coupon_rate, periods, yield_to_maturity, freq=2):
    coupon_payment = (coupon_rate * face_value) / freq
    ytm_per_period = yield_to_maturity / freq
    pv_coupons = sum([coupon_payment / (1 + ytm_per_period) ** t for t in range(1, periods + 1)])
    pv_face = face_value / (1 + ytm_per_period) ** periods
    return pv_coupons + pv_face

@given(
    face_value=st.floats(min_value=100, max_value=10000, allow_nan=False, allow_infinity=False),
    coupon_rate=st.floats(min_value=0.0, max_value=0.15, allow_nan=False, allow_infinity=False),
    yield_to_maturity=st.floats(min_value=0.0001, max_value=0.20, allow_nan=False, allow_infinity=False),
    years=st.integers(min_value=1, max_value=30),
    freq=st.sampled_from([1, 2, 4])  # Annual, semiannual, quarterly
)
def test_price_bond_properties(face_value, coupon_rate, yield_to_maturity, years, freq):
    periods = years * freq
    price = price_bond(face_value, coupon_rate, periods, yield_to_maturity, freq)

    # Property 1: Price must always be positive
    assert price > 0, "Bond price should always be positive"

    # Property 2: Zero-coupon bond should always be less than face value
    if coupon_rate == 0:
        assert price < face_value, "Zero-coupon bond should price below par"

    # Property 3: If coupon == YTM, bond is near par
    if abs(coupon_rate - yield_to_maturity) < 1e-5:
        assert abs(price - face_value) < 50, "Bond near par when coupon ≈ YTM"

# Run manually
if __name__ == "__main__":
    test_price_bond_properties()