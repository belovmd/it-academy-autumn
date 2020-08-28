"""
Уникальные элементы в списке
Дан список. Выведите те его элементы,
которые встречаются в списке только один раз.
Элементы нужно выводить в том порядке,
в котором они встречаются в списке.
"""


def get_unique_elements(lst):
    result = []
    elem_count = {}
    for el in lst:
        elem_count[el] = elem_count.get(el, 0) + 1
    for el in lst:
        if elem_count[el] == 1:
            result.append(el)
            elem_count[el] = 0
    return result


list_ = [1, 1, 2, 3, 32, 65, 35, 4, 5, 5, 4, 3, 3, 6, 8, 9, 65]
unique_elements = get_unique_elements(list_)
for element in unique_elements:
    print(element, end=' ')
