var = int(input("число"))
for number in range (2, var // 2 + 1):
  if not var % number:
    break
else:
  print ('простое')