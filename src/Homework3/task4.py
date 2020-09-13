"""
Пары элементов
Дан список чисел. Посчитайте, сколько в нем пар элементов,
равных друг другу. Считается, что любые два элемента, равные
друг другу образуют одну пару, которую необходимо посчитать.
Входные данные - строка из чисел, разделенная пробелами.
Выходные данные - количество пар.
Важно: 1 1 1 - это 3 пары, 1 1 1 1 - это 6 пар
"""


def count_pairs(count):
    return count * (count - 1) // 2


def find_pairs(lst):
    elements_dict = {}
    result = 0
    for el in lst:
        elements_dict[el] = elements_dict.get(el, 0) + 1
    for count_of_element in elements_dict.values():
        if count_of_element >= 2:
            result += count_pairs(count_of_element)
    return result


lst = [1, 1, 1, 1]


print(find_pairs(lst))
