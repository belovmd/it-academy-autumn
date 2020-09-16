# Даны два списка чисел. Посчитайте, сколько различных
# чисел входит только в один из этих списков


lst1 = [8, 4, 5, 3, 5, 3, 78, 3, 56, 25, 54, 6, 4, 23]
lst2 = [8, 4, 5, 3, 5, 3, 38, 74, 52, 75, 24, 234, 456, 24]
counter = 0
dct1, dct2 = {el:1 for el in lst1}, {el:1 for el in lst2}
for key in dct1:
    if key not in dct2:
        counter += 1
for key in dct2:
    if key not in dct1:
        counter += 1
print(counter)
