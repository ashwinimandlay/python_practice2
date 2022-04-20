# formatting strings

# insert a string or a character
print('a, b and {}'.format('whatever'))

# positional formatting string from list
lis = ['apple', 'orange']
print('i like {} but not {}'.format(lis[0], lis[1]))
# or using splat
print('i like {} but not {}'.format(*lis))

# also we can change position between them
print('i like {1} but not {0}'.format(*lis))
