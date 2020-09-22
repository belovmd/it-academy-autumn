# Написать программу которая находит ближайшую степень двойки
# к введенному числу. 10(8), 20(16), 1(1), 13(16)

def pow_two(num):
    degree = 0
    while 1:
        diff = abs(num - (1 << degree))
        next_diff = abs(num - (1 << degree + 1))
        if next_diff > diff:
            break
        else:
            degree += 1
    return '{} - ближайшая степень двойки, ' \
           'Число - {}'. format(degree, 1 << degree)


print(pow_two(int(input('Введите число: '))))
