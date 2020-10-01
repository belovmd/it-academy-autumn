"""
Создайте декоратор, который хранит
результаты вызовы функции
(за все время вызовов, не только текущий запуск программы)
"""


def save(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        with open('results.txt', 'at') as f:
            f.write(str(result) + '\n')
        return result
    return wrapper


@save
def sum_(a, b):
    return a + b


if __name__ == '__main__':
    for i in range(10):
        print(sum_(i, i))
