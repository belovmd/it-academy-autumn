# 1 https://www.codewars.com/kata/53d40c1e2f13e331fc000c26
"""
In this kata you will have to calculate fib(n) where:

fib(0) := 0
fib(1) := 1
fin(n + 2) := fib(n + 1) + fib(n)
Write an algorithm that can handle n up to 2000000.

Your algorithm must output the exact integer answer, to full precision.
Also, it must correctly handle negative numbers as input.

HINT I: Can you rearrange the equation fib(n + 2) = fib(n + 1) + fib(n)
to find fib(n) if you already know fib(n + 1) and fib(n + 2)?
Use this to reason what value fib has to have for negative values.
"""


def pow(matrix_a, n, identity_matrix, mult):
    if n == 0:
        return identity_matrix
    elif n == 1:
        return matrix_a
    elif n % 2:
        return mult(pow(matrix_a, n - 1, identity_matrix, mult), matrix_a)
    else:
        matrix_b = pow(matrix_a, n // 2, identity_matrix, mult)
        return mult(matrix_b, matrix_b)


def matrix_multiply(matrix_a, matrix_b):
    transposed_matrix_b = list(zip(*matrix_b))
    return [[sum(a * b
                 for a, b in zip(row_a, col_b))
            for col_b in transposed_matrix_b]
            for row_a in matrix_a]


def fib(n):
    print(abs(n))
    f = pow([[1, 1], [1, 0]], abs(n), [[1, 0], [0, 1]], matrix_multiply)
    return -f[0][1] if n < 0 and not n % 2 else f[0][1]


# 2 https://www.codewars.com/kata/5667e8f4e3f572a8f2000039
'''
This time no story, no theory. The examples below show you how to write
function accum:

Examples:

accum("abcd") -> "A-Bb-Ccc-Dddd"
accum("RqaEzty") -> "R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy"
accum("cwAt") -> "C-Ww-Aaa-Tttt"
'''


def accum(s):
    return '-'.join([c.upper() + c.lower() * i for i, c in enumerate(s)])


# 3 https://www.codewars.com/kata/54da5a58ea159efa38000836
'''
Given an array, find the integer that appears an odd number of times.

There will always be only one integer that appears an odd number of times.
'''


def find_it(seq):
    nums = {}
    for num in seq:
        nums[num] = nums.get(num, 0) + 1
    for key, value in nums.items():
        if value % 2:
            return key



# 4 https://www.codewars.com/kata/514b92a657cdc65150000006
'''
If we list all the natural numbers below 10
that are multiples of 3 or 5, we get 3, 5, 6 and 9.
The sum of these multiples is 23.

Finish the solution so that it returns the sum of all the multiples
of 3 or 5 below the number passed in.
'''


def solution(number):
    return sum([i for i in range(number) if not i % 3 or not i % 5])


# 5 https://www.codewars.com/kata/513e08acc600c94f01000001
'''
The rgb function is incomplete.
Complete it so that passing in RGB decimal values will result
in a hexadecimal representation being returned.
Valid decimal values for RGB are 0 - 255.
Any values that fall out of that range must be rounded
to the closest valid value.
The following are examples of expected output values:

rgb(255, 255, 255) # returns FFFFFF
rgb(255, 255, 300) # returns FFFFFF
rgb(0,0,0) # returns 000000
rgb(148, 0, 211) # returns 9400D3
'''


def rgb(r, g, b):
    r = r if 256 > r >= 0 else 0 if r < 0 else 255
    g = g if 256 > g >= 0 else 0 if g < 0 else 255
    b = b if 256 > b >= 0 else 0 if b < 0 else 255
    return ('{:02X}' * 3). format(r, g, b)
