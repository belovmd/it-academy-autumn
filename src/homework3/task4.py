'''Пары элементов
Дан список чисел. Посчитайте, сколько в нем пар элементов, равных друг другу.
Считается, что любые два элемента, равные друг другу образуют одну пару,
которую необходимо посчитать.
Входные данные - строка из чисел, разделенная пробелами.
Выходные данные - количество пар.
Важно: 1 1 1 - это 3 пары, 1 1 1 1 - это 6 пар
'''
lst = list(map(int, input().split()))
total_pairs = 0
control = []
for num in lst:
    num_count = lst.count(num)
    if num not in control and num_count > 1:
        pairs = (num_count * (num_count-1)) / 2
        control.append(num)
    else:
        continue
    total_pairs += pairs
print(total_pairs)
