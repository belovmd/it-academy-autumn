divisor = 10
digits = 1

input_variable = int(input("Введите n: "))

# Sanity checks - inverting the input if it's negative
# and aborting if the input has less than two digits.

if input_variable < 0:
    input_variable *= -1
elif not input_variable // 10:
    print("Must have more than one digit!")
    quit()

while input_variable // divisor:
    digits += 1
    divisor *= 10

for i in range(1, int((digits / 2) + 1)):
    first_digit = input_variable % (10 ** (digits - i + 1)) // (10 ** (digits - i))
    last_digit = (input_variable % 10 ** i) // 10 ** (i - 1)
    if first_digit != last_digit:
        print("Not a palindrome!")
        quit()

print("It's a palindrome!")
