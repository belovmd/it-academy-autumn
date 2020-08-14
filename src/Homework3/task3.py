"""Tuple practice
Создайте список ['a', 'b', 'c'] и сделайте из него кортеж.
Создайте кортеж ('a', 'b', 'c'), И сделайте из него список
Сделайте следующие присвоения одной строкой a = 'a', b=2, c=’python’.
Создайте кортеж из одного элемента, чтобы при итерировании по этому элементы
последовательно выводились значения 1, 2, 3.
Убедитесь что len() исходного кортежа возвращает 1.
"""

# 1
origin_list = ['a', 'b', 'c']
origin_tuple = tuple(origin_list)
print(origin_tuple)

# 2
origin_tuple = ('a', 'b', 'c')
origin_list = list(origin_tuple)
print(origin_list)

# 3
a, b, c = 'a', 2, 'python'
print(a, b, c)

# 4
origin_tuple = ((1, 2, 3),)
for el in origin_tuple:
    print(el)
print('len =', len(origin_tuple))
