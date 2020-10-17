"""
Оформите решение задач из прошлых домашних работ в функции. Напишите функцию
runner. (все станет проще когда мы изучим модули, getattr и setattr)
runner() – все фукнции вызываются по очереди
runner(‘func_name’) – вызывается только функцию func_name.
runner(‘func’, ‘func1’...) - вызывает все переданные функции
"""
from src import homework4 as lib


def run_functions(*args):
    for func in args:
        running_func = getattr(lib, func)
        running_func()


def runner(*args):
    if args:
        run_functions(*args)
    else:
        functions = [attr for attr in dir(lib)
                     if not attr.startswith('__')]
        run_functions(*functions)


if __name__ == '__main__':
    runner()
    runner('task7')
    runner('dict_comp', 'task7')
