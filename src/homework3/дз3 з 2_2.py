'''Используйте на предыдущий список slice чтобы получить следующий: ['ab', 'ad', 'bc'].'''


g = [i[0]+c[0] for i in 'ab'  for c in 'bcd']

print(g)

s = g[slice(0,1)]+g[slice(2,3)]+g[slice(4,5)]
print(s)
