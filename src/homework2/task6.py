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
    num = n
    num2 = 0
    while num > 0:
        digit = num % 10
        num = num // 10
        num2 = (num2 * 10) + digit
    if not num2 - n:
        True
        return 'True'
    else:
        False
        return 'False'
    return ''  # write return value here


if __name__ == '__main__':
    # здесь можно сделать ввод из консоли и проверить работу функции
    n =0
    print(palindrom(n))
