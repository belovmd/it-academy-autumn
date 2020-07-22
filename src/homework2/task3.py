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
    print(clear_str)
    return 'Введеная строка - ' + str_ + '; Очищенная строка - ' + clear_str  # write return value here


if __name__ == '__main__':
    # здесь можно сделать ввод из консоли и проверить работу функции
    str_ = 'здесь можно сделать ввод .. из консоли и // проверить работу функции'
    print(sub_string(str_))
