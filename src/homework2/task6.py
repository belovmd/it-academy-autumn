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
    i = True
    if n <= 10:
        i = False
    if n == 100:
        i = False
    if n == 1000:
        i = False

    if n > 10:
        if n < 100:
            for i in range(1, 10):
                if i == (n // 10):
                    if i == (n % 10):
                        i = True
                        break
                    else:
                        i = False

    if n > 100:
        if n < 1000:
            for i in range(1, 10):
                if i == (n // 100):
                    if i == (n % 10):
                        i = True
                        break
                    else:
                        i = False

    return i


if __name__ == '__main__':
    # здесь можно сделать ввод из консоли и проверить работу функции
    n = int(input("Enter the number:"))

    print(palindrom(n))
