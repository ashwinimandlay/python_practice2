# zipped function
# zipped(iterable1, iterable2, iterable3, ...)
# This function returns a list of tuples.
# elements of same index from iterable1,2,3 will be combined
# in a single tuple

# If the iterable1,2,3 are of unequal lengths,
# then the returned list is truncated to the length
# of the shortest iterable length
a = [1, 2]
b = [3, 4]
c = [5, 6, 7] # 7 is truncated here

x = [a] + [b] + [c]
print(list(zip(*x)))

print(list(zip([1, 2, 3, 4, 5, 6], 'Hacker')))
