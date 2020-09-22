"""
Города
Дан список стран и городов каждой страны. Затем даны названия
 городов. Для каждого города укажите, в какой стране он находится.
Входные данные
Программа получает на вход количество стран N. Далее идет N строк,
 каждая строка начинается с названия страны, затем идут названия
  городов этой страны. В следующей строке записано число M, далее
   идут M запросов — названия каких-то M городов, перечисленных выше.
Выходные данные
Для каждого из запроса выведите название страны, в котором находится
 данный город.
Примеры

Входные данные
2
Russia Moscow Petersburg Novgorod Kaluga
Ukraine Kiev Donetsk Odessa

3
Odessa
Moscow
Novgorod

Выходные данные
Ukraine
Russia
Russia

"""
dct = {}
count_lines = int(input())
lst_countries = []
for line in range(count_lines):
    line = input().split()
    var = {word: line[0] for word in line[1:]}
    dct.update(var)
count_cities = int(input())
for city in range(count_cities):
    city = input()
    lst_countries.append(dct.get(city))
for country in lst_countries:
    print(country)
