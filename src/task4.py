"""
В файле хранятся данные с сайта IMDB. Скопированные данные хранятся в файле
./data/ ratings.list.
a. Откройте и прочитайте файл(если его нет необходимо вывести ошибку).
b. Найдите ТОП250 фильмов и извлеките заголовки.
c. Программа создает 3 файла  top250_movies.txt – названия файлов, ratings.txt
– гистограмма рейтингов, years.txt – гистограмма годов.
"""

BEFORE_TOP250_LINE = 'New  Distribution  Votes  Rank  Title'
TOP_MOVIES_COUNT = 250
GIST_MAX_LENGTH = 80


def get_top250_list(f):
    line = f.readline()
    while BEFORE_TOP250_LINE not in line:
        line = f.readline()
    lst = []
    for _ in range(TOP_MOVIES_COUNT):
        line = f.readline().strip()
        distr, votes, rank, *title, year = line.split()
        lst.append((votes, rank, title, year))
    return lst


def get_gist(lst):
    gist_data = {}
    for num in lst:
        gist_data[num] = gist_data.get(num, 0) + 1


    min_num = min(gist_data.values())
    max_num = max(gist_data.values())
    res = ''
    if max_num == min_num:
        for num in sorted(gist_data.keys()):
            res += str(num) + '|' + '*' * (GIST_MAX_LENGTH // 2)
        return res.strip()
    for num in sorted(gist_data.keys()):
        res += str(num) + '|' + '*' * (int((gist_data[num] - min_num) *
                                           GIST_MAX_LENGTH /
                                           (max_num - min_num))) + '*\n'
    return res.strip()


def get_headers(lst):
    titles = [' '.join(line[-2]) for line in lst]
    return '\n'.join(titles)


def get_ratings_gist(lst):
    ratings = [float(line[-3]) for line in lst]
    return get_gist(ratings)


def get_years_gist(lst):
    years = [int(line[-1].strip('()/I')) for line in lst]
    return get_gist(years)


def main():
    try:
        f = open('ratings.list')
    except FileNotFoundError:
        print('File not found')
        return

    top250_list = get_top250_list(f)
    f.close()

    with open('top250_movies.txt', 'w') as file:
        file.write(get_headers(top250_list))

    with open('ratings.txt', 'w') as file:
        file.write(get_ratings_gist(top250_list))

    with open('years.txt', 'w') as file:
        file.write(get_years_gist(top250_list))


if __name__ == "__main__":
    main()
