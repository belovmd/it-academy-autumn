"""
itertools
Use itertools.groupby and bool to return groups of
consecutive lines that either have content or don't.

PRINTS:
This is the first paragraph.
This is the second.
"""


from itertools import groupby
lines = '''
This is the
first paragraph.

This is the second.
'''.splitlines()

for has_chars, frags in groupby(lines, bool):
    if has_chars:
        print(' '.join(frags))
