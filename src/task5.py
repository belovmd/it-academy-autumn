'''
5.Написать программу которая находит ближайшую степень двойки к введенному числу. 10(8), 20(16), 1(1), 13(16)
'''
v = int(input('enter the number:'))
a = 2
z = 0
num = 1
i =1
while 1:
    if a**i > v:
        if v - a**(i-1) < a**i - v:
            print(a**(i-1))
            break
        elif v - a**(i-1) > a**i - v:
            print(a**i)
            break
    i+=1






