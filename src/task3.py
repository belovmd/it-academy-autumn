"""
Реализовать функцию get_ranges которая получает на вход непустой
список неповторяющихся целых чисел, отсортированных по возрастанию,
которая этот список “сворачивает”
 get_ranges([0, 1, 2, 3, 4, 7, 8, 10]) // "0-4,7-8,10"
 get_ranges([4,7,10]) // "4,7,10"
 get_ranges([2, 3, 8, 9]) // "2-3,8-9"

"""


def get_ranges(lst):
    bln = False
    num = 0
    str_ = ''

    for i in range(len(lst) - 1):
        try:
            if bln and not int(lst[i + 1]) == int(lst[i]) + 1:
                lst[num + 1:i] = '-'
                bln = False
                i = num - 1
            elif not bln and int(lst[i + 1]) == int(lst[i]) + 1:
                bln = True
                num = i

        except IndexError:
            pass

    for i in range(len(lst) - 1):
        if lst[i] != '-' and lst[i + 1] != '-':
            if int(lst[i]) + 1 == int(lst[i + 1]):
                lst.insert(i + 1, '-')

    for i in range(len(lst)):
        if not lst[i] == '-' and not lst[i - 1] == '-' and not str_ == '':
            str_ = str_ + ',' + str(lst[i])
        else:
            str_ = str_ + str(lst[i])

    return str_


if __name__ == '__main__':
    print(get_ranges([0, 1, 2, 3, 4, 7, 8, 10]))
    print(get_ranges([4, 7, 10]))
    print(get_ranges([2, 3, 8, 9]))
