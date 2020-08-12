str1 = 'ab ac ad bb bc bd'
lst_comp = [elem for elem in str1.split()]
print(lst_comp)
lst_comp_slice = lst_comp[::2]
print(lst_comp_slice)
str2 = '1a 2a 3a 4a'
lst_comp2 = [elem for elem in str2.split()]
print(lst_comp2)
print(lst_comp2.pop(1))
print(lst_comp2)
lst_comp2_copy = lst_comp2[:]
lst_comp2_copy.insert(1, '2a')
print(lst_comp2_copy)
print(lst_comp2)
