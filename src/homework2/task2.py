import re


def longest_word(str_):
    current_longest = ""
    temp_storage = re.findall(r"[a-zA-Z]+", str_)
    for word in temp_storage:
        if len(word) > len(current_longest):
            current_longest = word
    return current_longest


if __name__ == "__main__":
    # здесь можно сделать ввод из консоли и проверить работу функции
    str_ = "fatal: you must specify path(s) to restore"
    print(longest_word(str_))
