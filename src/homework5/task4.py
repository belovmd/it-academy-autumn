"""
В файле хранятся данные с сайта IMDB.
Скопированные данные хранятся в файле ./data/ ratings.list.
"""

SEPARATOR_HEADER = 'New  Distribution  Votes  Rank  Title\n'
DB_FILENAME = 'ratings.list'
MOVIELIST_FILENAME = 'top250_movies.txt'
YEARS_HISTOGRAM_FILENAME = 'years.txt'
RATINGS_HISTOGRAM_FILENAME = 'ratings.txt'
COUNT_OF_MOVIES = 250


def get_database():
    movie_names = []
    years = {}
    ratings = {}
    try:
        with open(DB_FILENAME, 'r') as file:
            line = ''
            while line != SEPARATOR_HEADER:
                line = file.readline()
            for i in range(COUNT_OF_MOVIES):
                line = file.readline()
                rating, year, movie_name = get_data_from_line(line)

                movie_names.append(movie_name)
                years[year] = years.get(year, 0) + 1
                ratings[rating] = ratings.get(rating, 0) + 1
        create_movie_names_file(movie_names)
    except FileNotFoundError:
        print('File not exist')
    return movie_names, years, ratings


def get_data_from_line(line):
    line = line.strip()
    array = line.split()
    rating = str(array[2])
    year = str(array[-1]).strip('()')
    name = ' '.join(array[3: -1])

    return (rating, year, name)


def create_movie_names_file(names):
    with open(MOVIELIST_FILENAME, 'w') as file:
        file.write('\n'.join(names) + '\n')


def create_histogram_file(data, file_name):
    with open(file_name, 'w') as file:
        for key in sorted(data.keys()):
            dollars = "$" * data[key]
            result = "{key} \t {dollars}\n".format(key=key,
                                                   dollars=dollars)
            file.write(result)


names, years, ratings = get_database()

create_movie_names_file(names)
create_histogram_file(years, YEARS_HISTOGRAM_FILENAME)
create_histogram_file(ratings, RATINGS_HISTOGRAM_FILENAME)
