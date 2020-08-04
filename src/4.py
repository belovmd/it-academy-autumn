"""
Fibonacci, tuple assignment
Print fib numbers until result < 100
"""


parents, babies = (1, 1)
while babies < 100:
    print('This generation has {0} babies'.format(babies))
    parents, babies = (babies, parents + babies)
