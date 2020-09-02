"""
Дан список чисел. Посчитайте, сколько в нем пар элементов,
равных друг другу. Считается, что любые два элемента,
равные друг другу образуют одну пару, которую необходимо посчитать.
Входные данные - строка из чисел, разделенная пробелами.
Выходные данные - количество пар.
Важно: 1 1 1 - это 3 пары, 1 1 1 1 - это 6 пар
"""


def count_pairs(lst):
    count_elements = {}
    for el in lst:
        count_elements[el] = count_elements.get(el, 0) + 1
    return sum(value * (value - 1) // 2 for value in count_elements.values())


if __name__ == '__main__':
    pair = [1, 1, 1, 1]
    print(count_pairs(pair))
