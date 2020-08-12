for elem in range(1, 101):
    if not elem % 15:
        print('FizzBuzz')
    elif not elem % 3:
        print('Fizz')
    elif not elem % 5:
        print('Buzz')
    else:
        print(elem)
