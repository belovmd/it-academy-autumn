"""
В файле хранятся данные с сайта IMDB. Скопированные данные хранятся в файле ./data/ ratings.list.
Откройте и прочитайте файл(если его нет необходимо вывести ошибку).
Найдите ТОП250 фильмов и извлеките заголовки.
Программа создает 3 файла  top250_movies.txt – названия файлов, ratings.txt – гистограмма р
ейтингов, years.txt – гистограмма годов.

"""
import operator
ratings = []
years = []
ratings_ = {}
ratings_sort = {}
years_ = {}
years_sort = {}
wr_file = open('top250_movies.txt','a')
file_rating = open('rating.txt', 'a')
file_years = open('years.txt', 'a')
try:
    file = open('ratings.list')
    for i in range(1,279):
            s = file.readline()
            if i > 28:
                 wr_file.write(s[32:])


                 for word in s.split():
                     if '.' in word:
                         for char in word:
                             if char in '0123456789':
                                 ratings.append(word)
                                 break
                     if '(' in word:
                         years.append(word)


    for i in ratings:
         ratings_[i] = ratings_.get(i,0)+1


    for key,value in sorted(ratings_.items(), key=operator.itemgetter(1),reverse = True):
         ratings_sort[key] = value


    for key,value in ratings_sort.items():
        file_rating.write(str(key)+'('+str(value)+')')
        for i in range(0,value):
            file_rating.write('+')
        file_rating.write('\n')


    for i in years:
        years_[i] = years_.get(i,0)+1


    for key,value in sorted(years_.items(), key=operator.itemgetter(1),reverse = True):
        years_sort[key] = value


    for key,value in years_sort.items():
        file_years.write(str(key)+'('+str(value)+')')
        for i in range(0,value):
            file_years.write('+')
        file_years.write('\n')


except FileNotFoundError:
    print('Невозможно открыть файл')


finally:
    file.close()
    wr_file.close()
    file_rating.close()
    file_years.close()