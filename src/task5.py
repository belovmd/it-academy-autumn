"""
Написать программу которая находит ближайшую степень двойки к введенному числу.
10(8), 20(16), 1(1), 13(16)
"""

import math


def get_closest_pow2(num):
    if num <= 1:
        return 1
    res = 1
    min_diff = math.inf
    while True:
        res <<= 1
        if abs(num - res) < min_diff:
            min_diff = abs(res - num)
        else:
            return res >> 1


if __name__ == "__main__":
    print(get_closest_pow2(10))
    print(get_closest_pow2(20))
    print(get_closest_pow2(1))
    print(get_closest_pow2(13))
