import numpy as np

def price_bond(face_value, coupon_rate, periods, yield_to_maturity, freq=2):
    """
    Calculates the price of a plain vanilla bond using Discounted Cash Flow (DCF).
    
    Parameters:
    - face_value (float): Face/par value of the bond (e.g., 1000)
    - coupon_rate (float): Annual coupon rate as a decimal (e.g., 5% => 0.05)
    - periods (int): Total number of coupon periods (e.g., 5 years * 2 = 10)
    - yield_to_maturity (float): Annual yield to maturity as decimal (e.g., 6% => 0.06)
    - freq (int): Coupon payment frequency per year (default = 2 for semiannual)

    Returns:
    - float: Present value (price) of the bond
    """
    coupon_payment = (coupon_rate * face_value) / freq
    ytm_per_period = yield_to_maturity / freq

    # Present value of coupon payments
    pv_coupons = sum([coupon_payment / (1 + ytm_per_period) ** t for t in range(1, periods + 1)])

    # Present value of face value
    pv_face = face_value / (1 + ytm_per_period) ** periods

    return pv_coupons + pv_face

# Example usage:
if __name__ == "__main__":
    face_value = 1000       # ₹1000 face value
    coupon_rate = 0.05      # 5% annual coupon
    yield_to_maturity = 0.06  # 6% annual YTM
    years = 5
    freq = 2                # Semiannual
    periods = years * freq  # Total periods = 5*2 = 10

    bond_price = price_bond(face_value, coupon_rate, periods, yield_to_maturity, freq)
    print(f"Bond Price: ₹{bond_price:.2f}")