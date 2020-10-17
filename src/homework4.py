def dict_comp():
    dct = {i: i ** 3 for i in range(1, 21)}
    print(dct)


def task7():
    num1 = 9
    num2 = 99

    while 1:
        if not num1 % num2:
            break
        else:
            num1, num2 = num2, num1 % num2

    print(num2)
