"""
Во входной строке записан текст. Словом считается последовательность
непробельных символов идущих подряд, слова разделены одним или большим числом
пробелов или символами конца строки. Определите, сколько различных слов
содержится в этом тексте.
"""


def count_words(str_):
    return len(set(str_.split()))


if __name__ == '__main__':
    str_ = """kjfljd kjfljd   kjkdj
    kdjfdknn  kjdkf
    fldf dfkjkfjdk   h dkfjdkj dfkd"""

    print(count_words(str_))
