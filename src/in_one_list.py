"""
Даны два списка чисел.
Посчитайте, сколько различных чисел
входит только в один из этих списков
"""


lst_1 = [1, 1, 2, 2, 3, 4, 5, 6, 7, 8, 9]
lst_2 = [2, 3, 4, 10, 11, 11]

print(len(set(lst_1) - set(lst_2)))
