# #1 https://www.codewars.com/kata/53d40c1e2f13e331fc000c26
# def pow(A, n, I, multiply):
#     """
#     Возвращает x в степени n. Предполагает, что I – это единичная матрица, которая
#     перемножается с mult, а n – положительное целое
#     """
#     if n == 0:
#         return I
#     elif n == 1:
#         return A
#     elif n % 2:
#         return multiply(pow(A, n - 1, I, multiply), A)
#     else:
#         B = pow(A, n // 2, I, multiply)
#         return multiply(B, B)
#
# def matrix_multiply(A, B):
#     BT = list(zip(*B))
#     return [[sum(a * b
#                  for a, b in zip(row_a, col_b))
#             for col_b in BT]
#             for row_a in A]
#
# def fib(n):
#     print(abs(n))
#     F = pow([[1, 1], [1, 0]], abs(n), [[1, 0], [0, 1]], matrix_multiply)
#     return -F[0][1] if n < 0 and not n % 2 else F[0][1]

# #2 https://www.codewars.com/kata/5667e8f4e3f572a8f2000039
# def accum(s):
#     return '-'.join([char.upper() + char.lower() * i for i, char in enumerate(s)])

# # 3 https://www.codewars.com/kata/54da5a58ea159efa38000836
# def find_it(seq):
#     for i in set(seq):
#         if seq.count(i) % 2:
#             return i

# # 4 https://www.codewars.com/kata/514b92a657cdc65150000006
# def solution(number):
#     return sum([i for i in range(number) if not i % 3 or not i % 5])



if __name__ == '__main__':

    print(solution(10))
