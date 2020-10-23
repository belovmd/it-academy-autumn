"""
Реализовать функцию get_ranges которая
получает на вход непустой список неповторяющихся
целых чисел, отсортированных по возрастанию,
которая этот список “сворачивает”
"""


def get_range_str(lst):
    if lst:
        return str(lst[0]) + ('-' + str(lst[-1])) * (len(lst) > 1) + ','
    return ''


def get_ranges(lst):
    result = ''
    ranges = []
    for ind, el in enumerate(lst):
        if not ranges:
            ranges.append(el)
        elif el == ranges[-1] + 1:
            ranges.append(el)
        else:
            result += get_range_str(ranges)
            ranges = [el]
    return (result + get_range_str(ranges))[:-1]


if __name__ == '__main__':
    lst1 = [1, 2, 3, 5, 6, 7, 9, 10, 11]
    lst2 = [-10, -9, -8, 0, 1, 2, 3, 4, 5]
    lst3 = [1, 3, 5, 7, 9, 11, 13]
    lst4 = [1, 2, 3, 5, 9, 10, 11]
    print(get_ranges(lst1))
    print(get_ranges(lst2))
    print(get_ranges(lst3))
    print(get_ranges(lst4))
