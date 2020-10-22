"""
В файле хранятся данные с сайта IMDB.
Скопированные данные хранятся в файле ./data/task4/ ratings.list.
1. Откройте и прочитайте файл(если его нет необходимо вывести ошибку).
2. Найдите ТОП250 фильмов и извлеките заголовки.
3. Программа создает 3 файла
    top250_movies.txt – названия файлов,
    ratings.txt – гистограмма рейтингов,
    years.txt – гистограмма годов.
"""
from os import path


def read_films():
    def weighted_rank(film):
        """weighted rank = (v/(v+k))*X + (k/(v+k))*C

        where:

        X = average for the movie (mean)

        v = number of votes for the movie

        k = minimum votes required to be listed in the top 250

        (currently 25000)

        C = the mean vote across the whole report (currently 6.90)

        :param film:
        :return: int(rate)
        """
        vot, rate, *_ = film
        result = vot / (vot + 25000) * rate + (25000 / (vot + 25000)) * 6.90
        return vot > 25000 and result

    work_path = path.join(path.dirname(__file__), 'data', 'task4')

    films = []
    try:
        with open(path.join(work_path, 'ratings.list')) as f:
            for line in f:
                try:
                    items = line.split()
                    # film line
                    distribution, votes, rate, *name, year = items
                    if not line.strip() or len(distribution) != 10:
                        continue

                    # year validation
                    year = year.strip('()')
                    if not (year and len(year) == 4 and year.isdigit()):
                        continue

                    name = ' '.join(name)

                    films.append((int(votes),
                                  float(rate),
                                  name.strip(),
                                  int(year)))
                except Exception:
                    continue
    except FileNotFoundError:
        print("File not found")

    # sort top 250 films
    films.sort(key=weighted_rank, reverse=True)
    top250_films = []
    count = 0
    rates = []
    names = []
    years = []
    only_name = []
    for film in films:
        if count == 250:
            break
        _, rate, name, year = film

        # if in list exist copy of the film
        if name not in only_name:
            top250_films.append(film)
            rates.append(rate)
            names.append((rate, name, year))
            years.append(year)
            only_name.append(name)
            count += 1

    with open(path.join(work_path, 'top250_movies.txt'), 'w') as f:
        print(*sorted(names, key=lambda x: x[1]), file=f, sep='\n')

    rates.sort()
    min_rate = rates[0]
    max_rate = rates[-1]
    dct_rates = {}
    while min_rate <= max_rate:
        dct_rates[round(min_rate, 1)] = 0
        min_rate += 0.1
    for rate in rates:
        dct_rates[rate] += 1
    with open(path.join(work_path, 'ratings.txt'), 'w') as f:
        for key, value in dct_rates.items():
            print(str(key) + ':', '+' * value, file=f)

    years.sort()
    min_year = years[0]
    max_year = years[-1]
    dct_years = {}
    while min_year <= max_year:
        dct_years[min_year] = 0
        min_year += 1
    for year in years:
        dct_years[year] += 1
    with open(path.join(work_path, 'years.txt'), 'w') as f:
        for key, value in dct_years.items():
            print(str(key) + ':', '+' * value, file=f)


def main():
    read_films()


if __name__ == '__main__':
    main()
