import re

# Import, regular expressions

for test_string in ['555-1212', 'ILL-LEGAL']:
    if re.match(r'^\d{3}-\d{4}$', test_string):
        print(test_string, 'Is a valid local US phone number')
    else:
        print(test_string, 'rejected')
