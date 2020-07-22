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

    # write your code here
    y = []
    for i in str_:
        if i not in y:
            y.append(i)
    s_out = (''.join(y))
    s_out = s_out.replace(' ', '')
    return s_out  # write return value here


if __name__ == '__main__':
    # здесь можно сделать ввод из консоли и проверить работу функции
    str_ = ''
    print(sub_string(str_))
