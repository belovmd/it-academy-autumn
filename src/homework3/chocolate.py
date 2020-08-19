# Шоколадка
# Прямоуголькик, размером n * n плиток.
# Разлом - деление шоколадки на две части с натуральными размерами по прямой.
# Долька - элемент шоколадки размером 1х1.
# Очевидно шоколадка состоит из n * m долек.
# Кусок - элемент шоколадки произвольного (целочисленного размера).
# Определите, можно ли одним разломом отделить от шоколадки
# кусок площадью ровно k.
# Определите, можно ли отломить от шоколадки ровно
# k долек за некоторое количество разломов.
# Определите, можно ли отломить от шоколадки ровно k долек с помощью t разломов

n = int(input('Введите длинну шоколадки: '))
m = int(input('Введите ширину шоколадки: '))
k = int(input('Введите количество долек, которые нужно отломить: '))
"""
Если площадь куска шоколадки меньше, чем площадь всей шоколадки,
то её можно отломить.
В то-же время, если кусок делиться нацело на одну из сторон,
то его можно отломить за один раз.
"""
if k < n * m and ((not k % m) or (not k % n)):
    print('Можно разломить за один разлом!')
elif k < n * m:
    print('Можно разломить за несколько разломов!')
else:
    print('Нельзя разломить!')
