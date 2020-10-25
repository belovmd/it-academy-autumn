"""
Написать программу которая находит ближайшую степень двойки к
введенному числу. 10(8), 20(16), 1(1), 13(16)
"""


def closest_power_of_two(num):
    prev = 0
    next_ = 1
    while next_ < num:
        prev = next_
        next_ <<= 1

    if abs(next_ - num) < abs(prev - num):
        return next_
    return prev


print(closest_power_of_two(13))
