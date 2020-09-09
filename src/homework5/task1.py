"""
Оформите решение задач из прошлых домашних работ в функции.
Напишите функцию runner.
(все станет проще когда мы изучим модули, getattr и setattr)
runner() – все фукнции вызываются по очереди
runner(‘func_name’) – вызывается только функцию func_name.
runner(‘func’, ‘func1’...) - вызывает все переданные функции
"""

from src.homework2.task1 import total_sum
from src.homework2.task2 import longest_word
from src.homework2.task3 import sub_string
from src.homework2.task4 import count_letters
from src.homework2.task5 import fibonacci
from src.homework2.task6 import palindrom


def runner(*args):
    if not args:
        args = ('total_sum', 'longest_word', 'sub_string',
                'count_letters', 'fibonacci', 'palindrom')
    funcs = {
        'total_sum': ('2', '5', '10'),
        'longest_word': ("asd  asd af d asd gfa gaf dasfadsfsad fsa sdfa s",),
        'sub_string': ('.///.../.,,,,',),
        'count_letters': ('ASd sadasdas aDASD AFad asd asDSADA',),
        'fibonacci': (15,),
        'palindrom': (12344321,),
    }

    for func in args:
        arg = funcs[func]
        print(func + ':', globals()[func](*arg))


def main():
    my_all = [total_sum, longest_word, sub_string, count_letters, fibonacci,
              palindrom]
    dir(my_all)
    runner()


if __name__ == '__main__':
    main()
