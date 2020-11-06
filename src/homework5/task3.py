"""
Реализовать функцию get_ranges которая получает на вход
непустой список неповторяющихся целых чисел, отсортированных
по возрастанию, которая этот список “сворачивает”
"""


def get_packed_block(start, array):
    index = start
    prev_el = array[index]
    result_array = [prev_el]
    while 1:
        index += 1
        if index == len(array) or array[index] != prev_el + 1:
            break
        prev_el = array[index]
        result_array.append(prev_el)
    return (result_array, index)


def block_to_string(array):
    if len(array) == 1:
        return str(array[0])
    else:
        return "{first} - {last}".format(first=array[0],
                                         last=array[-1])


def zipped_string(array):
    index = 0
    result_array = []
    while index != len(array):
        block, index = get_packed_block(index, array)
        result_array.append(block_to_string(block))
    print(",".join(result_array))


zipped_string([0, 1, 2, 3, 4, 7, 8, 10])
zipped_string([4, 7, 8, 10])
zipped_string([10])
