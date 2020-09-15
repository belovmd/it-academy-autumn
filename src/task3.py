"""
Даны два списка чисел. Посчитайте, сколько различных чисел содержится
одновременно как в первом списке, так и во втором.
"""


def numbers_in_two_lists(lst1, lst2):
    return len(set(lst1) & set(lst2))


if __name__ == '__main__':
    lst1 = [1, 2, 3, 4, 5, 6, 6, 7]
    lst2 = [1, 3, 4, 5, 8, 9]
    print(numbers_in_two_lists(lst1, lst2))
