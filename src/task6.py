"""
Вводится число найти его максимальный делитель,
являющийся степенью двойки. 10(2) 16(16), 12(4).
"""


def deliver_of_tw(num):
    prev = 1
    next_ = 2

    if num == 1:
        return 1

    while next_ <= num:
        if not num % next_:
            prev = next_
        next_ <<= 1
    return prev


print(deliver_of_tw(12))
