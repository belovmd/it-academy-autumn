"""
Напишите функцию runner. (все станет проще когда мы изучим модули,
getattr и setattr)
runner() – все фукнции вызываются по очереди
runner(‘func_name’) – вызывается только функцию func_name.
runner(‘func’, ‘func1’...) - вызывает все переданные функции

"""
import task1


def functions(*args):
    for func in args:
        fun = getattr(task1, func)
        fun()


def runner(*args):
    if args:
        functions(*args)
    else:
        function = [attr for attr in dir(task1) if not attr.startswith('__')]
        functions(*function)


if __name__ == '__main__':
    runner()
    runner('func1')
    runner('func1', 'func2', 'func3')
