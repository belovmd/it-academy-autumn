"""
Дан список. Выведите те его элементы, которые встречаются в списке
 только один раз.
Элементы нужно выводить в том порядке, в котором они встречаются в списке.
"""


def unique_elements(lst):
    elements = {}
    for el in lst:
        elements[el] = elements.get(el, 0) + 1
    return [key for key, value in elements.items() if value == 1]



if __name__ == '__main__':
    pair = [7, 1, 1, 1, 1, 2, 2, 3, 3, 4, 4, 2, 2, 1, 5, 6]
    print(unique_elements(pair))

