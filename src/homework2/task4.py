"""Посчитать количество строчных (маленьких) и прописных (больших) букв в
    введенной строке. Учитывать только английские буквы.
"""


def count_letters(str_):
    """Подсчет символов.

    :param str_: входная строка
    :return: кортеж. (low_number, up_number). low_number - количество строчных,
                                              up_number - количество пописных.
    """
    # write your code here
    low_number = 0
    up_number = 0
    alef = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz'
    for letters in str_:
        if letters in alef:
            if letters.islower():
                low_number+=1
                continue
            if letters.upper():
                up_number+=1

    print(low_number,up_number)

    #return (low_number, up_number)  # write return value here


if __name__ == '__main__':
    # здесь можно сделать ввод из консоли и проверить работу функции
    str_ = 'fvdfdgASDDWWWSDdedf!!!ваавыапкыеы'
    #print(count_letters(str_))
    count_letters(str_)
