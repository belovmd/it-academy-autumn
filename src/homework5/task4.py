# В файле хранятся данные с сайта IMDB. Скопированные данные хранятся в файле
# ./data/ ratings.list.
# Откройте и прочитайте файл(если его нет необходимо вывести ошибку).
# Найдите ТОП250 фильмов и извлеките заголовки.
# Программа создает 3 файла  top250_movies.txt – названия файлов,
# ratings.txt – гистограмма рейтингов, years.txt – гистограмма годов.


with open('ratings.list', encoding="ISO-8859-1") as src, open('top250_movies.txt', 'w') as dest:
    dct_rank, dct_years = {}, {}
    for line in src:
        if line.startswith('      000000'):
            lst_temp = [el for el in line.split()[2::]]
            rank, year = float(lst_temp.pop(0)), int(lst_temp.pop(-1).strip('()/I'))
            dct_rank[rank] = dct_rank.get(rank, 0) + 1
            dct_years[year] = dct_years.get(year, 0) + 1
            dest.write(' '.join(lst_temp) + '\n')
        elif len(dct_rank) > 1:
            break

with open('ratings.txt', 'w') as hysto_ranks:
    sorted_list = sorted(dct_rank.items())
    for el in sorted_list:
        hysto_ranks.write(str(el[0]) + '#' * el[1] + '\n')

with open('years.txt', 'w') as hysto_years:
    sorted_list = sorted(dct_years.items())
    for el in sorted_list:
        hysto_years.write(str(el[0]) + '#' * el[1] + '\n')
