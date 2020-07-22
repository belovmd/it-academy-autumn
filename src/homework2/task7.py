# https://www.codewars.com/kata/5526fc09a1bbd946250002dc
def find_outlier(integers):
    if integers[0] % 2 == integers[1] % 2:
        odd = integers[0] % 2
        for i in integers[2:]:
            if i % 2 != odd:
                return i
    return integers[0] if integers[0] % 2 != integers[2] % 2 else integers[1]


# https://www.codewars.com/kata/5a99a03e4a6b34bb3c000124
def num_primorial(n):
    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23]
    res = 1
    k = primes[-1] + 2
    while len(primes)<n:
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
