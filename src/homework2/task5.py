"""Выведите n-ое число Фибоначчи, используя только временные переменные,
    циклические операторы и условные операторы. n - вводится.
"""


def fibonacci(n):
    """Поиск числа фибоначчи.

    :param n: Номер числа Фибоначчи.
    :return: Число. n-ое число Фибоначчи
    """

    # write your code here
    a, b = 0, 1
    fib = []
    for nums in range(n):
        dig = a + b
        fib.append(dig)
        a, b = b, (a + b)
    return 'fib'  # write return value here


if __name__ == '__main__':
    # здесь можно сделать ввод из консоли и проверить работу функции
    n = 10
    print(fibonacci(n))
