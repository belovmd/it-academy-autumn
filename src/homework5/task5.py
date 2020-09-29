"""
Написать программу которая находит ближайшую
степень двойки к введенному числу. 10(8), 20(16), 1(1)
"""


def get_nearest(number):
    test_number = number
    count_of_bits = 0
    while test_number > 0:
        test_number = test_number >> 1
        count_of_bits += 1
    if not number & 1 or number == 1:
        count_of_bits -= 1
    print(2**count_of_bits)


get_nearest(10)
get_nearest(20)
get_nearest(1)
get_nearest(13)
