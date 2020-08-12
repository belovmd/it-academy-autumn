"""
Определения:
Шоколадка - прямоугольник, размером n×m (n, m - натуральные).
Разлом - деление шоколадки на две части с натуральными размерами по прямой.
Долька - элемент шоколадки размером 1х1. Очевидно шоколадка состоит из n*m долек.
Кусок - элемент шоколадки произвольного (целочисленного размера).

1. Определите, можно ли одним разломом отделить от шоколадки кусок площадью ровно k.
2. Определите, можно ли отломить от шоколадки ровно k долек за некоторое количество разломов.
3. Определите, можно ли отломить от шоколадки ровно k долек с помощью t разломов
Описание решения поместите в docstring
"""


def chocolate(n, m, k, t):
    """

    :param n: сторона шоколоадки
    :param m: другая сторона шоколоадки
    :param k: 1) площадь куска 2) 3) кол-во долек в шоколадке
    :param t: кол-во разломов
    :return: tuple(bool, bool, bool)
    """
    area = n * m
    """
    1.
    слева условие делимости
    cправа условие что k меньше по площади и больше какой либо стороны
    если обе части выкидают True то можно разделить
    """
    ans1 = (not k % n or not k % m) and (k <= area and (k >= n or k >= m))

    """
    2.Если в шоколадке есть k долек, то всегда можно 
    """
    ans2 = k <= area

    """
    3 Делаем разлом всегда на полоске с большей длиной
    и затем разломы на дольки
    Для n и n - 1 долек нужно n - 1 разломов на куске 1 х n   
    """
    maxlen = n if n > m else m

    # если последний кусок, то кол-во разломов совпадает с кол-вом долек, кроме последей
    if k > area - maxlen:
        if k == area:
            ans3 = k - 1 <= t
        else:
            ans3 = k <= t
        if k > area:
            ans3 = False
        return ans1, ans2, ans3

    # Если последняя долька в куске 1 x n
    # Для n и n - 1 долек нужно n - 1 разломов на куске 1 х n
    if k % maxlen:
        ans3 = k + 1 <= t
    else:
        ans3 = k <= t

    return ans1, ans2, ans3


if __name__ == '__main__':

    print(*chocolate(6, 3, 18, 50))

