"""
For loop, built-in enumerate function, new style formatting
Print names of friends
"""


friends = ['john', 'pat', 'gary', 'michael']
for i, name in enumerate(friends):
    print("iteration {iteration} is {name}".format(iteration=i, name=name))
