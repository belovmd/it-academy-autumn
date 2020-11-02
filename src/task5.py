"""
Каждый из N школьников некоторой школы знает Mi языков. Определите, какие
языки знают все школьники и языки, которые знает хотя бы один из школьников.
Входные данные
Первая строка входных данных содержит количество школьников N. Далее
идет N чисел Mi, после каждого из чисел идет Mi строк, содержащих названия
 языков, которые знает i-й школьник.
Пример входных данных:
3          # N количество школьников
2          # M1 количество языков первого школьника
Russian    # языки первого школьника
English
3          # M2 количество языков второго школьника
Russian
Belarusian
English
3
Russian
Italian
French
"""
lst = []
all_languages = []
any_languages = []
count_all_languages = 0
count_any_languages = 0
dct = {}
number_student = int(input())
for student in range(number_student):
    kol_languages = int(input())
    for language in range(kol_languages):
        languages = input()
        lst.append(languages)
for word in lst:
    dct[word] = dct.get(word, 0) + 1
for word in dct:
    if dct[word] == number_student:
        count_all_languages += 1
        all_languages.append(word)
    else:
        count_any_languages += 1
        any_languages.append(word)
print(count_all_languages)
for language in all_languages:
    print(language)
print(count_any_languages)
for language in any_languages:
    print(language)
