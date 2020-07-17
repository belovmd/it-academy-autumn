num = int(input('число'))
a, b = 0, 1
for nums in range(num):
    print(a + b)
    a, b = b, (a + b)
