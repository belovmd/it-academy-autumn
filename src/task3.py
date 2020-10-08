"""
Реализовать функцию get_ranges которая получает на вход непустой список
неповторяющихся целых чисел, отсортированных по возрастанию, которая этот
список “сворачивает”
get_ranges([0, 1, 2, 3, 4, 7, 8, 10]) // "0-4,7-8,10"
get_ranges([4,7,10]) // "4,7,10"
get_ranges([2, 3, 8, 9]) // "2-3,8-9"
"""


def get_ranges(lst):
    res = str(lst[0])
    last_num = lst[0]

    for num in lst[1:]:
        if num - last_num == 1:
            if res[-1] != '-':
                res += '-'
        else:
            if res[-1] == '-':
                res += str(last_num) + ',' + str(num)
            else:
                res += ',' + str(num)
        last_num = num

    if res[-1] == '-':
        res += str(lst[-1])

    return res


if __name__ == '__main__':
    print(get_ranges([0, 1, 2, 3, 4, 7, 8, 10]))
    print(get_ranges([4, 7, 10]))
    print(get_ranges([2, 3, 8, 9]))
