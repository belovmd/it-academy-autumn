"""
Каждый из N школьников некоторой школы знает Mi языков. Определите, какие языки
знают все школьники и языки, которые знает хотя бы один из школьников.
Входные данные
Первая строка входных данных содержит количество школьников N. Далее идет N
чисел Mi, после каждого из чисел идет Mi строк, содержащих названия языков,
которые знает i-й школьник.
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
Начиная со второй строки - список таких языков. Затем - количество языков,
которые знает хотя бы один школьник, на следующих строках - список таких
языков.
"""


def languages_of_pupils(str_):
    list_of_input = str_.split('\n')
    list_of_input = [line.strip() for line in list_of_input]
    pupil_count = int(list_of_input[0])
    pupil = 0
    language_base = {}

    for line in list_of_input[1:]:
        if line.isdigit():
            pupil += 1
            language_base[pupil] = set()
            if pupil > pupil_count:
                break
            continue
        else:
            language_base[pupil].add(line)

    all_pupils_languages = set()
    min_one_pupil_languages = set()
    for ind, set_ in enumerate(language_base.values()):
        min_one_pupil_languages |= set_
        if not ind:
            all_pupils_languages |= set_
        else:
            all_pupils_languages &= set_

    print(len(all_pupils_languages))
    for lang in all_pupils_languages:
        print(lang)
    print(len(min_one_pupil_languages))
    for lang in min_one_pupil_languages:
        print(lang)
    

if __name__ == '__main__':
    input_str = """3
    2
    Russian
    English
    3
    Russian
    Belarusian
    English
    3
    Russian
    Italian
    French"""
    languages_of_pupils(input_str)
