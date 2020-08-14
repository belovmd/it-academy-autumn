"""
List practice
Используйте генератор списков чтобы получить следующий:
['ab', 'ac', 'ad', 'bb', 'bc', 'bd'].
Используйте на предыдущий список slice чтобы получить следующий:
['ab', 'ad', 'bc'].
Используйте генератор списков чтобы получить следующий
['1a', '2a', '3a', '4a'].
Одной строкой удалите элемент  '2a' из прошлого списка и напечатайте его.
Скопируйте список и добавьте в него элемент '2a'
так чтобы в исходном списке этого элемента не было.
"""


origin_list = list('abcd')

# 1
origin_list = [a + b for a in origin_list[0:2] for b in origin_list[1:4]]
print(origin_list)

# 2
print(origin_list[0::2])

# 3
origin_list = [str(el) + 'a' for el in range(1, 5)]
print(origin_list)

# 4
print(origin_list.pop(1))

# 5
copy_list = origin_list[:]
copy_list.append('2a')
print(copy_list)
print(origin_list)
