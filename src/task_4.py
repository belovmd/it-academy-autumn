str_ = '1 1 1 1 '
count = 0
list_comp = [int(el) for el in str_.split()]
for i in range(len(list_comp)):
    for j in range(i + 1, len(list_comp)):
        if list_comp[i] == list_comp[j]:
            count += 1
print(count)
