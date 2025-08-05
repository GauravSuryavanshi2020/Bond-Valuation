#include <iostream>
#include <cmath>
using namespace std;

/**
 * Function to calculate the price of a bond using Discounted Cash Flow (DCF)
 *
 * @param face_value - Face or par value of the bond
 * @param coupon_rate - Annual coupon rate (e.g., 0.05 for 5%)
 * @param periods - Total number of coupon periods (e.g., 10 for 5 years semiannual)
 * @param ytm - Annual yield to maturity (e.g., 0.06 for 6%)
 * @param freq - Coupon frequency per year (default = 2 for semiannual)
 * @return double - Present value (price) of the bond
 */
double priceBond(double face_value, double coupon_rate, int periods, double ytm, int freq = 2) {
    double coupon_payment = (coupon_rate * face_value) / freq;
    double ytm_per_period = ytm / freq;

    double pv_coupons = 0.0;
    for (int t = 1; t <= periods; ++t) {
        pv_coupons += coupon_payment / pow(1 + ytm_per_period, t);
    }

    double pv_face = face_value / pow(1 + ytm_per_period, periods);

    return pv_coupons + pv_face;
}

int main() {
    double face_value = 1000;
    double coupon_rate = 0.05;
    double ytm = 0.06;
    int years = 5;
    int freq = 2;
    int periods = years * freq;

    double price = priceBond(face_value, coupon_rate, periods, ytm, freq);
    cout << "Bond Price: ₹" << price << endl;

    return 0;
}