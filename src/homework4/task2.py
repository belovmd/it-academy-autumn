"""
Дан список стран и городов каждой страны. Затем даны названия городов.
Для каждого города укажите, в какой стране он находится.
Входные данные
Программа получает на вход количество стран N.
Далее идет N строк, каждая строка начинается с названия страны,
затем идут названия городов этой страны. В следующей строке записано число M,
далее идут M запросов — названия каких-то M городов, перечисленных выше.
Выходные данные
Для каждого из запроса выведите название страны,
в котором находится данный город.
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


def cities():
    cities_collection = {}
    for _ in range(int(input())):
        country, *cities = input().split()
        for city in cities:
            cities_collection[city] = country
    for _ in range(int(input())):
        print(cities_collection[input()])


def cities_with_similar():
    countries = {}
    for _ in range(int(input())):
        country, *cities = input().split()
        countries[country] = cities
    for _ in range(int(input())):
        city = input()
        for key, value in countries.items():
            if city in value:
                print(key)
                break


if __name__ == '__main__':
    cities_with_similar
    cities()
