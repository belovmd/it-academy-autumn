"""
Напишите программу, которая печатает цифры от 1 до 100, но вместо чисел,
кратных 3 пишет Fizz, вместо чисел кратный 5 пишет Buzz, а вместо чисел
одновременно кратных и 3 и 5 - FizzBuzz
"""
# 1
for num in range(1, 101):
    if not num % 15:
        print('FizzBuzz')
    elif not num % 5:
        print('Buzz')
    elif not num % 3:
        print('Fizz')
    else:
        print(num)
# 2
print(['Fizz' * (not el % 3) + 'Buzz' * (not el % 5) 
       or el for el in range(1, 101)])
