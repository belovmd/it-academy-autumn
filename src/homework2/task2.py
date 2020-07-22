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
    import re
    str_ = re.sub(r'[^\w\s]', '', str_.replace("_", ""))
    str_ = str_.split(' ')
    spis = []
    for slovo in str_:
        spis.append(len(slovo))
    return str_[spis.index(max(spis))]


if __name__ == '__main__':
    str_ = '________'
    print(longest_word(str_))
