"""
Каждый из N школьников некоторой школы знает Mi языков.
Определите, какие языки знают все школьники и языки,
которые знает хотя бы один из школьников.

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
"""


def get_int_number():
    while 1:
        count = input()
        if count.isdigit():
            return int(count)
        else:
            print("Enter number")


def get_student_data():
    student_data = set()
    number_of_languages = get_int_number()
    for _ in range(number_of_languages):
        student_data.add(input())
    return student_data


def languages():
    common_languages = set()
    at_least_one = set()
    count_of_students = get_int_number()

    for _ in range(count_of_students):
        student_languages = get_student_data()
        at_least_one.update(student_languages)
        if not common_languages:
            common_languages = student_languages
            continue
        common_languages = common_languages.intersection(student_languages)

    result = "{count}\n{languages}".format(
             count=len(common_languages),
             languages=','.join(common_languages)
    )
    print(result)
    result = "{count}\n{languages}".format(
             count=len(at_least_one),
             languages=','.join(at_least_one)
    )
    print(result)


languages()
