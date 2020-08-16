"""
Дан список целых чисел. Требуется переместить все ненулевые элементы в левую
часть списка, не меняя их порядок, а все нули - в правую часть.
Порядок ненулевых элементов изменять нельзя, дополнительный список
использовать нельзя, задачу нужно выполнить за один проход по списку.
Распечатайте полученный список.
"""


def swap_(lst, right_index, left_index):
    tmp = lst[left_index]
    lst[left_index] = lst[right_index]
    lst[right_index] = tmp


def zero_to_hero(lst):
    left_index = 0
    for right_index in range(0, len(lst)):
        if lst[right_index] != 0:
            if left_index < right_index:
                swap_(lst, right_index, left_index)
            left_index += 1
    print(lst)


lst = [0, 1, 0, 3, 1, 0, 5, 4, 7, 10, 0, 1, 0]

zero_to_hero(lst)

lst = [0, 3, 0]

zero_to_hero(lst)
