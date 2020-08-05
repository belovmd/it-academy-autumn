"""
You are given an array (which will have a length of at least 3, but could be very large) containing
integers. The array is either entirely comprised of odd integers or entirely comprised of even
integers except for a single integer N. Write a method that takes the array as an argument
and returns this "outlier" N.
https://www.codewars.com/kata/5526fc09a1bbd946250002dc
"""


def find_outlier(integers):
    if integers[0] % 2 == integers[1] % 2:
        odd = integers[0] % 2
        for i in integers[2:]:
            if i % 2 != odd:
                return i
    return integers[0] if integers[0] % 2 != integers[2] % 2 else integers[1]


"""
Is similar to factorial of a number, In primorial, not all the natural numbers get multiplied,
only prime numbers are multiplied to calculate the primorial of a number. It's denoted with P# and
it is the product of the first n prime numbers.
https://www.codewars.com/kata/5a99a03e4a6b34bb3c000124
"""


def num_primorial(n):
    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23]
    res = 1
    k = primes[-1] + 2
    while len(primes) < n:
        for prime in primes:
            if k % prime == 0:
                k += 2
                break
        else:
            primes.append(k)
            k += 2

    for i in primes[:n]:
        res *= i

    return res
