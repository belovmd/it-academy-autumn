lst = [0, 2, 1, 0, 0, 4, 3, 0, 0, 5]
for el in lst:
    if el == 0:
        lst.remove(0)
        lst.append(0)
print(lst)
