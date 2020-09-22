"""
Во входной строке записан текст. Словом считается
последовательность непробельных символов идущих подряд,
слова разделены одним или большим числом пробелов или
символами конца строки. Определите, сколько различных
слов содержится в этом тексте.
"""
text = """To be or not to be?Hello world.   and everybody.
 Welcome to the course!"""
replace_symbols = text.maketrans('.,:;!?', '      ')
changed_text = text.translate(replace_symbols)
lst = []
for word in changed_text.lower().split():
    if word not in lst:
        lst.append(word)
print(lst)
print(len(lst))
