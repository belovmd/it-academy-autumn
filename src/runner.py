"""
Напишите функцию runner. (все станет проще когда мы изучим модули, getattr и setattr)
runner() – все фукнции вызываются по очереди
runner(‘func_name’) – вызывается только функцию func_name.
runner(‘func’, ‘func1’...) - вызывает все переданные функции
"""


import runner_test


def runner(module, *argc):
    func_set = set(argc)
    call_all = True
    if func_set:
        call_all = False

    attr_list = dir(module)
    for attr_name in attr_list:
        attr = getattr(module, attr_name)
        if type(attr).__name__ == 'function':
            if call_all:
                attr()
            else:
                if attr_name in func_set:
                    attr()


if __name__ == '__main__':
    runner(runner_test)
    print('--------------')
    runner(runner_test, 'func3')
    print('--------------')
    runner(runner_test, 'func1', 'func7', 'func5')
