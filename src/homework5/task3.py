# Реализовать функцию get_ranges которая получает на вход
# непустой список неповторяющихся целых чисел,
# отсортированных по возрастанию, которая этот список “сворачивает”
#  get_ranges([0, 1, 2, 3, 4, 7, 8, 10]) // "0-4,7-8,10"
#  get_ranges([4,7,10]) // "4,7,10"
#  get_ranges([2, 3, 8, 9]) // "2-3,8-9"


def get_ranges(numbers):
    input_list = []
    output_list = []
    for el in numbers:
        if el + 1 not in numbers:
            output_list.append(el)
            input_list.append(output_list.copy())
            output_list.clear()
        else:
            output_list.append(el)

    for el in input_list:
        if len(el) >= 2:
            el = [el[0], '-', el[-1]]
        output_list.append(''.join(str(i) for i in el))

    return ','.join(output_list)


print(get_ranges([0, 1, 2, 3, 4, 7, 8, 10]))
