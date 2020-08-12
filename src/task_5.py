lst = [1, 1, 2, 3, 2, 4, 5, 4, 3, 5]
new_lst = []
gencomp = [new_lst.append(el) for el in lst if el not in new_lst]
print(new_lst)
