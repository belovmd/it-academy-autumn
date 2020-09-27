"""
Оформите решение задач из прошлых домашних работ в функции.
"""
from src.homework5 import functions


def run_function_from_module(module_name, func_name):
    if hasattr(module_name, func_name):
        func_instance = getattr(module_name, func_name)
        if callable(func_instance):
            print("Run func - ", func_name)
            func_instance()
        else:
            print("Attribute [{name}] not callable".format(name=func_name))
    else:
        print("Func [{name}] not exist".format(name=func_name))


def runner(*args):
    if args:
        [run_function_from_module(functions, param)
         for param in args if isinstance(param, str)]
    else:
        [run_function_from_module(functions, param)
         for param in dir(functions)]


runner()
