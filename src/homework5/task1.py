# Оформите решение задач из прошлых домашних работ в функции.
# Напишите функцию runner. Dсе станет проще когда мы изучим модули,
# getattr и setattr)


from homework5 import my_pack as my_func


def runner(*args):
    lst = [*args]
    if not lst:
        func_names = []
        for el in dir(my_func):
            if not el.startswith('__'):
                func_names.append(el)
    else:
        func_names = [*args]

    for el in func_names:
        if hasattr(my_func, el):
            result = getattr(my_func, el)()
            print(result)
            print(el, 'done')
        else:
            print('func not found')


runner()
runner('zeros_to_the_right')
runner('zeros_to_the_right', 'fizz_buzz')
runner('bullshit')