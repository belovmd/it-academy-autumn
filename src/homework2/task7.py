"""
1) Найти индекс такого элемента,
где сумма всех элементов справа и слева равна.
Если такого элемента нет - вернуть -1.

:param arr: список элементов
:return: индекс элемента

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

:param string: Строка со скобками
:return: True, False

Пример:
"()"              =>  true
")(()))"          =>  false
"("               =>  false
"(())((()())())"  =>  true
"""


def valid_parentheses(string):

    parentheses = {
        '(': ')',
        '{': '}',
        '[': ']',
        '<': '>',
    }

    close_parentheses = parentheses.values()

    stack = []

    for prnth in string:
        if prnth in parentheses:
            stack.append(prnth)
        elif not (len(stack) and parentheses[stack.pop()] == prnth):
            return False

    return len(stack) == 0


"""
Шифрование.
Взять четные символы в строке
и соединить с нечетными символами в строке
n-ое кол-во раз.
Сделать шифратор и дешифратор.

:param text: текст для шифрования
:param n: кол-во итераций
:return: Зашифрованный или расшифрованный текст

Пример:
"This is a test!", 1 -> "hsi  etTi sats!"
"This is a test!", 2 -> "hsi  etTi sats!" -> "s eT ashi tist!"
"""


def decrypt(text, n):
    if text in ("", None):
        return text

    text_center = len(text) // 2

    for i in range(n):
        left_part = text[:text_center]
        right_part = text[text_center:]
        text = ""
        for ch_id in range(text_center + 1):
            text = "".join(right_part[ch_id:ch_id + 1] + left_part[ch_id:ch_id + 1])

    return text


def encrypt(text, n):
    for i in range(n):
        text = text[1::2] + text[::2]

    return text


"""
Составить стисок с элементами из дерева,
отсортированными по уровням.

:param node: корень дерева
:return: Список элементов дерева, отсортированных по уровням

Структура дерева:
    class Node:
    def __init__(self, L, R, n):
        self.left = L
        self.right = R
        self.value = n

Пример:

    Дерево:
              2
         8         9
       1   3     4   5

    Результат:
        [2,8,9,1,3,4,5]
"""


# рекурсия
def tree_by_levels(node):
    result_dct = {}

    def next_lvl(tree_node, lvl_number):
        if node is None:
            return
        result_dct.setdefault(lvl_number, []).append(tree_node.value)
        next_lvl(tree_node.left, lvl_number + 1)
        next_lvl(tree_node.right, lvl_number + 1)

    next_lvl(node, 0)
    result = []

    for i in range(len(result_dct)):
        result += result_dct[i]

    return result
