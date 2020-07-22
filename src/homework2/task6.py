"""Определите, является ли число палиндромом (читается слева направо и справа
    налево одинаково).  Число положительное целое, произвольной длины. Задача
    требует работать только с числами (без конвертации числа в строку или
    что-нибудь еще)
"""


def palindrom(n):
    """Поиск числа фибоначчи.

    :param n: Число.
    :return: Bool. True или False. Является ли число палиндромом.
    """

    # write your code here
    div = 1
    while (n / div >= 10):
        div *= 10

    while (n != 0):
        led = n // div
        trail = n % 10
        if (led != trail):
            return False

        n = (n % div) // 10
        div = div / 100

    return True
    # write return value here


if __name__ == '__main__':
    # здесь можно сделать ввод из консоли и проверить работу функции
    n = 0
    print(palindrom(n))
