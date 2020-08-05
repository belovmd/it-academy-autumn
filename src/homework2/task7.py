#1. 
def mult_two(a, b):

    return a*b


#2
''' 3Ваше задание здесь создать функцию, которая получает массив(tuple) и возвращает набор с 3 элементами - первым, третьим, вторым с конца.

example

Входные данные: Набор длинной не менее 3 элементов.

Выходные данные: Набор элементов.'''

def easy_unpack(elements: tuple) -> tuple:
    """
        returns a tuple with 3 elements - first, third and second to the last
    """
    # your code here
    a = elements[0]
    b = elements[2]
    c = elements[-2]
    return a,b,c

if __name__ == '__main__':
    
    
    print('Examples:')
    print(easy_unpack((1, 2, 3, 4, 5, 6, 7, 9)))
    
   


#3'''Дана строка и нужно найти ее первое слово.

Это упрощенная версия миссии First Word.

Строка состоит только из английских символов и пробелов.
В начале и в конце строки пробелов нет.
Входные параметры: Строка.

Выходные параметры: Строка.'''

def first_word(text: str) -> str:
    """
        returns the first word in a given text.
    """
    str_ = ''
    for i in text:
        if not i == ' ':
           str_ = str_ + i
        else:
            break
    print (str_)
    return str_


if __name__ == '__main__':
    print("Example:")
    print(first_word("Hello world"))
    
   


#4
'''У вас есть положительное целое число. Попробуйте узнать, сколько у него цифр? 
Вход: положительный Int. Выход: Int. Пример:'''





def end_zeros(num: int) -> int:
    
    s = str(a)
    x = len(s)


    return x

if __name__ == '__main__':
    print("Example:")
    print(number_length(10))

   


#5
'''Не все элементы важны. Что вам нужно сделать здесь, это удалить из списка все элементы до указанного.


   [1,2,3,4,5]


Для иллюстрации у нас есть список [3, 4, 5], и нам нужно удалить все элементы, которые идут до 3 - это 1 и 2.

У нас есть два крайних случая: (1) если режущий элемент не может быть найден, то список не должен изменяться. (2) если список пуст, то он должен оставаться пустым.

Вход: список и элемент границы.

Выход: Iterable (кортеж, список, итератор ...)."""



def remove_all_before(items: list, border: int) -> Iterable:
    # your code here
    lst_ = []
    
    
    if border== 0:
        lst_=items       
     
    elif border not in items:
        lst_=items 
    
    else:      
        for i in range(0,len(items)):
          if  border == items[i] :
            lst_= items[i:]
            break
          
           
            
    print(lst_)
    
    return lst_


if __name__ == '__main__':
    print("Example:")
    print(list(remove_all_before([1, 2, 3, 4, 5], 3)))

