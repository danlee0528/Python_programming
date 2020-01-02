# Output format option 1
year = 2016
event = 'Referendum'
print(f'Results of the {year} {event}')

# Output format option 2
yes_votes = 42_572_654
no_votes = 43_132_495
percentage = yes_votes / (yes_votes + no_votes)
print('{:-9} YES votes {:2.2%}'.format(yes_votes, percentage))
print('{0} and {1}.'.format(yes_votes, no_votes))
print('{1} and {0}.'.format(yes_votes,no_votes))
print('{yv} and {nv}.'.format(yv=yes_votes, nv=no_votes))

# Output format option 3
s = 'Hello, world'
print(str(s))
print(repr(s))  # repr() generates representations which can be read by the interpreter

# Formatted String Liters
table = {'Sjoered': 4127, 'Jack': 4098, 'Dcab': 7678}
for name, phone in table.items():
    print(f'{name:10} ==> {phone:10d}')     # ':' will cause that filed to be a minimum number of characters wide
                                            # useful fo making columns line up
 # Other modifiers
animals = 'eels'
print(f'My hovercraft is full of {animals!s}.')    # '!s' applies str()
print(f'My hovercraft is full of {animals!r}.')    # '!r' applies rep()
print(f'My hovercraft is full of {animals!a}.')    # '!a' applies ascii()

# long string format
print('Jack: {Jack:d}; Sjoered: {Sjoered:d}; Dcab: {Dcab:d}'.format(**table))
print(table)

# other examples
for x in range(1, 11):
        print('{0:2d} {1:3d} {2:4d}'.format(x, x**2, x**3))

print('12'.zfill(5))   # right-justifies
print('12'.zfill(7))
print('12'.ljust(5))
print('12'.center(5))

# old school formatting
import math
print('The value of pi is approximately %5.3f.' % math.pi)