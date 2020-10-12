# Даны два списка чисел. Посчитайте, сколько различных
# чисел входит только в один из этих списков


lst1 = [8, 4, 5, 3, 5, 3, 78, 3, 56, 25, 54, 6, 4, 23]
lst2 = [8, 4, 5, 3, 5, 3, 38, 74, 52, 75, 24, 234, 456, 24]
set1, set2 = set(lst1), set(lst2)
not_repet_in_lsts = len(set1) + len(set2)
set1.update(set2)
print(not_repet_in_lsts - ((not_repet_in_lsts - len(set1)) * 2))
