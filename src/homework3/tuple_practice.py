# Tuple practice
# 1. Создайте список ['a', 'b', 'c'] и сделайте из него кортеж.
# 2. Создайте кортеж ('a', 'b', 'c'), И сделайте из него список
# 3. Сделайте следующие присвоения одной строкой a = 'a', b=2, c=’python’.
# 4. Создайте кортеж из одного элемента,
# чтобы при итерировании по этому элементы
# последовательно выводились значения 1, 2, 3.
# Убедитесь что len() исходного кортежа возвращает 1.

tuple_ = tuple(['a', 'b', 'c'])
print(tuple_)

list_ = list(tuple_)
print(list_)

a, b, c = 'a', 2, 'python'
print(a, b, c)

tuple_2 = ([1, 2, 3], )
for i in range(3):
    print(tuple_2[0][i], end=', ')
print('len =', len(tuple_2))
