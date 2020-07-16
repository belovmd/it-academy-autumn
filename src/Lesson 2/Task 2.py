input_variable = int(input("Введите n: "))

if input_variable <= 1:
    print("Число должно быть меньше единицы")
    quit()

for factor in range(2, int(input_variable ** 0.5 + 1)):
    if not input_variable % factor:
        print(str(input_variable) + " - составное число")
        quit()

print(str(input_variable) + " - простое число")
