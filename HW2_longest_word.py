#Task_find the longest word in the text
my_list=('method takes all items in an iterable and joins them into one string')
my_list1=my_list.split(' ')

my_list2= '.'.join(my_list1)

print(my_list2)
max_word=0
for i in my_list1:
    if len(i)>max_word:
        max_word=len(i)
        word=i
print('the longest word is: {}'.format(word))
