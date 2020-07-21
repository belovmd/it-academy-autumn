"""
MATRIX(CLOCKWISE)
https://www.codewars.com/kata/521c2db8ddc89b9b7a0000c1/python
Snail Sort
Given an n x n array, return the array elements arranged
from outermost elements to the middle element, traveling clockwise.
array = [[1,2,3],
         [4,5,6],
         [7,8,9]]
snail(array) #=> [1,2,3,6,9,8,7,4,5]

For better understanding, please follow the numbers
of the next array consecutively:

array = [[1,2,3],
         [8,9,4],
         [7,6,5]]
snail(array) #=> [1,2,3,4,5,6,7,8,9]
NOTE: The idea is not sort the elements from the lowest value to the highest;
the idea is to traverse the 2-d array in a clockwise snailshell pattern.
"""


def snail(snail_map):
    count = len(snail_map)
    loops_count = count - 1
    result_list = [] + snail_map[0]

    direction = 1
    i = 0
    j = loops_count

    while loops_count != 0:
        for _ in range(loops_count):
            i += direction
            result_list.append(snail_map[i][j])

        direction *= -1

        for _ in range(loops_count):
            j += direction
            result_list.append(snail_map[i][j])

        loops_count -= 1
    return result_list


array = [[1, 2, 3],
         [8, 9, 4],
         [7, 6, 5]]


print(snail(array))
