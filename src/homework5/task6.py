# Вводится число найти его максимальный делитель,
# являющийся степенью двойки. 10(2) 16(16), 12(4).


def pow_two(num):
    div = 1
    max_div = 1

    while 1:
        div = div << 1
        if num % div:
            break

        max_div = div

    return '{} - Max делитель, степень 2'.format(max_div)


print(pow_two(int(input('Введите число: '))))
