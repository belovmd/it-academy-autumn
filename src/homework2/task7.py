# 1 https://www.codewars.com/kata/53d40c1e2f13e331fc000c26
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
def accum(s):
    return '-'.join([c.upper() + c.lower() * i for i, c in enumerate(s)])


# 3 https://www.codewars.com/kata/54da5a58ea159efa38000836
def find_it(seq):
    for i in set(seq):
        if seq.count(i) % 2:
            return i


# 4 https://www.codewars.com/kata/514b92a657cdc65150000006
def solution(number):
    return sum([i for i in range(number) if not i % 3 or not i % 5])


# 5 https://www.codewars.com/kata/513e08acc600c94f01000001
def rgb(r, g, b):
    r = r if 256 > r >= 0 else 0 if r < 0 else 255
    g = g if 256 > g >= 0 else 0 if g < 0 else 255
    b = b if 256 > b >= 0 else 0 if b < 0 else 255
    return ('{:02X}' * 3). format(r, g, b)
