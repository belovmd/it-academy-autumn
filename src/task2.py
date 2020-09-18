"""
2.	Создайте декоратор, который хранит результаты вызовы функции
(за все время вызовов, не только текущий запуск программы)
"""

def my_dec(func):
    lst_ = []
    def wrapper(*args,**kwargs):
        res = func(*args,**kwargs)+1
        nonlocal lst_
        lst_.append(res)
        return lst_
    return wrapper

@my_dec
def func(a,b,c):
    return a+b+c


func(1,2,3)
func(1,4,3)
func(1,2,55)
func(1,2,12)
func(1,2,3)
func(1,4,3)
func(1,2,55)
func(1,2,12)

lst_2 = func(1,2,333)
print(lst_2)
