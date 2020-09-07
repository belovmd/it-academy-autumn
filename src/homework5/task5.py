"""
Написать программу которая находит ближайшую степень двойки
к введенному числу.
10(8), 20(16), 1(1), 13(16)
"""


def near_num(num):
    step_num = 1
    ans = 0
    while step_num < num << 1:
        current = abs(num - step_num)
        if abs(num - ans) > current:
            ans = step_num
        step_num <<= 1
    return ans


def main():
    num = 12
    print(near_num(num))


if __name__ == '__main__':
    main()
