"""
Вводится число найти его максимальный делитель,
являющийся степенью двойки. 10(2) 16(16), 12(4)
"""


def get_max_2_div(number):
    if number & 1:
        return 1
    count_of_bits = 0
    while not number & 1:
        number = number >> 1
        count_of_bits += 1
    return 2**count_of_bits


print(get_max_2_div(1))
print(get_max_2_div(10))
print(get_max_2_div(16))
print(get_max_2_div(12))
