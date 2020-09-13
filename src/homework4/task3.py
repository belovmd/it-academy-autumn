"""
Даны два списка чисел.
Посчитайте, сколько различных чисел содержится
одновременно как в первом списке, так и во втором.
"""


list_one = [1, 2]
list_two = [1, 2, 3]

set_one = set(list_one)
set_two = set(list_two)

common_elements = set_one.intersection(set_two)
print(len(common_elements))
