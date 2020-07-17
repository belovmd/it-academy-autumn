divisor = 10
digits = 1

number = int(input("Введите n: "))

# Sanity checks - inverting the input if it's negative
# and aborting if the input has less than two digits.

if number < 0:
    number *= -1
elif not number // 10:
    print("Число должно иметь больше одного разряда!")
    quit()

while number // divisor:
    digits += 1
    divisor *= 10

for i in range(1, int((digits / 2) + 1)):
    first_digit = number % (10 ** (digits - i + 1)) // (10 ** (digits - i))
    last_digit = (number % 10 ** i) // 10 ** (i - 1)
    if first_digit != last_digit:
        print(f"Число {number} - не палиндром.")
        quit()

print(f"Число {number} - палиндром.")
