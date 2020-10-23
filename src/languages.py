"""
Каждый из N школьников некоторой школы знает Mi языков.
Определите, какие языки знают все школьники и языки,
которые знает хотя бы один из школьников.
"""


languages = []
for student in range(int(input())):
    languages.append(set())
    for language in range(int(input())):
        languages[student].add(input())
print(languages)
all_ = set.intersection(*languages)
any_ = set.union(*languages)
print(len(all_), *all_, sep='\n')
print(len(any_), *any_, sep='\n')
