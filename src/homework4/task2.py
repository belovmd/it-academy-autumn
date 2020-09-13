"""
Дан список стран и городов каждой страны.
Затем даны названия городов. Для каждого города укажите,
в какой стране он находится.
Входные данные
Программа получает на вход количество стран N.
Далее идет N строк, каждая строка начинается с названия страны,
затем идут названия городов этой страны. В следующей строке записано число M,
далее идут M запросов — названия каких-то M городов, перечисленных выше.
Выходные данные
Для каждого из запроса выведите название страны,
в котором находится данный город.

2
Russia Moscow Petersburg Novgorod Kaluga
Ukraine Kiev Donetsk Odessa Moscow

3
Odessa
Moscow
Novgorod

"""


def get_int_number():
    while 1:
        count = input()
        if count.isdigit():
            return int(count)
        else:
            print("Enter number")


def get_database(count_of_lines):
    result_dict = {}
    for _ in range(count_of_lines):
        country, *cities = str(input()).split()
        for city in cities:
            result_dict.setdefault(city, {country}).add(country)
    return result_dict


def match_countries():
    count = get_int_number()
    database = get_database(count)

    print(database)
    number_of_requests = get_int_number()
    for _ in range(number_of_requests):
        matched_countries = database.get(input())
        print(','.join(matched_countries) if matched_countries
              else "Not found")


match_countries()
