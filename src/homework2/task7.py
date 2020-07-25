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
nums = [[int(0) for j in range(d)] for i in range(d)]
r = 1
a = d
while a > 0:
    for i in range(r - 1, r):
        for j in range(r - 1, a):
            nums[i][j] = nums[i][j - 1] + 1
    for j in range(a - 1, a - 2, -1):
        for i in range(r, a):
            nums[i][j] = nums[i - 1][j] + 1
    for i in range(a - 1, a - 2, -1):
        for j in range(a - 2, r - 2, -1):
            nums[i][j] = nums[i][j + 1] + 1
    for j in range(r - 1, r - 2, -1):
        for i in range(a - 2, r - 1, -1):
            nums[i][j] = nums[i + 1][j] + 1
    a -= 1
    r += 1
for row in nums:
    print(' '.join([str(elem) for elem in row]))
