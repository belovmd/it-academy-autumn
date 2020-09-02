"""
Во входной строке записан текст.
Словом считается последовательность непробельных символов идущих подряд,
слова разделены одним или большим числом пробелов или символами конца строки.
Определите, сколько различных слов содержится в этом тексте.
"""


def words(str_):
    words = set(str_.split())
    return len(words)


if __name__ == '__main__':
    str_ = (
        'asfd  asdf a asdf    aaf     asdf adsf   d  d  dd   dd d'
        '   asdfadfa   asdfadsfa asdf'
        '  asdfa n \n      \n  adsfadf   adf adf adf adf adf         \n   adf'
    )
    print(words(str_))
