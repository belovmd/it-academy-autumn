"""Выведите n-ое число Фибоначчи, используя только временные переменные,
    циклические операторы и условные операторы. n - вводится.
"""


def fibonacci(n):
    """Поиск числа фибоначчи.

    :param n: Номер числа Фибоначчи.
    :return: Число. n-ое число Фибоначчи
    """

    # write your code here

    if n == 0:
        i3 = 0

    if n == 1:
        i3 = 1


    else:
        i1 = 0
        i2 = 1

        while n - 1  > 0:
            i3 = i1+i2
            i1 = i2
            i2 = i3

            n-=1
    print(i3)
    #return ''  # write return value here


if __name__ == '__main__':
    # здесь можно сделать ввод из консоли и проверить работу функции
    n = 14
    #print(fibonacci(n))
    fibonacci(n)