# map function
# map(mapping_function, iterable)
# returns a map object

lis = [1, 2, 3, 4]
print('using lambda')
print(list(map(lambda x: pow(x, 3), lis)))


def cube(n):
    return pow(n, 3)


print('using functions:')
print(list(map(cube, lis)))
