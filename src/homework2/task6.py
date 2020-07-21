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

    try:
        number = n
        new_number = number
        variable = 0
        while number > 0:
            digit = number % 10
            number //= 10
            variable = variable * 10 + digit
        if new_number == variable:
            return True
        else:
            return False
    except ValueError:
        return 'Вы ввели не число'


if __name__ == '__main__':
    # здесь можно сделать ввод из консоли и проверить работу функции
    n = 0
    print(palindrom(n))
