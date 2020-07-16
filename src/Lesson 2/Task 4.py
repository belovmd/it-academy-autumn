a = 0
b = 1
input_variable = int(input("Введите n: "))

if input_variable < 0:
    print("Must be positive, transforming: ")
    input_variable *= -1
elif input_variable < 1:
    print("Must be above 1!")
    quit()

for i in range(input_variable):
    a, b = b, (a + b)
    print(a)
