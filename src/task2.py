"""
Дан список стран и городов каждой страны. Затем даны названия городов.
Для каждого города укажите, в какой стране он находится.
Входные данные
Программа получает на вход количество стран N. Далее идет N строк, каждая
строка начинается с названия страны, затем идут названия городов этой страны.
В следующей строке записано число M, далее идут M запросов — названия каких-то
M городов, перечисленных выше.
Выходные данные
Для каждого из запроса выведите название страны, в котором находится данный
город.
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


def country_of_city(str_):
    list_of_input = str_.split('\n')
    countries_cities = {}

    for string in list_of_input[1:int(list_of_input[0]) + 1]:
        list_of_country_and_its_cities = string.split()
        country = list_of_country_and_its_cities[0]
        cities = list_of_country_and_its_cities[1:]
        countries_cities[country] = cities

    for string in list_of_input[int(list_of_input[0]) + 2:]:
        res_countries = []
        for country in countries_cities:
            if string.strip() in countries_cities[country]:
                res_countries.append(country)
        if res_countries:
            for country in res_countries:
                print(country, end=' ')
            print()
        else:
            print('No')


if __name__ == '__main__':
    input_str = """2
    Russia Moscow Petersburg Novgorod Kaluga
    Ukraine Kiev Donetsk Odessa
    4
    Odessa
    Moscow
    Novgorod
    Kiev"""
    country_of_city(input_str)
