"""
Во входной строке записан текст. Словом считается последовательность
непробельных символов идущих подряд, слова разделены одним или большим числом
пробелов или символами конца строки. Определите, сколько различных слов
содержится в этом тексте.
"""


def count_words(str_):
    count = 0
    list_of_strings = str_.split('\n')
    for string in list_of_strings:
        count += len(string.split())
    return count


if __name__ == '__main__':
    str_ = """kjfljd kjdfldkjf   kjkdj
    kdjfdknn  kjdkf
    fldf dfkjkfjdk   h dkfjdkj dfkd"""

    print(count_words(str_))
