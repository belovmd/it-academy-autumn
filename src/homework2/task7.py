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

"""
https://www.codewars.com/kata/5a99a03e4a6b34bb3c000124/train/python
Definition (Primorial Of a Number)
Is similar to factorial of a number, In primorial,
not all the natural numbers get multiplied, only prime numbers are
multiplied to calculate the primorial of a number.
It's denoted with P# and it is the product
of the first n prime numbers.

numPrimorial (3) ==> return (30)
numPrimorial (5) ==> return (2310)
numPrimorial (6) ==> return (30030)
"""


def is_prime(curr_num):
    for num in range(2, curr_num // 2 + 1):
        if curr_num % num == 0:
            return False
    return True


def num_primorial(n):
    result = 2
    next_prime = 3
    count = 1
    while count != n:
        if is_prime(next_prime):
            count += 1
            result *= next_prime
        next_prime += 1

    return result


print(num_primorial(6))
