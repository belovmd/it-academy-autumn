from datetime import datetime
from functools import wraps

from src.homework5 import functions


# Создайте декоратор, который хранит результаты вызовы функции
# (за все время вызовов, не только текущий запуск программы)


def decor(foo):
    @wraps(foo)
    def wrapper(*args, **kwargs):
        res = foo(*args, *kwargs)
        start = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
        with open('result.txt', 'a') as result:
            result.write('Функция: {}\n'.format(foo.__name__))
            result.write('Запущена: {}\n'.format(start))
            result.write('Результат: {}\n'.format(res))
            result.write('\n')
        return res

    return wrapper


decor(functions.languges)()

# Имена функций:
# Про страны с городами - 'capitals',
# Пересечение множеств - 'setTask1',
# Объединение множеств - 'setTask2',
# Школьники, которые знают языки - 'languges',
# Подсчет слов в тексте - 'text',
# НОД по Евклиду - 'euklid'.
