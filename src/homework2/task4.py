def count_letters(str_):
    low_number = 0
    up_number = 0
    for char in str_:
        if char.isupper():
            up_number += 1
        elif char.islower():
            low_number += 1

    return (low_number, up_number)


if __name__ == "__main__":
    # здесь можно сделать ввод из консоли и проверить работу функции
    str_ = "9867565443789ASDFS{}DGSDFGSFDG sdf g"
    print(count_letters(str_))
