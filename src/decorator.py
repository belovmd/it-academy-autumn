"""
Создайте декоратор, который хранит
результаты вызовы функции
(за все время вызовов, не только текущий запуск программы)
"""
from datetime import datetime


def save(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        with open('results.txt', 'a') as f:
            date_ = datetime.now()
            f.write(str(date_) + ' ' + str(func.__name__) + ' ' + str(result) + '\n')
        return result
    return wrapper


@save
def sum_(a, b):
    return a + b


if __name__ == '__main__':
    for i in range(10):
        print(sum_(i, i))
