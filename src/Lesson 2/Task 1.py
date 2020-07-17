input_variable = int(input("Введите n: "))

if input_variable < 1:
    print("Число не может быть меньше единицы!")
else:
    for i in range(1, input_variable + 1):
        print(i ** 3)
