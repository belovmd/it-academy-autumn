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
    genM = m * s
    genN = n * s
    if genN > 99:
        genM += genN // 100
        genN = genN % 100
    return (genM, 'rubles', genN, 'kopecks')  # write return value here


if __name__ == '__main__':
    # здесь можно сделать ввод из консоли и проверить работу функции
    m, n, s =5, 60, 6
    print(total_sum(m, n, s))
