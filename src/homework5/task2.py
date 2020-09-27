"""
Создайте декоратор, который хранит результаты вызовы функции
(за все время вызовов, не только текущий запуск программы)
"""
from functools import wraps


def amazing_decorator(gorgeous_func):
    def super_wraper(*args, **kwargs):
        func_name = gorgeous_func.__name__
        func_result = gorgeous_func(*args, **kwargs)
        print(func_name, func_result)
    return super_wraper


@amazing_decorator
def god():
    print("")


god()
