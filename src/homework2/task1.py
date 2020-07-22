"""Напишите программу, которая считает общую цену.

   Вводится M рублей и N копеек цена, а также количество S товара
   Посчитайте
   общую цену в рублях и копейках за L товаров.
"""


def total_sum(m, n, s):
    """Подсчет общей суммы покупок.

    :param m: рубли
    :param n: копейки
    :param s: количество товара
    :return: строка. общая цена в рублях и копейках. формат:
        'x rubles y kopecks'

    """
    m = abs(int(m))
    n = abs(int(n))
    s = abs(int(s))
    x = m * s
    y = str(n * s)
    rub = 0
    str_rub = ''
    while len(y) > 2:
        str_rub += y[rub]
        y = y[:rub] + y[rub + 1:]
    x = x + int(str_rub)
    return str(x) + ' rubles ' + str(int(y)) + ' kopecks'


if __name__ == '__main__':
    m, n, s = '23', '36', '111'
    print(total_sum(m, n, s))
