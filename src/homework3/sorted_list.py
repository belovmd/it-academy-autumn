# Упорядоченный список.
# Дан список целых чисел. Требуется переместить все ненулевые элементы
# в левую часть списка, не меняя их порядок, а все нули - в правую часть.
# Порядок ненулевых элементов изменять нельзя,
# дополнительный список использовать нельзя,
# задачу нужно выполнить за один проход по списку.
# Распечатайте полученный список.

list_ = [int(i) for i in input().split()]
for i in range(len(list_)):
    if not list_[i]:
        list_.append(list_.pop(i))
print(list_)
