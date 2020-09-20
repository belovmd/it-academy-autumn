# Языки
# Каждый из N школьников некоторой школы знает Mi языков.
# Определите, какие языки знают все школьники и языки,
# которые знает хотя бы один из школьников.


stud = [{input('Языки: ') for i in range(int(input('Введите кол-во языков: ')))}
        for j in range(int(input('Введите кол-во школьников: ')))]
every, some = set.intersection(*stud), set.union(*stud)
print(len(every), *sorted(every), sep='\n')
print(len(some), *sorted(some), sep='\n')
