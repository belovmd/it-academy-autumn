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

    all_rubles = m * s
    all_kopecks = n * s
    rubles = all_rubles + all_kopecks // 100
    kopecks = all_kopecks % 100
    return '{0} rubles {1} kopecks'.format(rubles, kopecks)


if __name__ == '__main__':
    # здесь можно сделать ввод из консоли и проверить работу функции
    m, n, s = '', '', ''
    print(total_sum(m, n, s))
