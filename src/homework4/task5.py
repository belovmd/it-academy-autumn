"""
Каждый из N школьников некоторой школы знает Mi языков.
Определите, какие языки знают все школьники и языки,
которые знает хотя бы один из школьников.

Входные данные
Первая строка входных данных содержит количество школьников N.
Далее идет N чисел Mi, после каждого из чисел идет Mi строк,
содержащих названия языков, которые знает i-й школьник.

Пример входных данных:
3          # N количество школьников
2          # M1 количество языков первого школьника
Russian    # языки первого школьника
English
3          # M2 количество языков второго школьника
Russian
Belarusian
English
3
Russian
Italian
French

Выходные данные
В первой строке выведите количество языков, которые знают все школьники.
Начиная со второй строки - список таких языков.
Затем - количество языков, которые знает хотя бы один школьник,
на следующих строках - список таких языков.
"""


from functools import reduce


def main():

    count_of_students = int(input('count_of_students'))

    languages_of_students = []
    for student in range(count_of_students):
        temp_languages = []
        for languages in range(int(input('count_of_languges'))):
            temp_languages.append(input('language'))
        languages_of_students.append(set(temp_languages))
        temp_languages.clear()

    common = reduce(lambda common, languages: common & languages,
                    languages_of_students)
    print(len(common))
    print(common)

    all_languages = reduce(lambda all, languages: all | languages,
                           languages_of_students)

    print(len(all_languages))
    print(all_languages)


if __name__ == '__main__':
    main()
