from datetime import datetime, timedelta

from py_vollib.black_scholes.implied_volatility import implied_volatility
from py_vollib.black_scholes.greeks.analytical import (
    delta as d,
    gamma as g,
    rho as r,
    theta as t,
)

rate_of_interest = 0.1


def get_option_type(option_type):
    if option_type == "CE":
        option_type = "c"
    elif option_type == "PE":
        option_type = "p"

    return option_type


def time_to_expiry(expiry):
    expiry = datetime.strptime(expiry, "%Y-%m-%d")
    expiry.replace(hour=15, minute=30)
    time_to_expiry = (expiry - datetime.now()) / timedelta(days=365)

    return time_to_expiry


def iv(option_price, strike, expiry, option_type, underlying_price):
    tte = time_to_expiry(expiry)
    flag = get_option_type(option_type)

    return implied_volatility(
        option_price,
        underlying_price,
        strike,
        tte,
        rate_of_interest,
        flag,
    )


def delta(strike, expiry, option_type, underlying_price, implied_vol):
    tte = time_to_expiry(expiry)
    flag = get_option_type(option_type)

    return d(flag, underlying_price, strike, tte, rate_of_interest, implied_vol)


def rho(strike, expiry, option_type, underlying_price, implied_vol):
    tte = time_to_expiry(expiry)
    flag = get_option_type(option_type)

    return r(flag, underlying_price, strike, tte, rate_of_interest, implied_vol)


def gamma(strike, expiry, option_type, underlying_price, implied_vol):
    tte = time_to_expiry(expiry)
    flag = get_option_type(option_type)

    return g(flag, underlying_price, strike, tte, rate_of_interest, implied_vol)


def theta(strike, expiry, option_type, underlying_price, implied_vol):
    tte = time_to_expiry(expiry)
    flag = get_option_type(option_type)

    return t(flag, underlying_price, strike, tte, rate_of_interest, implied_vol)
