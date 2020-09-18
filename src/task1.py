"""
1.	Оформите решение задач из прошлых домашних работ в функции. Напишите функцию runner.
все станет проще когда мы изучим модули, getattr и setattr)
"""
import task1_pack

#1
def runner():
    getattr(task1_pack, 'fun1')()
    getattr(task1_pack,'fun2')()
    getattr(task1_pack,'fun3')()
runner()

#2
def runner(func_name):
    getattr(task1_pack, func_name)()
runner('fun1')

#3
def runner(*args):
    names = args
    for name in names:
        getattr(task1_pack, name)()

runner('fun1','fun2','fun3')