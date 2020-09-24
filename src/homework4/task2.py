# Дан список стран и городов каждой страны. Затем даны названия городов.
#  Для каждого города укажите, в какой стране он находится.
# Входные данные
# Программа получает на вход количество стран N. Далее идет N строк, каждая
# строка начинается с названия страны, затем идут названия городов этой страны.
# В следующей строке записано число M, далее идут M запросов — названия
#  каких-то M городов, перечисленных выше.
# Выходные данные
# Для каждого из запроса выведите название страны, в котором находится город.
# Примеры
# Входные данные
# 2
# Russia Moscow Petersburg Novgorod Kaluga
# Ukraine Kiev Donetsk Odessa
# 3
# Odessa
# Moscow
# Novgorod

# Выходные данные
# Ukraine
# Russia
# Russia


num_cntrs = int(input())
cities_dct = {}
out_cntrs_lst = []
for _ in range(num_cntrs):
    country, *cities = input().split()
    for el in cities:
        cities_dct[el] = cities_dct.get(el, '') + country + ' '


num_cities = int(input())
for _ in range(num_cities):
    city = str(input())
    out_cntrs_lst += cities_dct.get(city).split()
print('\n'.join(el for el in out_cntrs_lst))
