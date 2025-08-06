import logging
import random

# Configure logging
logging.basicConfig(
    filename="bond_fuzzing.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def price_bond(face_value, coupon_rate, periods, yield_to_maturity, freq=2):
    try:
        coupon_payment = (coupon_rate * face_value) / freq
        ytm_per_period = yield_to_maturity / freq
        pv_coupons = sum([coupon_payment / (1 + ytm_per_period) ** t for t in range(1, periods + 1)])
        pv_face = face_value / (1 + ytm_per_period) ** periods
        return pv_coupons + pv_face
    except Exception as e:
        return f"Error: {e}"

def fuzz_test_price_bond(iterations=200):
    failures = []
    for i in range(iterations):
        face_value = random.uniform(100, 10000)
        coupon_rate = random.uniform(0.0, 0.20)
        ytm = random.uniform(0.0001, 0.20)
        freq = random.choice([1, 2, 4, 12])
        periods = random.randint(1, 60)

        result = price_bond(face_value, coupon_rate, periods, ytm, freq)
        if isinstance(result, str) and result.startswith("Error"):
            logging.warning(f"⚠️ Failed Input: {(face_value, coupon_rate, periods, ytm, freq)} | {result}")
            failures.append((face_value, coupon_rate, periods, ytm, freq, result))
        else:
            logging.info(f"✅ Success: {(face_value, coupon_rate, periods, ytm, freq)} -> {result}")
    return failures

# Run if main
if __name__ == "__main__":
    failures = fuzz_test_price_bond()
    logging.info(f"Total failures: {len(failures)}")