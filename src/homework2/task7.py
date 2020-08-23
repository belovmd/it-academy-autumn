'''вводится число n. далее 4 слова;
#вывести кол-во непровторяющихся слов 1 строчкой
#второй строчкой столько раз повторяется каждое слово'''


words = [input('word?') for i in range(int(input('how much words?')))]
word_repeat = []
total_count = 0
used_words = []
for word in words:
    if word not in used_words:
        word_repeat.append(words.count(word))
        used_words.append(word)
        total_count += 1
    else:
        continue
print(total_count)
print(' '.join(str(a) for a in word_repeat))


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

'''Given: an array containing hashes of names
Return: a string formatted as a list of names separated
by commas except for the last two names, which should be separated by
an ampersand.
Example:
namelist([ {'name': 'Bart'}, {'name': 'Lisa'}, {'name': 'Maggie'} ])
# returns 'Bart, Lisa & Maggie'
namelist([ {'name': 'Bart'}, {'name': 'Lisa'} ])
# returns 'Bart & Lisa'
namelist([ {'name': 'Bart'} ])
# returns 'Bart'
namelist([])
https://www.codewars.com/kata/53368a47e38700bd8300030d'''


def namelist(namelist):
    lst = ''
    if not namelist:
        return lst
    else:
        for names in namelist:
            if names is namelist[-1]:
                lst += names.get('name')
            elif names is namelist[-2]:
                lst += names.get('name') + ' & '
            else:
                lst += names.get('name') + ', '
        print(lst)


'''The new "Avengers" movie has just been released! There are a lot of people
at the cinema box office standing in a huge line. Each of them has a single
100, 50 or 25 dollar bill. An "Avengers" ticket costs 25 dollars.
Vasya is currently working as a clerk. He wants to sell a ticket to every
single person in this line.
Can Vasya sell a ticket to every person and give change if he initially has no
money and sells the tickets strictly in the order people queue?
Return YES, if Vasya can sell a ticket to every person and give change with the
bills he has at hand at that moment. Otherwise return NO.
Examples:
tickets([25, 25, 50]) # => YES
tickets([25, 100]) # => NO. Vasya will not have enough money to give change to
100 dollars
tickets([25, 25, 50, 50, 100]) # => NO. Vasya will not have the right bills to
give 75 dollars of change (you can't make two bills of 25 from one of 50)
https://www.codewars.com/kata/555615a77ebc7c2c8a0000b8'''


def tickets(n):
    doll25 = 0
    doll50 = 0
    for num in n:
        if num == 25:
            doll25 += 1
        elif num == 50:
            if doll25 < 1:
                return "NO"
                break
            else:
                doll25 -= 1
                doll50 += 1
        elif num == 100:
            if doll25 > 0 and doll50 > 0:
                doll25 -= 1
                doll50 -= 1
            elif doll25 > 2:
                doll25 -= 3
            else:
                return "NO"
                break
    else:
        return "YES"
