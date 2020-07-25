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
    for nums in range(n-1):
        dig = a + b
        a, b = b, (a + b)
    return(dig - (b - a))  # а иначе не получается сделать две 1 подряд при n = 1 и n = 2


if __name__ == '__main__':
    # здесь можно сделать ввод из консоли и проверить работу функции
    n = ''
    print(fibonacci(n))
