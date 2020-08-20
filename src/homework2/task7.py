'''вводится число n. далее 4 слова;
#вывести кол-во непровторяющихся слов 1 строчкой
#второй строчкой столько раз повторяется каждое слово'''
n = int(input())
words = []
count = []
total_count = 0
for i in range(n):
    words += input('word?').split()
while len(words) > 0:
    count.append(words.count(words[0]))
    str0 = words[0]
    for i in range(words.count(words[0])):
        words.remove(str0)
    total_count += 1
print(total_count)
print(' '.join(str(a) for a in count))

""" Выведите таблицу размером d*d,
заполненную числами от 1 до d^2d
 по спирали, выходящей из левого
верхнего угла и закрученной по часовой стрелке,"""
d = int(input())
matrix = [[int(0) for column in range(d)] for row in range(d)]
row_start = 1
row_end = d
while row_end > 0:
    for row in range(row_start - 1, row_start):
        for column in range(row_start - 1, row_end):
            matrix[row][column] = matrix[row][column - 1] + 1
    for columns in range(row_end - 1, row_end - 2, -1):
        for row in range(row_start, row_end):
            matrix[row][columns] = matrix[row - 1][columns] + 1
    for row in range(row_end - 1, row_end - 2, -1):
        for columns in range(row_end - 2, row_start - 2, -1):
            matrix[row][columns] = matrix[row][columns + 1] + 1
    for column in range(row_start - 1, row_start - 2, -1):
        for row in range(row_end - 2, row_start - 1, -1):
            matrix[row][column] = matrix[row + 1][column] + 1
    row_end -= 1
    row_start += 1
for rows in matrix:
    print(' '.join([str(elem) for elem in rows]))
