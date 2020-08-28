def order(lst):
    ind = 0
    lst_length = len(lst)
    while ind < lst_length:
        if lst[ind] == 0:
            del lst[ind]
            lst.append(0)
            lst_length -= 1
        else:
            ind += 1


list_1 = [0, 0, 0, 0, 1, 2, 3, 4]
list_2 = [1, 0, 2, 0, 3, 0, 4, 0]
list_3 = [0, 0, 0, 0, 0, 0, 0, 0]
list_4 = [1, 2, 3, 4, 5, 6, 7, 8]
list_5 = []
list_6 = [1, 0, 0, 1, 0, 1, 0, 1, 1, 1, 0, 0, 0, 1, 0, 0, 1, 1, 1, 0]

order(list_1)
order(list_2)
order(list_3)
order(list_4)
order(list_5)
order(list_6)

print(list_1, list_2, list_3, list_4, list_5, list_6, sep='\n')
