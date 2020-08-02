"""Вводится строка. Требуется удалить из нее повторяющиеся символы и все
    пробелы. Например, если было введено "abc cde def", то должно быть
    выведено "abcdef".

   Подсказка: оператор in проверяет, входит ли подстрока в строку или нет.
"""


def sub_string(str_):
    """Конструирование подстроки.

    :param str_: входная строка
    :return: строка. Получившееся выражение
    """
    y = []
    
    for i in str_:
        if i not in y and i != ' ':
            y.append(i)
   
            z = ''.join(y)
    print(z)
            
          
    # write your code here
    #return ''  # write return value here

if __name__ == '__main__':
    #str_ = input('Введите предложение:')
    str_ = 'abc cde def'
    #print(sub_string(str_))
    sub_string(str_)

