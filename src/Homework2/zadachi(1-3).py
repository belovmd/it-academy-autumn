# Кубы первых n чисел
n = int(input("Введите кол-во n чисeл - "))
for el in range(n):
    print(el * el * el)
# Проверка числа на простоту
num = int(input("Введите число которое необходимо проверить на простоту - "))
if num == 1:
    print('Это единица!')
elif num == 2:
    print('Это простое число')
else:
    i = 2
    while i < num ** 0.5:
        if n % i == 0:
            print('Это сложное число')
            break
        i += 1
    else:
        print('Это простое число')
# Проверить является ли число палиндромом
num = int(input("Введите число которое вы хотите проверить - "))
num_copy = num
check_sum = 0
while not int(num_copy % 10) > 0:
    check_sum = check_sum * 10 + int(num_copy % 10)
    num_copy = int(num_copy) / 10
    print('num_copy - ' + (str(num_copy)))
    print('check_sum - ' + (str(check_sum)))
if check_sum == num:
    print('Палиндром')
else:
    print('Не палиндром');
