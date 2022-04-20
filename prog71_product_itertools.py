# product function
# product(iterable1, iterable2, iterable3,...)
# it is cartesian product
from itertools import product

a = [1, 2]
b = [3, 4, 5]
# c = [5, 6, 7]

print(list(product(a, b)))
