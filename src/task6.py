"""
Вводится число найти его максимальный делитель, являющийся степенью двойки.
10(2) 16(16), 12(4).
"""


def get_max_div_pow2(num):
    res_pow = 0
    while not num >> res_pow & 1:
        res_pow += 1
    return 2 ** res_pow


if __name__ == "__main__":
    print(get_max_div_pow2(10))
    print(get_max_div_pow2(16))
    print(get_max_div_pow2(12))
