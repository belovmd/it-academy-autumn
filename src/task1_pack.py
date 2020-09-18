
"""
1.	Dict comprehensions
Создайте словарь с помощью генератора словарей, так чтобы его ключами были числа от 1 до 20, а значениями кубы этих чисел.
"""

def fun1():
    x = list(zip([i for i in range(1,20)],[i*3 for i in range(1,20)] ))
    print(x)
    return x


def fun2():
    dct_1 = {}
    dct_2 = {}
    lst_1 = [1, 2, 2, 2, 2, 2, 2, 111]
    lst_2 = [22, 3, 4, 5, 6, 7, 7, 7, 8, 8, 6, 4, 3]

    for i in lst_1:
        dct_1[i] = dct_1.get(i, 0) + 1

    for i in lst_2:
        dct_2[i] = dct_2.get(i, 0) + 1
    print('в списках содедержится', len(dct_1) + len(dct_2), 'различных чисел')


def fun3():
    dct_ = {}
    lst_ = []
    str_ = 'Во входной  строке записан тоь гп нпа нек к      текст ..... Словом с  .  читается'

    str_ = str_.split()

    for word in str_:
        if not len(word) <= 1:
            lst_.append(word)
    for i in lst_:
        dct_[i] = dct_.get(i, 0) + 1
    print(len(dct_), 'различных слов')