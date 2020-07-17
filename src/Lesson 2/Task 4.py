a, b = 0, 1

input_variable = int(input("Введите n: "))

if input_variable < 0:
    print("Число не может быть отрицательным, преобразовываем: ")
    input_variable *= -1
elif input_variable < 1:
    print("Число не может быть меньше единицы!")
    quit()

for i in range(input_variable):
    a, b = b, (a + b)
    print(a)
