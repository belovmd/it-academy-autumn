# List practice
# Используйте генератор списков чтобы получить следующий:
# ['ab', 'ac', 'ad', 'bb', 'bc', 'bd'].
# Используйте на предыдущий список slice чтобы получить следующий:
# ['ab', 'ad', 'bc'].
# Используйте генератор списков чтобы получить следующий:
# ['1a', '2a', '3a', '4a'].
# Одной строкой удалите элемент  '2a' из прошлого списка и напечатайте его.
# Скопируйте список и добавьте в него элемент '2a'
# так чтобы в исходном списке этого элемента не было.

list_1 = [i + j for i in 'ab' for j in 'bcd']
print(list_1)
print(list_1[::2])

list_2 = [i + 'a' for i in '1234']
print(list_2)

print(list_2.pop(1))

list_3 = list_2.copy()
list_3.append('2a')
print(list_3)
