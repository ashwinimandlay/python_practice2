from collections import defaultdict
# default dictionary is used to avoid invalid key/ value
# errors and sets a default value when key is not in
# dictionary, generally represented as:
# defaultdict(default_factory)

# if default_factory is list then default value is and
# empty list
d = defaultdict(list)
d[1] = [1]
d['b'] = [2]

print(d['b'])
print(d['c'])
print(d[0])
print(d)

# if default_factory is int then default value is zero
d2 = defaultdict(int)

d2['a'] = 3
d2[2] = 11

print(d2[2])
print(d2[14])
print(d2)
# we can also change values of keys inside dictionary
d2[2] -= 1
print(d2[2])
print(d2)
