"""Найти самое длинное слово в введенном предложении.

    В случае если их несколько, самое левое в строке Учтите что в предложении
    есть знаки препинания.
"""


def longest_word(str_):
    """Поиск самого длинного слова в предложении.

    :param str_: входная строка
    :return: строка. Самое длинное слово в предложении (в случае если их
        несколько, самое левое в строке).
        в случае если
    """

    # write your code here
    import re

    str_ = re.sub(r'[^\w\s]', '', str_)
    maxlen = 0
    long_wors = ''
    for word in str_.split():
        if len(word) > maxlen:
            long_wors = word
            maxlen = len(word)
    return long_wors  # write return value here


if __name__ == '__main__':
    # здесь можно сделать ввод из консоли и проверить работу функции
    str_ = ''
    print(longest_word(str_))
