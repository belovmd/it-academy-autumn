"""Посчитать количество строчных (маленьких) и прописных (больших) букв в
    введенной строке. Учитывать только английские буквы.
"""


def count_letters(str_):
    """Подсчет символов.

    :param str_: входная строка
    :return: кортеж. (low_number, up_number). low_number - количество строчных,
                                              up_number - количество пописных.
    """

    # write your code here
    low_number = 0
    up_number = 0

    upper_list = 'QWERTYUIOPLKJHGFDSAZXCVBNM'
    lower_list = 'qwertyuioplkjhgfdsazxcvbnm'
    for i in range(len(str_)):
        if str_[i] in upper_list:
            up_number += 1
        if str_[i] in lower_list:
            low_number += 1
    return ('low -', low_number, ', ', 'up -', up_number)  # write return value here


if __name__ == '__main__':
    # здесь можно сделать ввод из консоли и проверить работу функции
    str_ = ''
    print(count_letters(str_))
