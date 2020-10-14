# Вводится число найти его максимальный делитель,
# являющийся степенью двойки. 10(2) 16(16), 12(4).


num = int(input())
power_2 = 2 << len(bin(num)) - 3

while num:
    power_2 >>= 1
    num = num % power_2

if power_2 == 1:
    print('no suitable divisor found')
else:
    print(power_2)
