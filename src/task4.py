"""
Дан список чисел. Посчитайте, сколько в нем пар элементов, равных друг другу.
Считается, что любые два элемента,
равные друг другу образуют одну пару, которую необходимо посчитать.
Входные данные - строка из чисел, разделенная пробелами.
Выходные данные - количество пар.
Важно: 1 1 1 - это 3 пары, 1 1 1 1 - это 6 пар
"""


def element_pairs(str_):
    numbers_count = {}
    count = 0
    for el in str_.split():
        numbers_count[el] = numbers_count.get(el, 0) + 1

    for cnt in numbers_count.values():
        count += cnt * (cnt - 1) // 2
    return count


if __name__ == '__main__':
    str_ = '1 1 1 1 2 2'
    print(element_pairs(str_))
