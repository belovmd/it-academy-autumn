# Во входной строке записан текст. Словом считается
# последовательность непробельных символов идущих подряд,
# слова разделены одним или большим числом пробелов или
# символами конца строки. Определите, сколько различных
# слов содержится в этом тексте


text = 'gfijhf,fkdhk v  kgd,kjfg ,lflksf.'
count = 0
for el in range(1, len(text)):
    if el == 1 and text[0].isalpha():
        count += 1
    elif text[el].isalpha() and not text[el - 1].isalpha():
        count += 1
    else:
        continue
print(count)
