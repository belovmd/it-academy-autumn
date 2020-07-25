"""
Заполнить матрицу размером 8×8 нулями
и единицами таким образом, чтобы сумма
всех элементов матрицы была равна 8,
при этом сумма элементов ни в одном столбце,
строке или диагональном ряде матрицы не превышала единицы.
"""

BOARD_SIZE = 8


class BailOut(Exception):
    pass


def validate(queens):
    left = right = col = queens[-1]
    for r in reversed(queens[:-1]):
        left, right = left - 1, right + 1
        if r in (left, col, right):
            raise BailOut


def add_queen(queens):
    for i in range(BOARD_SIZE):
        test_queens = queens + [i]
        try:
            validate(test_queens)
            if len(test_queens) == BOARD_SIZE:
                return test_queens
            else:
                return add_queen(test_queens)
        except BailOut:
            pass
    raise BailOut


result = add_queen([])
print(result)
print("\n".join(". " * q + "Q " + ". " * (BOARD_SIZE - q - 1) for q in result))
