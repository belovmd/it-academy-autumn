"""Вводится строка. Требуется удалить из нее повторяющиеся символы и все
    пробелы. Например, если было введено "abc cde def", то должно быть
    выведено "abcdef".

   Подсказка: оператор in проверяет, входит ли подстрока в строку или нет.
"""


def sub_string(str_):
    """Конструирование подстроки.

    :param str_: входная строка
    :return: строка. Получившееся выражение
    """
    clear_str = ''
    for char in str_:
        if char not in clear_str and char != ' ':
            clear_str += char
    return clear_str


if __name__ == '__main__':
    str_ = 'sd asdas'
    print(sub_string(str_))
