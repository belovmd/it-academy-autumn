def sub_string(str_):
    clean_string = ""
    for char in str_:
        if char not in clean_string and char != " ":
            clean_string += char
    return f"{clean_string}"


if __name__ == "__main__":
    # здесь можно сделать ввод из консоли и проверить работу функции
    str_ = "asdfasdfadsf           s fd"
    print(sub_string(str_))
