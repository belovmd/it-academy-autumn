"""
Даны два списка чисел.
Посчитайте, сколько различных чисел входит только в один из этих списков
"""

list_one = [1, 2]
list_two = [1, 2, 3]

set_one = set(list_one)
set_two = set(list_two)

different_elements = set_one.symmetric_difference(set_two)
print(len(different_elements))
