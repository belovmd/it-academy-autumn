"""
1. Создайте список ['a', 'b', 'c'] и сделайте из него кортеж.
2. Создайте кортеж ('a', 'b', 'c'), И сделайте из него список
3. Сделайте следующие присвоения одной строкой a = 'a', b=2, c=’python’.
4.Создайте кортеж из одного элемента, чтобы при итерировании по этому
элементы последовательно выводились значения 1, 2, 3. Убедитесь что len()
исходного кортежа возвращает 1.
"""


def tuple_practice():
    # 1
    lst1 = ['a', 'b', 'c']
    tuple1 = tuple(lst1)
    print(tuple1)

    # 2
    tuple2 = 'a', 'b', 'c'
    lst2 = list(tuple2)
    print(lst2)

    # 3
    a, b, c = 'a', 2, 'python'
    print(a, b, c)

    # 4
    tuple3 = '1, 2, 3.',
    for el in tuple3:
        print(el)
    print('len =', len(tuple3))



if __name__ == '__main__':
    tuple_practice()
