# Языки
# Каждый из N школьников некоторой школы знает Mi языков.
# Определите, какие языки знают все школьники и языки,
# которые знает хотя бы один из школьников.


stud = [{input() for i in range(int(input()))} for j in range(int(input()))]
every, some = set.intersection(*stud), set.union(*stud)
print(len(every), *sorted(every), sep='\n')
print(len(some), *sorted(some), sep='\n')
