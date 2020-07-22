def palindrom(n):

    divisor = 10
    digits = 1
    is_palindrome = True

    while n // divisor:
        digits += 1
        divisor *= 10

    for i in range(1, int((digits / 2) + 1)):
        first_digit = n % (10 ** (digits - i + 1)) // (10 ** (digits - i))
        last_digit = (n % 10 ** i) // 10 ** (i - 1)
        if first_digit != last_digit:
            is_palindrome = False

    return is_palindrome


if __name__ == "__main__":
    # здесь можно сделать ввод из консоли и проверить работу функции
    n = 0
    print(palindrom(n))
