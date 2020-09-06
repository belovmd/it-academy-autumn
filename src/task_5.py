"""
Дан список. Выведите те его элементы, которые встречаются в
только один раз. Элементы нужно выводить в том порядке, в котором
они встречаются в списке.
"""
lst = [1, 2, 3, 2, 4, 5, 4, 3]
dct = {}
for elem in lst:
    dct[elem] = dct.get(elem, 0) + 1
list_comp = [key for key, value in dct.items() if value == 1]
print(list_comp)
