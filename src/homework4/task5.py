# Каждый из N школьников некоторой школы знает Miязыков.
# Определите, какие языки знают все школьники и языки,
# которые знает хотя бы один из школьников.
# Входные данные
# Первая строка входных данных содержит количество
# школьников N. Далее идет N чисел Mi, после каждого из
# чисел идет Mi строк, содержащих названия языков,
# которые знает i-й школьник. 
# Пример входных данных:
#     3          # N количество школьников
# 2          # M1 количество языков первого школьника
# Russian    # языки первого школьника
# English
# 3          # M2 количество языков второго школьника
# Russian
# Belarusian
# English
# 3
# Russian
# Italian
# French


stud_num = int(input('количество учеников?'))
dct_lngs = {}
for _ in range(stud_num):
    lngs_num = int(input('сколько языков знает товарищ?'))
    for lng in range(lngs_num):
        lng = input('собственно язык?')
        dct_lngs[lng] = dct_lngs.get(lng, 0) + 1
counter_all = 0
all_lst = []
counter_any = 0
any_lst = []
for key, value in dct_lngs.items():
    if value == stud_num:
        counter_all += 1
        all_lst.append(key)
    else:
       counter_any += 1
       any_lst.append(key)
print(counter_all)
for el in all_lst:
    print(el)
print(counter_any)
for el in any_lst:
    print(el)
