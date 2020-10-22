"""
Создайте декоратор, который хранит результаты вызовы функции
(за все время вызовов, не только текущий запуск программы)
"""
import datetime
from os import path

write_template = '{date}: args={args}, function={func}'


def my_dec(func):

    my_path = path.join(path.dirname(__file__), 'data', 'task2', 'source.txt')
    history = []

    with open(my_path) as f:
        for line in f:
            temp = []
            for num in line:
                temp.append(num)
            history.append(temp)

    def wrapper(*args, **kwargs):
        with open(my_path, 'a') as file:

            print(write_template.format(date=str(datetime.datetime.now()),
                                        args=str(args),
                                        func=func.__name__),
                  file=file)
        history.append(list(args))
        result = func(*args, **kwargs)
        return result
    return wrapper


@my_dec
def my_sum(*args):
    sum_ = 0
    # many input lists
    for lst in args:
        for num in lst:
            sum_ += num
    return sum_


def main():
    my_test_lst = [num for num in range(7)]
    print(my_sum(my_test_lst, my_test_lst))


if __name__ == '__main__':
    main()
