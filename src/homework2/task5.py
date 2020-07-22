"""Выведите n-ое число Фибоначчи, используя только временные переменные,
    циклические операторы и условные операторы. n - вводится.
"""


def fibonacci(n):
    """Поиск числа фибоначчи.

    :param n: Номер числа Фибоначчи.
    :return: Число. n-ое число Фибоначчи
    """
    i = 0
    previous = 1
    current = 1
    while i < n - 2:
        i = i + 1
        next = previous + current
        previous = current
        current = next
    # write your code here
    return 'n-ое число ряда Фибоначчи - ' + str(current)  # write return value here


if __name__ == '__main__':
    # здесь можно сделать ввод из консоли и проверить работу функции
    n = 8
    print(fibonacci(n))
