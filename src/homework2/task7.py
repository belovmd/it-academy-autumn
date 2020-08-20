# Given an array of integers your solution should find the smallest integer.

def find_smallest_int(arr):

    min = arr[0]
    for i in arr:
        if i < min:
            min = i
    return (min)


# In a small town the population is p0 = 1000 at the beginning of a year.
# The population regularly increases by 2 percent per year
# and moreover 50 new inhabitants per year come to live in the town.
# How many years does the town need to see its population
# greater or equal to p = 1200 inhabitants?

def nb_year(p0, percent, aug, p):
    i = 0
    while p0 < p:
        p0 = p0 * (percent / 100 + 1) + aug
        i += 1
    return i


# There is a bus moving in the city,
# and it takes and drop some people in each bus stop.
# You are provided with a list (or array) of integer arrays (or tuples).
# Each integer array has two items which represent number of people get
# into bus (The first item) and number
# of people get off the bus (The second item)
# in a bus stop. Your task is to return number of people who are
# still in the bus after the last bus station (after the last array).
# Even though it is the last bus stop, the bus is not empty
# and some people are still in the bus,
# and they are probably sleeping there :D
# Take a look on the test cases.
# Please keep in mind that the test cases ensure that
# the number of people in the bus
# is always >= 0. So the return integer can't be negative.
# The second value in the first integer array is 0,
# since the bus is empty in the first bus stop.

def number(bus_stops):
    left = 0
    for i in bus_stops:
        left += i[0] - i[1]
    return left


# Given: an array containing hashes of names
# Return: a string formatted as a list of names separated by commas
# except for the last two names, which should be separated by an ampersand.

def namelist(names):
    str = ''
    if len(names):
        arr = []
        for i in range(0, len(names) - 1):
            arr.append(names[i]['name'])
        str = ', '.join(arr)
        str += ' & ' + names[-1]['name'] if str != '' else names[-1]['name']

    return str


# Make a program that filters a list of strings
# and returns a list with only your friends name in it.
# If a name has exactly 4 letters in it,
# you can be sure that it has to be a friend of yours!
# Otherwise, you can be sure he's not...

def friend(x):
    friends = list(filter(lambda y: len(y) == 4, x[:]))

    return friends
