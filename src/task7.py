"""
Даны два натуральных числа. Вычислите их наибольший общий делитель при помощи
алгоритма Евклида (мы не знаем функции и рекурсию).
"""


big = 99
small = 8

while 1:
    if not big % small:
        break
    else:
        big, small = small, big % small

print(small)
