"""
Оформите решение задач из прошлых домашних работ в функции.
"""


def func1(lst=[1, 1, 1, 1, 2, 3, 4]):
    para = 0
    dct = {}
    for elem in lst:
        dct[elem] = dct.get(elem, 0) + 1
    for value in dct.values():
        if value > 1:
            para += (value * (value - 1)) // 2
    print(para)


def func2(lst=[1, 2, 3, 2, 4, 5, 4, 3]):
    dct = {}
    for elem in lst:
        dct[elem] = dct.get(elem, 0) + 1
    list_comp = [key for key, value in dct.items() if value == 1]
    print(list_comp)


def func3(lst=[0, 2, 1, 0, 0, 4, 3, 0, 0, 5]):
    for el in lst:
        if el == 0:
            lst.remove(0)
            lst.append(0)
    print(lst)
