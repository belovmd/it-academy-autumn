"""Определите, является ли число палиндромом (читается слева направо и справа
    налево одинаково).  Число положительное целое, произвольной длины. Задача
    требует работать только с числами (без конвертации числа в строку или
    что-нибудь еще)
"""


def palindrom(n):
    """Проверка палиндрома.

    :param n: Число.
    :return: Bool. True или False. Является ли число палиндромом.
    """
    if n < 11:
        return False
    num_copy = n
    check_sum = 0
    last_dig = 0
    while num_copy >= 1:
        last_dig = int(num_copy % 10)
        check_sum = check_sum * 10 + last_dig
        num_copy = int(num_copy) / 10
    if check_sum == n:
        return True
    else:
        return False


if __name__ == '__main__':
    # здесь можно сделать ввод из консоли и проверить работу функции
    n = 213112
    print(palindrom(n))
