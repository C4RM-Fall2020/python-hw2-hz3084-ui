import numpy as np

def getBondPrice(y, face, couponRate, m, ppy=1):

    coupon = face * couponRate / ppy
    bondPrice = 0

    for t in range(1, m * ppy + 1):

        cf = coupon

        if t == m * ppy:
            cf += face

        pv = cf / (1 + y / ppy) ** t

        bondPrice += pv

    return bondPrice
