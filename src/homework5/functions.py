def fizz_buzz():
    for el in range(1, 101):
        print(('Fizz' * (not el % 3) + 'Buzz' * (not el % 5)) or el)


def find_unique(lst=[1, 1, 2, 3, 4, 5, 5, 5, 3]):
    result_dict = {}
    for el in lst:
        result_dict[el] = result_dict.get(el, 0) + 1
    print([key for key, value in result_dict.items() if value == 1])

