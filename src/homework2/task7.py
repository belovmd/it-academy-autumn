"""
1) Найти индекс такого элемента,
где сумма всех элементов справа и слева равна.
Если такого элемента нет - вернуть -1.
"""


def find_even_index(arr):

    left_sum, right_sum = 0, sum(arr)

    for i, e in enumerate(arr):
        right_sum -= e
        if left_sum == right_sum:
            return i
        left_sum += e

    return -1
