# groupby(iterable, key_function)
# groupby() function assigns the keys from key_function to
# same elements in the iterable (list, tuple or string)
# if key_function is not assigned it takes the element itself
# as the key
from itertools import groupby
s = 'aaabbbbbbbccdeee'
g = groupby(s)
print('without using key_function')
for keys, group in g:
    print(keys, list(group))

# IMPORTANT: it groups consecutive occurrence
# so it is advisable to use sorting for unique keys
jumbled_char = groupby("BCAACACAADBBB")
print('\nkeys are not unique')
for keys, group in jumbled_char:
    print(keys, list(group))

things = [("animal", "bear"), ("animal", "duck"),
          ("plant", "cactus"), ("vehicle", "speed boat"),
          ("vehicle", "school bus")]
g1 = groupby(things)
print()
for keys, group in g1:
    print(keys, list(group), sep='-->')


def choose_first_element(a):
    return a[0]


g2 = groupby(things, choose_first_element)
print('\n\nusing function:')
for keys, group in g2:
    print(keys, list(group), sep='-->')
# notice that we write choose_first_element
# and not choose_first_element() , this is because we are not
# calling the function but groupby is using the function
# because groupby format is : (iterable, function)
# so we are not calling a function but it puts the iterable items
# in the function

# we can also use lambda function
# lambda simply tells that what follows is a function
key_func = lambda x: x[0]
g3 = groupby(things, key_func)
print('\n\nusing lambda:')
for keys, group in g3:
    print(keys, list(group), sep='-->')

# ex for key_function
# group by a key function
# >>> # islower = lambda s: s.islower()                      # equivalent
# >>> def islower(s):
# ...     """Return True if a string is lowercase, else False."""
# ...     return s.islower()
# >>> print_groupby(sorted("bCAaCacAADBbB"), keyfunc=islower)
# key: 'False'--> group: ['A', 'A', 'A', 'B', 'B', 'C', 'C', 'D']
# key: 'True'--> group: ['a', 'a', 'b', 'b', 'c']
