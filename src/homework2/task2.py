"""Найти самое длинное слово в введенном предложении.

    В случае если их несколько, самое левое в строке Учтите что в предложении
    есть знаки препинания.
"""


from string import punctuation


def longest_word(str_):
    """Поиск самого длинного слова в предложении.

    :param str_: входная строка
    :return: строка. Самое длинное слово в предложении (в случае если их
        несколько, самое левое в строке).
        в случае если
    """

    words_with_punctuation = str_.split()
    words = [word.strip(punctuation) for word in words_with_punctuation]

    max_word = ''
    max_length = 0
    for word in words:
        word_len = len(word)
        if word_len > max_length:
            max_word = word
            max_length = word_len
    # write your code here
    return max_word  # write return value here


if __name__ == '__main__':
    # здесь можно сделать ввод из консоли и проверить работу функции
    str_ = 'word {} wordd  '
    print(longest_word(str_))
