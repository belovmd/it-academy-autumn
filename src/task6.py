'''
6.Вводится число найти его максимальный делитель, являющийся степенью двойки. 10(2) 16(16), 12(4).
'''
v = int(input('enter the number:'))
a = 2
z = 0
while 1:
    if v == 0:
        break

    elif v%2 == 0:
        z+=1
        v = v/2

    elif v%2 != 0:
        break

print(2**z)






