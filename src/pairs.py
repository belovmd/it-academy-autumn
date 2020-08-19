"""
Пары элементов
Дан список чисел. Посчитайте, сколько в нем пар элементов,
равных друг другу. Считается, что любые два элемента, равные
друг другу образуют одну пару, которую необходимо посчитать.
Входные данные - строка из чисел, разделенная пробелами.
Выходные данные - количество пар.
Важно: 1 1 1 - это 3 пары, 1 1 1 1 - это 6 пар
"""


from math import factorial


def combinations(n, k):
    return factorial(n) // (factorial(k) * factorial(n - k))


# Метод pairs_counter считает кол-во одинаковых элементов в списке
# и считает кол-во сочетаний для каждого элемента.
# Возвращает словарь {элемент : кол-во пар}


def pairs_counter(lst):
    elements_count = {}
    for el in lst:
        elements_count[el] = elements_count.get(el, 0) + 1
    pairs_count = {}
    for el in elements_count:
        count = elements_count[el]
        if count > 1:
            pairs_count[el] = combinations(count, 2)
    return pairs_count


numbers = "1 1 1 2 2 3 4 4 2 2 2 3 5 6 7 3 4 5 6 7 7 7 10"
numbers_lst = [int(el) for el in numbers.split()]

pairs = pairs_counter(numbers_lst)

for el in pairs:
    print('Кол-во пар для элемента {}: {}'.format(el, pairs[el]))
print('Всего пар: {}'.format(sum(pairs.values())))
