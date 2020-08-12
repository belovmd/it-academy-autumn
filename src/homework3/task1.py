"""
Напишите программу, которая печатает цифры от 1 до 100,
но вместо чисел, кратных 3 пишет Fizz,
вместо чисел кратный 5 пишет Buzz,
а вместо чисел одновременно кратных и 3 и 5 - FizzBuzz
"""


def fizz_buzz():
    [print("Fizz" * (not i % 3) + "Buzz" * (not i % 5) or i)
     for i in range(1, 101)
     ]


if __name__ == '__main__':
    fizz_buzz()
