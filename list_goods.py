count = int(input('vvedi number of items: '))          
dict_goods ={} 
value=0                    
for i in range(count):        
    text = input('vvedi key values through space :').split()     #split the input text based on space & store in the list 'text'
    dict_goods[text[0]] = float(text[1])       #assign the 1st item to key and 2nd item to value of the dictionary
    value += int(text[1])

print(dict_goods)
print('rubley {} kopeek {}'.format(int(value//1), int(10*value%10)))

