SEPARATOR = 'New  Distribution  Votes  Rank  Title\n'
MOVIES_FILE_NAME = 'top250_movies.txt'
RATINGS_FILE_NAME = 'ratings.txt'
YEARS_FILE_NAME = 'years.txt'


def get_info(line):
    rank, *title, year = line.split()[2::]
    return rank, ' '.join(title), year[1:-1:]


def get_data():
    movies = []
    ratings = {}
    years = {}
    try:
        with open('./ratings.list') as f:
            line = ''
            while line != SEPARATOR:
                line = f.readline()
            for _ in range(250):
                line = f.readline()
                rating, title, year = get_info(line)
                movies.append(title)
                ratings[rating] = ratings.get(rating, 0) + 1
                years[year] = years.get(year, 0) + 1
    except FileNotFoundError:
        print('There are no file')
    return movies, ratings, years


def create_histograms():
    movies, ratings, years = get_data()
    with open(MOVIES_FILE_NAME, 'wt') as f:
        for movie in movies:
            f.write(movie + '\n')
    with open(RATINGS_FILE_NAME, 'wt') as f:
        for rating in sorted(ratings):
            f.write(rating + ': ' + '*' * ratings[rating] + '\n')
    with open(YEARS_FILE_NAME, 'wt') as f:
        for year in sorted(years):
            f.write(year + ': ' + '*' * years[year] + '\n')


if __name__ == '__main__':
    create_histograms()
