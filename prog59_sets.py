# sets are unordered list without duplicates
# methods: intersection_update, difference_update, union_update,
# symmetric_difference_update
# issubset, isdisjoint, issuperset
s = 'string and strip'
print(set(s))

# initialize set
empty_set = set()

# different functions that can be used on sets
a = [1, 2, 4, 2, 4, 5, 1]
b = [1, 8]
print((set(a).intersection(b)))
print(set(a).union())

# better approach is to convert then in sets first instead of list
set_a = set(a)
set_b = set(b)

# add something to set
set_b.add('ashwini')
print('add something = ', set_b)

# difference
set3 = set_a.difference(set_b)
print('set3 =', set3)

# to avoid storing in another variable use difference_update
set_a.difference_update(set_b)
print('difference_update = ', set_a)

# update is used to add which is not already in intersection
s1 = set(a)
s2 = set(b)
s1.update(s2)
print('update method = ', s1)

# terms in either set_a or set_b (basically xor)
set1 = {1, 3, 5, 8}
set2 = {2, 3, 4, 8}
print(set1 ^ set2)

# remove and discard
# .remove(x) removes x from the set and returns NONE
# if x is not present then it raises a KeyError
# to overcome KeyError we use discard instead
set4 = {1, 2, 3, 4, 5}
# set4.remove(6)
# this raises error

set4.discard(6)
# this does not
