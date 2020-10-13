# Написать программу которая находит ближайшую степень
# двойки к введенному числу. 10(8), 20(16), 1(1), 13(16)


num = bin(int(input()))[2::]

if int(num, 2) == 1:
    output = 2
elif num[1] == '1':
    output = 2 << len(num) - 1
else:
    output = 2 << len(num) - 2
print(output)