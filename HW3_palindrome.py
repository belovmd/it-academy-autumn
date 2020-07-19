my_list=('k a ba k')
my_list1=my_list.replace(' ','')
my_list2=my_list1[::-1]
if my_list1==my_list2:
    print('palindrome')
else:
    print('ne palindrome')
