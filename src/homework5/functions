def text_founder():
    import re
    text = 'gfijhf,fkdhk v  kgd,kjfg ,lflksf.'
    result = re.findall(r'\w+', text)
    return len(result)


def fizz_buzz():
    return [('Fizz' * (not el % 3) + 'Buzz' * (not el % 5) or el)
            for el in range(1, 101)]


def zeros_to_the_right():
    lst = [1, 2, 0, 4, 3, 0, 0, 4, 3, 0, 6, 6, 0, 0, 7, 4, 8, 0, 9, 10]
    for el in lst:
        if el == 0:
            lst.append(lst.pop(lst.index(el)))
    return lst
