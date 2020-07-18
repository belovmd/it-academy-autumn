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
    count = 0
    temp = n
    while temp:
        temp //= 10
        count += 1

    first = n // 10 ** (count - count // 2)
    last = n % 10 ** (count // 2)
    for i in range(1, count // 2 + 1):
        if not first // 10 ** (count // 2 - i) == last % 10:
            return False
        first %= 10 ** (count // 2 - i)
        last //= 10
    else:
        return True


if __name__ == '__main__':
    # здесь можно сделать ввод из консоли и проверить работу функции
    n = 1232
    print(palindrom(n))
