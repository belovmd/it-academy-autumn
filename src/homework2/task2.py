"""Найти самое длинное слово в введенном предложении.

    В случае если их несколько, самое левое в строке Учтите что в предложении
    есть знаки препинания.
"""
import operator

def longest_word(str_):
    """Поиск самого длинного слова в предложении.

    :param str_: входная строка
    :return: строка. Самое длинное слово в предложении (в случае если их
        несколько, самое левое в строке).
        в случае если
    """
    #очистка строк от знаков припенания
    clean_str_ = []
    str_ = str_.split()
    for word in str_:
        symbol = "(),.:\"&?;«»!><"
        for i in range(0,len(symbol)):
            word = word.replace(symbol[i],"")
        if len(word) > 1:
            clean_str_.append(word)


    #sort
    max_word = clean_str_[0]
    print(max_word)
    for word in clean_str_:
        if len(word) >= len(max_word):
            max_word_2 = max_word
            max_word = word
    if len(max_word_2) == len(max_word):
        str_1 = 'В строке два длинных слова, это самое левое в строке ' + max_word_2
    else:
        str_1 = 'Самое длинное слово - ' +  max_word

    return str_1  # write return value here


if __name__ == '__main__':
    # здесь можно сделать ввод из консоли и проверить работу функции
    str_ = ''
    str_ = input('Введите предложение:')
    print(longest_word(str_))
