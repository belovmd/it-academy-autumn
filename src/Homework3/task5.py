"""
Уникальные элементы в списке
Дан список. Выведите те его элементы,
которые встречаются в списке только один раз.
Элементы нужно выводить в том порядке,
в котором они встречаются в списке.
"""

lst = [1, 1, 2, 3, 4, 5, 5, 5, 3]


def find_unique(lst):
    result_dict = {}
    for el in lst:
        result_dict[el] = result_dict.get(el, 0) + 1
    return [key for key, value in result_dict.items() if value == 1]


print(find_unique(lst))
