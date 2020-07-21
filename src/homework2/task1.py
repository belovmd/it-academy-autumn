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

    rubles = m
    kopecks = n
    rubles_total = rubles * s
    kopecks_total = kopecks * s
    if 100 <= kopecks_total < 1000000:
        kopecks_rez = kopecks_total % 100
        rubles_total = rubles_total + kopecks_total // 100
    elif kopecks_total < 100:
        kopecks_rez = kopecks_total
    return '{0} rubles {1} kopecks'. \
        format(rubles_total, kopecks_rez)


if __name__ == '__main__':
    # здесь можно сделать ввод из консоли и проверить работу функции
    m, n, s = '', '', ''
    print(total_sum(m, n, s))
