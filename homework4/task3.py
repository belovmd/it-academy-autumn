"""
3.	Даны два списка чисел. Посчитайте, сколько различных чисел
содержится одновременно как в первом списке, так и во втором.
"""

dct_1 = {}
dct_2 = {}
lst_1 = [1, 2, 2, 2, 2, 2, 2, 111]
lst_2 = [22, 3, 4, 5, 6, 7, 7, 7, 8, 8, 6, 4, 3]

for i in lst_1:
    dct_1[i] = dct_1.get(i, 0) + 1


for i in lst_2:
    dct_2[i] = dct_2.get(i, 0) + 1
print('в списках содедержится', len(dct_1)+len(dct_2), 'различных чисел')
