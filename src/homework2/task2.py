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

    words_list = []
    word_str = ''

    for symbol in str_:
        if symbol.isalpha():
            word_str += symbol
        elif len(word_str) != 0:
            words_list.append(word_str)
            word_str = ''

    if word_str:
        words_list.append(word_str)

    max_length = 0
    max_word = ''
    for word in words_list:
        word_length = len(word)
        if word_length > max_length:
            max_length = word_length
            max_word = word

    # write your code here
    return max_word  # write return value here


if __name__ == '__main__':
    # здесь можно сделать ввод из консоли и проверить работу функции
    str_ = ''
    print(longest_word(str_))