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
for _ in range(num_cntrs):
    city_lst = input().split()
    temp_dct = {el: city_lst[0] for el in city_lst[1:]}
    cities_dct.update(temp_dct)
num_cities = int(input())
for _ in range(num_cities):
    city = str(input())
    print(cities_dct.get(city))
