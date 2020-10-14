# Реализовать функцию get_ranges которая получает на вход непустой
# список неповторяющихся целых чисел, отсортированных по возрастанию,
# которая этот список “сворачивает”
# get_ranges([0, 1, 2, 3, 4, 7, 8, 10]) // "0-4,7-8,10"
# get_ranges([4,7,10]) // "4,7,10"
# get_ranges([2, 3, 8, 9]) // "2-3,8-9"


def get_ranges(lst):
    fold_str = ''
    for i, el in enumerate(lst):
        if i == 0:
            fold_str += str(el)
        elif el - lst[i - 1] > 1 and lst[i - 1] - lst[i - 2] == 1:
            fold_str += '-' + str(lst[i - 1]) + ',' + str(el)
        elif el - lst[i - 1] > 1:
            fold_str += ',' + str(el)
        elif el == lst[-1]:
            fold_str += '-' + str(el)
    return fold_str


num_lst = [0, 1, 2, 3, 4, 7, 8, 10]
get_ranges(num_lst)

lst = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
get_ranges(lst)
