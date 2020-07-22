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
    str_ = str_.replace('_', ' ')
    list_of_words = str_.split(' ')
    words_with_only_letters = []
    for word in list_of_words:
        new_word = ''
        for symb in word:
            if symb.isalpha():
                new_word += symb
            else:
                break
        words_with_only_letters.append(new_word)
    list_of_lengths = []
    if not words_with_only_letters:
        return ''
    for word in words_with_only_letters:
        list_of_lengths.append(len(word))

    return words_with_only_letters[list_of_lengths.index(max(list_of_lengths))]


if __name__ == '__main__':
    # здесь можно сделать ввод из консоли и проверить работу функции
    str_ = '______________________________________word_wordd____wordd__'
    print(longest_word(str_))
