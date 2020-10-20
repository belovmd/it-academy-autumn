import inspect
from src.homework5 import functions

# Оформите решение задач из прошлых домашних работ в функции.
# Напишите функцию runner. (все станет проще когда мы изучим модули,
# getattr и setattr)
# runner() – все фукнции вызываются по очереди
# runner(‘func_name’) – вызывается только функцию func_name.
# runner(‘func’, ‘func1’...) - вызывает все переданные функции


def runner(foo, *args):
    if not foo:
        run_list = [el for el in dir(functions) if not el.startswith('__')]
    else:
        run_list = [foo]

        for foo in run_list:
            try:
                foo = getattr(functions, foo)
                if inspect.isfunction(foo):
                    print('Функция: ', foo.__name__)
                    print('Выполнение: ', foo(*args))
            except AttributeError:
                print('Функция не найдена.', foo)


runner('euklid', 2, 7)

# Имена функций:
# Про страны с городами - 'capitals',
# Пересечение множеств - 'setTask1',
# Объединение множеств - 'setTask2',
# Школьники, которые знают языки - 'languges',
# Подсчет слов в тексте - 'text',
# НОД по Евклиду - 'euklid'.
