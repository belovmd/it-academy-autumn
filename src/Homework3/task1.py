"""
FizzBuzz
Напишите программу, которая печатает цифры от 1 до 100,
но вместо чисел, кратных 3 пишет Fizz,
вместо чисел кратный 5 пишет Buzz,
а вместо чисел одновременно кратных и 3 и 5 - FizzBuzz
"""


def fizz_buzz():
    for el in range(1, 101):
        print(('Fizz' * (not el % 3) + 'Buzz' * (not el % 5)) or el, sep='\n')


fizz_buzz()


print([('Fizz' * (not el % 3) +
        'Buzz' * (not el % 5)) or el for el in range(1, 101)])
