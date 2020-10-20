# -*- coding: utf-8 -*-
import re
import sys
import codecs

sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())
# В файле хранятся данные с сайта IMDB.
# Скопированные данные хранятся в файле ./data/ ratings.list.
# Откройте и прочитайте файл(если его нет необходимо вывести ошибку).
# Найдите ТОП250 фильмов и извлеките заголовки.
# Программа создает 3 файла  top250_movies.txt – названия файлов,
# ratings.txt – гистограмма рейтингов, years.txt – гистограмма годов.


def top_movies(count):
    movies = []
    found_top_n_header = False
    try:
        with open('ratings.list', errors='ignore') as content:
            for line in content:
                if found_top_n_header:
                    if not count:
                        break
                    line = re.sub(r'\s+', ' ', line.strip())
                    movies.append(line)
                    count -= 1

                if line.strip() == 'New  Distribution  Votes  Rank  Title':
                    found_top_n_header = True
    except OSError:
        print('Файд не найден!')
        return None

    return movies


def save_list(filename, lst):
    with open(filename, 'w') as file:
        for line in lst:
            file.write(line + '\n')


def chart_bar(filename, chart):
    with open(filename, 'w') as file:
        for key, value in chart.items():
            file.write(key + '\t\t' + '#' * value + '\n')


def movie_names(movies):
    names = []

    for line in movies:
        name = line.split(' ', 3)[-1]
        name = name[:name.rfind('(') - 1]

        names.append(name)

    return names


def rating_bar(movies):
    chart = {}

    for line in movies:
        rating = line.split(' ')[2]
        chart[rating] = chart.get(rating, 0) + 1

    return chart


def year_bar(movies):
    chart = {}

    for line in movies:
        year = line[line.rfind('(') + 1: line.rfind(')')]
        chart[year] = chart.get(year, 0) + 1

    sorted_year = list(chart.keys())
    sorted_year.sort(reverse=False)

    return {year: chart[year] for year in sorted_year}


movies_lst = top_movies(250)
if movies_lst:
    save_list('top250_movies.txt', movie_names(movies_lst))
    chart_bar('ratings.txt', rating_bar(movies_lst))
    chart_bar('years.txt', year_bar(movies_lst))
