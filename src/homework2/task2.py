"""Найти самое длинное слово в введенном предложении.

    В случае если их несколько, самое левое в строке Учтите что в предложении
    есть знаки препинания.
"""


def longest_word(str_):
    """Поиск самого длинного слова в предложении.

    :param str_: входная строка
    :return: строка. Самое длинное слово в предложении (в случае если их
        несколько, самое левое в строке).
    """
    from string import punctuation

    line_str = str_.split()
    new_list = list()
    for words in line_str:
        new_list.append(words.split(punctuation))

    new_list.sort(key=len, reverse=True)
    if len(new_list) == 0:
        word = ''
    else:
        word = new_list[0]
    return word  # write return value here


if __name__ == '__main__':
    # здесь можно сделать ввод из консоли и проверить работу функции
    str_ = ''
    print(longest_word(str_))
