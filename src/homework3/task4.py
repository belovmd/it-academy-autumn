"""
Дан список чисел. Посчитайте, сколько в нем пар элементов,
равных друг другу. Считается, что любые два элемента,
равные друг другу образуют одну пару, которую необходимо посчитать.
Входные данные - строка из чисел, разделенная пробелами.
Выходные данные - количество пар.
Важно: 1 1 1 - это 3 пары, 1 1 1 1 - это 6 пар
"""


def count_pairs_simple(lst):
    count = 0
    for start in range(len(lst)):
        for el in lst[start + 1:]:
            if lst[start] == el:
                count += 1
    return count


def count_pairs_advanced(lst):
    count_elements = {}
    for el in lst:
        count_elements[el] = count_elements.get(el, 0) + 1
    return sum([sum(range(value)) for value in count_elements.values()])


if __name__ == '__main__':
    pair = [1, 1, 1, 1, 2, 2, 3, 3, 4, 4, 2, 2, 1]
    print(count_pairs_simple(pair))
    print(count_pairs_advanced(pair))
