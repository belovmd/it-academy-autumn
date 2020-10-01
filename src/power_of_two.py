def get_max_power_of_two(num):
    prev, curr = 0, 1
    while curr < num:
        prev, curr = curr, curr << 1
    return curr if curr - num < num - prev else prev


if __name__ == '__main__':
    print(get_max_power_of_two(2))
    print(get_max_power_of_two(10))
    print(get_max_power_of_two(20))
    print(get_max_power_of_two(1))
    print(get_max_power_of_two(13))
    print(get_max_power_of_two(32))
    print(get_max_power_of_two(128))
    print(get_max_power_of_two(1024))
