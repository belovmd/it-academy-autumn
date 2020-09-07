"""
Вводится число найти его максимальный делитель,
являющийся степенью двойки. 10(2) 16(16), 12(4).
"""


def max_div_2(num):
    n = 0
    while not num % 2:
        n += 1
        num >>= 1
    return 1 << n


def main():
    num = 48
    print(max_div_2(num))
    pass


if __name__ == '__main__':
    main()
