"""
Дан список целых чисел. Требуется переместить все ненулевые элементы в левую
часть списка, не меняя их порядок, а все нули - в правую часть. Порядок
ненулевых элементов изменять нельзя, дополнительный список использовать нельзя,
задачу нужно выполнить за один проход по списку. Распечатайте полученный
список.
"""


def move_zeros_to_right(lst):
    i = 0
    count = 0  # this variable counts the number of items passed
    while i < len(lst) and count < len(lst):
        if not lst[i]:
            lst.insert(len(lst) - 1, lst.pop(i))
        else:
            i += 1
        count += 1
    return lst


if __name__ == '__main__':
    lst = [0, 1, 0, 2, 0, 0, 0, 0, 3, 4, 5, 5, 4, 0]
    print(move_zeros_to_right(lst))
