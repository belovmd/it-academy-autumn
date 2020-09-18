"""
3.Реализовать функцию get_ranges которая получает на вход непустой список
неповторяющихся целых чисел, отсортированных по возрастанию, которая этот список
 “сворачивает”
 get_ranges([0, 1, 2, 3, 4, 7, 8, 10]) // "0-4,7-8,10"
 get_ranges([4,7,10]) // "4,7,10"
 get_ranges([2, 3, 8, 9]) // "2-3,8-9"
"""

lst_ = [2, 3, 8, 9]

def get_ranges(lst):
    l1 = ''
    lst_.reverse()
    while lst_:

        a1 = lst_.pop()
        a2 = a1

        while lst_ and lst_[-1] -a2 == 1:
            a2 = lst_.pop()


        if a1 == a2:
            l1+= str(a1)+','
        else:
            l1 += str(a1)+'-'+str(a2)+','


    l1 = l1[:-1]
    return l1



print(get_ranges(lst_))

