# В файле хранятся данные с сайта IMDB. Скопированные данные хранятся в файле
# ./data/ ratings.list.
# Откройте и прочитайте файл(если его нет необходимо вывести ошибку).
# Найдите ТОП250 фильмов и извлеките заголовки.
# Программа создает 3 файла  top250_movies.txt – названия файлов,
# ratings.txt – гистограмма рейтингов, years.txt – гистограмма годов.


import matplotlib.pyplot as plt


with open('ratings.list', encoding="ISO-8859-1") as src, open('top250_movies.txt', 'w') as dest:
    dct_rank, dct_years = {}, {}
    for line in src:
        if line.startswith('      000000'):
            lst_temp = [el for el in line.split()[2::]]
            rank, year = float(lst_temp.pop(0)), int(lst_temp.pop(-1).strip('()/I'))
            dct_rank[rank] = dct_rank.get(rank, 0) + 1
            sorted_rank_lst = sorted(dct_rank.items())
            dct_years[year] = dct_years.get(year, 0) + 1
            sorted_year_lst = sorted(dct_years.items())
            dest.write(' '.join(lst_temp) + '\n')
        elif len(dct_rank) > 1:
            break

with open('ratings.txt', 'w') as hysto_ranks:
    for el in sorted_rank_lst:
        hysto_ranks.write(str(el[0]) + '#' * el[1] + '\n')

with open('years.txt', 'w') as hysto_years:
    for el in sorted_year_lst:
        hysto_years.write(str(el[0]) + '#' * el[1] + '\n')


years = [el[0] for el in sorted_year_lst]
movies = [el[1] for el in sorted_year_lst]
plt.bar(years, movies)
plt.title("distribution by year")
plt.xlabel("years")
plt.ylabel("movies")
plt.show()


ranks = [str(el[0]) for el in sorted_rank_lst]
movies = [el[1] for el in sorted_rank_lst]
plt.bar(ranks, movies)
plt.title("distribution by ranks")
plt.xlabel("ranks")
plt.ylabel("movies")
plt.show()