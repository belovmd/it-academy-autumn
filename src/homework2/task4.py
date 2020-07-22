"""Посчитать количество строчных (маленьких) и прописных (больших) букв в
    введенной строке. Учитывать только английские буквы.
"""


def count_letters(str_):
    """Подсчет символов.

    :param str_: входная строка
    :return: кортеж. (low_number, up_number). low_number - количество строчных,
                                              up_number - количество пописных.
    """
    low_number = 0
    up_number = 0
    for symb in str_:
        if 'a' <= symb <= 'z':
            low_number += 1
        elif 'A' <= symb <= 'Z':
            up_number += 1
    return (low_number, up_number)


if __name__ == '__main__':
    # здесь можно сделать ввод из консоли и проверить работу функции
    str_ = 'FKjlkjkjdkfjlKJKJKJFK2324324'
    print(count_letters(str_))
