"""
Дан список. Выведите те его элементы, которые встречаются в списке только один
раз. Элементы нужно выводить в том порядке, в котором они встречаются в списке.
"""


def element_ones(lst):
    elem_count = {}
    for el in lst:
        elem_count[el] = elem_count.get(el, 0) + 1
    for el in elem_count:
        if elem_count[el] == 1:
            print(el)


if __name__ == '__main__':
    lst = [1, 2, 3, 4, 5, 5, 4]
    element_ones(lst)
