"""
Создайте декоратор, который хранит результаты вызова функции (за все время
вызовов, не только текущий запуск программы)
"""


def dec(func):
    def wrapper(*args, **kwargs):
        with open('results.txt', 'a') as f:
            result = func(*args, **kwargs)
            f.write(str(result) + '\n')
    return wrapper


@dec
def multiply(a, b):
    return a * b


if __name__ == '__main__':
    multiply(3, 5)
    multiply(a=7, b=10)
