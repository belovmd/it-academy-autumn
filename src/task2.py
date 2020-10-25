"""
Создайте декоратор, который хранит результаты вызовы функции
(за все время вызовов, не только текущий запуск программы)

"""
from datetime import datetime


def decorator(func):
    def wrapper(*args, **kwargs):
        with open('file.txt', 'a') as f:
            f.write(str(func(*args, **kwargs)) + '\n')
        return f

    return wrapper


@decorator
def function1():
    return 4


@decorator
def function2():
    return 'friend'


@decorator
def time_now():
    return datetime.now()


print(function1())
print(function2())
print(time_now())
