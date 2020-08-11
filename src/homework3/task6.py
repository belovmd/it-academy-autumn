"""
Дан список целых чисел. Требуется переместить все ненулевые элементы в левую
 часть списка, не меняя их порядок, а все нули - в правую часть.
Порядок ненулевых элементов изменять нельзя, дополнительный список
 использовать нельзя, задачу нужно выполнить за один проход по списку.
Распечатайте полученный список.
"""


def zero_to_right(lst):
    count = 0
    for i in range(len(lst)):
        if lst[i]:
            lst[i], lst[count] = lst[count], lst[i]
            count += 1
    return lst


if __name__ == '__main__':
    lst = [0, 2, 0, 1, 0, 4, 3, 2, 0, 1, 0, 4, 0]
    print(zero_to_right(lst))

