# Даны два натуральных числа. Вычислите их наибольший
# общий делитель при помощи алгоритма Евклида
# (мы не знаем функции и рекурсию).


nums = [int(el) for el in input('enter 2 nums separated by a space').split()]
mx, mn = max(nums), min(nums)
while True:
    div_remain = mx % mn
    if not div_remain:
        print(mn)
        break
    else:
        mx, mn = mn, div_remain


***
# Позже при углубленом копании в вопросе мною был 
# встречен более элегантный алгоритм решения. Вряд ли
# я в состоянии самостоятельно до него додуматься
# (хотя кто знает), но я не могу не оставить его здесь. 


a = int(input())
b = int(input())
while a != 0 and b != 0:
    if a > b:
        a = a % b
    else:
        b = b % a
print(a + b)
