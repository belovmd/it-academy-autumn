number = int(input('ведите число'))
num = number
num2 = 0
while num > 0:
    digit = num % 10
    num = num // 10
    num2 = (num2 * 10) + digit
if not num2 - number:
    print ('палиндром')