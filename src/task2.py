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
    cities_table = {}

    for string in list_of_input[1:int(list_of_input[0]) + 1]:
        country, *cities = string.split()
        for city in cities:
            cities_table[city] = cities_table.get(city, []).append(country)

    for string in list_of_input[int(list_of_input[0]) + 2:]:
        res_countries = cities_table.get(string.strip(), None)

        if res_countries:
            print(' '.join(res_countries))
        else:
            print('No')


if __name__ == '__main__':
    input_str = """4
    Russia Moscow Petersburg Novgorod Kaluga
    Ukraine Kiev Donetsk Odessa
    Belarus Brest Minsk
    France Brest Paris
    4
    Odessa
    Moscow
    Novgorod
    Brest"""
    country_of_city(input_str)
