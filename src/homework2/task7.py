"""
1) Найти индекс такого элемента,
где сумма всех элементов справа и слева равна.
Если такого элемента нет - вернуть -1.
"""


def find_even_index(arr):

    left_sum, right_sum = 0, sum(arr)

    for i, e in enumerate(arr):
        right_sum -= e
        if left_sum == right_sum:
            return i
        left_sum += e

    return -1


"""
2) Функция вычисляет кол-во
открытых и закрытых круглых скобок.
Возвращает True если кол-во
открывающих и закрывающих скобок равно,
и если они идут в правильном порядке.
Иначе False.

Пример:
"()"              =>  true
")(()))"          =>  false
"("               =>  false
"(())((()())())"  =>  true
"""


def valid_parentheses(string):
    counter = 0

    for ch in string:
        if ch == '(':
            counter += 1
        if ch == ')':
            counter -= 1
        if counter < 0:
            return False

    return counter == 0


"""
Шифрование.
Взять четные символы в строке
и соединить с нечетными символами в строке
n-ое кол-во раз.
Сделать шифратор и дешифратор.

Пример:
"This is a test!", 1 -> "hsi  etTi sats!"
"This is a test!", 2 -> "hsi  etTi sats!" -> "s eT ashi tist!"
"""


def decrypt(text, n):
    if text in ("", None):
        return text

    center = len(text) // 2

    for i in range(n):
        left = text[:center]
        right = text[center:]
        text = "".join(right[i:i + 1] + left[i:i + 1] for i in range(center + 1))

    return text


def encrypt(text, n):
    for i in range(n):
        text = text[1::2] + text[::2]

    return text
