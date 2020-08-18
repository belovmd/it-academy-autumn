# Уникальные элементы в списке
# Дан список. Выведите те его элементы,
# которые встречаются в списке только один раз.
# Элементы нужно выводить в том порядке, в котором они встречаются в списке.

numbers = [int(i) for i in input().split()]
for i in range(len(numbers)):
    for j in range(len(numbers)):
        if i != j and numbers[i] == numbers[j]:
            break
    else:
        print(numbers[i], end=' ')
