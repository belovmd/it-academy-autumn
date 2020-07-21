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
    text = "(hello, world. and everybody!)"
    var = text.maketrans(".,?:;!'()", "         ")
    text_new = text.translate(var)
    symbol = ""
    if text != "":
        for word in text_new.split():
            # print(word, len(word))
            if len(word) > len(symbol):
                symbol = word
        return "longest word is: " + symbol
    else:
        return ("You entered the empty string")


if __name__ == '__main__':
    # здесь можно сделать ввод из консоли и проверить работу функции
    str_ = ''
    print(longest_word(str_))
