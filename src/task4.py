"""
Даны два списка чисел. Посчитайте, сколько различных
 чисел входит только в один из этих списков
"""
lst_1 = [1, 2, 3, 4, 5, 6]
lst_2 = [5, 6, 7, 8, 9]
total_different = set(lst_1) ^ set(lst_2)
different_lst_1 = set(lst_1) & total_different
print(different_lst_1)
print(len(list(different_lst_1)))
