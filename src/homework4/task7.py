"""
Даны два натуральных числа.
Вычислите их наибольший общий делитель при помощи алгоритма Евклида
(мы не знаем функции и рекурсию).
"""


def gcd(num1, num2):
    while num2:
        num1, num2 = num2, num1 % num2
    return num1


if __name__ == '__main__':
    num1 = 18
    num2 = 30
    print(gcd(num1, num2))
