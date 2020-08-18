import sys

# Command line arguments, exception handling
# This program adds up integers that have
# been passed as arguments in the command line

try:
    total = sum(int(arg) for arg in sys.argv[1:])
    print('Sum = ', total)
except ValueError:
    print('Please supply integer arguments')
