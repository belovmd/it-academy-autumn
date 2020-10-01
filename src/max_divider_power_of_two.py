def max_divider(num):
    num = abs(num)
    result = 1
    power = 2
    while power <= num:
        if not num % power:
            result = power
        power <<= 1
    return result


if __name__ == '__main__':
    print(max_divider(10))
    print(max_divider(-16))
    print(max_divider(16))
    print(max_divider(12))
    print(max_divider(-10))
    print(max_divider(1))
    print(max_divider(-12))
