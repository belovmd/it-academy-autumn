"""Выведите n-ое число Фибоначчи, используя только временные переменные,
    циклические операторы и условные операторы. n - вводится.
"""


def fibonacci(n):
    """Поиск числа фибоначчи.

    :param n: Номер числа Фибоначчи.
    :return: Число. n-ое число Фибоначчи
    """

    # write your code here
    first = 1
    next = 1
    num = 2
    while num < n:
        num += 1
        first, next = next, first + next
    return next  # write return value here


if __name__ == '__main__':
    # здесь можно сделать ввод из консоли и проверить работу функции
    n = 5
    print(fibonacci(n))
