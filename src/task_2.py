"""
Используйте генератор списков чтобы получить следующий:
 ['ab', 'ac', 'ad', 'bb', 'bc', 'bd'].
"""
lst_comp = [elem1 + elem2 for elem1 in 'ab' for elem2 in 'bcd']
print(lst_comp)


"""
Используйте на предыдущий список slice чтобы получить
 следующий: ['ab', 'ad', 'bc'].
 """
lst_comp_slice = lst_comp[::2]
print(lst_comp_slice)


"""
Используйте генератор списков чтобы получить следующий
 ['1a', '2a', '3a', '4a'].
"""
str2 = '1a 2a 3a 4a'
lst_comp2 = [elem for elem in str2.split()]
print(lst_comp2)


"""
Одной строкой удалите элемент  '2a' из прошлого списка
 и напечатайте его.
"""
print(lst_comp2.pop(1))
print(lst_comp2)


"""
Скопируйте список и добавьте в него элемент '2a' так
 чтобы в исходном списке этого элемента не было.
"""
lst_comp2_copy = lst_comp2[:]
lst_comp2_copy.insert(1, '2a')
print(lst_comp2_copy)
print(lst_comp2)
