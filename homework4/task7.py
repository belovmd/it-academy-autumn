
# 7.	Оглянемся назад
# Даны два натуральных числа. Вычислите их наибольший общий
# делитель при помощи алгоритма Евклида (мы не знаем функции и рекурсию).



a = 1071
b = 462


while not a == b:
        if  a > b:
            a = a - b
            b = b
            print (a,b)
        else:
            b = b-a
            a = a
            print (a,b)
print(a,b)