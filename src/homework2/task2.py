from string import punctuation

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
    str_items = str_.split()

    words = []
    for item in str_items:
        words.append(item.strip(punctuation))

    max_len_word = ''
    max_len = 0
    for word in words:
        word_len = len(word)
        if word_len > max_len:
            max_len_word = word
            max_len = word_len

    return max_len_word  # write return value here


if __name__ == '__main__':
    # здесь можно сделать ввод из консоли и проверить работу функции
    str_ = ''
    print(longest_word(str_))
