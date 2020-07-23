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
