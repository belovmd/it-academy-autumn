"""Напишите программу, которая считает общую цену.

   Вводится M рублей и N копеек цена, а также количество S товара Посчитайте
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
    # write your code here

    rubs = m * s
    cents = n * s

    rubs += cents // 100
    cents = cents % 100
    return '%d rubles %d kopecks' % (rubs, cents)


if __name__ == '__main__':
    # здесь можно сделать ввод из консоли и проверить работу функции
    m, n, s = 12, 12, 0
    print(total_sum(m, n, s))
