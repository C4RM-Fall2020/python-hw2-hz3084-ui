import numpy as np

def getBondPrice(y, face, couponRate, m, ppy=1):

    n = m * ppy

    t = np.arange(1, n + 1)

    coupon = face * couponRate / ppy

    cashflows = np.full(n, coupon)
    cashflows[-1] = cashflows[-1] + face

    pv = cashflows / (1 + y / ppy) ** t

    bondPrice = np.sum(pv)

    return bondPrice
