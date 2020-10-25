"""
В файле хранятся данные с сайта IMDB. Скопированные данные хранятся в файле .
/data/ ratings.list.
Откройте и прочитайте файл(если его нет необходимо вывести ошибку).
Найдите ТОП250 фильмов и извлеките заголовки.
Программа создает 3 файла  top250_movies.txt – названия файлов,
ratings.txt – гистограмма рейтингов, years.txt – гистограмма годов.
"""
import matplotlib.pyplot as plt

from itertools import islice

filename = 'ratings.list'
top250_movies = 'top250_movies.txt.txt'
ratings = 'ratings.txt'
years = 'years.txt'
lst_top250_movies = []
lst_ratings = []
lst_years = []
try:
    with open(filename, 'r') as myfile1:
        f = list(islice(myfile1, 28, 278))
        for line in f:
            new_line_top250_movies = ' '.join(line.strip().split()[3:])
            new_line_ratings = ' '.join(line.strip().split()[2:3])
            new_line_years = ' '.join(line.strip().split()[-1][1:5])
            new_line_years = ''.join(new_line_years.split())

            lst_top250_movies.append(new_line_top250_movies + '\n')
            lst_ratings.append(new_line_ratings + '\n')
            lst_years.append(new_line_years + '\n')

            with open(top250_movies, 'w', newline='\n', encoding='utf-8') as f:
                f.writelines(lst_top250_movies)

            with open(ratings, 'w', newline='\n', encoding='utf-8') as myfile3:
                myfile3.writelines(lst_ratings)

            with open(years, 'w', newline='\n', encoding='utf-8') as myfile4:
                myfile4.writelines(lst_years)

except FileNotFoundError:
    print(f'File {filename} not found')

"""Creating histograms"""
plt.plot(lst_ratings, color='green')
plt.title('histogram of ratings')
plt.xlabel('count')
plt.ylabel('rating')
plt.show()

plt.plot(sorted(lst_years), color='blue')
plt.title('histogram of years')
plt.xlabel('count')
plt.ylabel('year')
plt.show()
