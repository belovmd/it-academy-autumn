"""
Реализовать функцию get_ranges которая получает на вход непустой список
неповторяющихся целых чисел, отсортированных по возрастанию,
которая этот список “сворачивает”
get_ranges([0, 1, 2, 3, 4, 7, 8, 10]) // "0-4,7-8,10"
get_ranges([4,7,10]) // "4,7,10"
get_ranges([2, 3, 8, 9]) // "2-3,8-9"
"""


def get_ranges(lst):
    """Перевернув лист я записываю границы последовательностей

    n n + 1

    во вложенном while я проверяю, если сл число является последовательностью,

    то я меняю границу. Затем записываю в ответ эти границы.

    :param lst:
    :return: str
    """
    lst = lst[::-1]
    answer = ''
    while lst:
        first = lst.pop()
        last = first
        while lst and lst[-1] - last == 1:
            last = lst.pop()

        answer += f'{first}-{last},' if first != last else f'{first},'
    print(lst)
    return answer.rstrip(',')


def main():
    lst = [0, 1, 2, 3, 4, 7, 8, 10]
    print(get_ranges(lst))



if __name__ == '__main__':
    main()
