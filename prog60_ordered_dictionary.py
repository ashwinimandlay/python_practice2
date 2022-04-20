# ordered dictionary:
# OrderedDict preserves the order in which the keys are inserted.
# A regular dict doesn’t track the insertion order and iterating
# it gives the values in an arbitrary order. By contrast, the
# order the items are inserted is remembered by OrderedDict.
from collections import OrderedDict

print("This is a Dict:\n")
d = {
    'a': 1,
    'b': 2,
    'c': 3,
    'd': 4,
    'e': 5,
    'f': 6,
    'g': 7
}
# d['a'] = 1
# d['b'] = 2
# d['c'] = 3
# d['d'] = 4
print(d)

for key, value in d.items():
    print(key, value)

print("\nThis is an Ordered Dict:\n")
od = OrderedDict()
od['a'] = 1
od['b'] = 2
od['c'] = 3
od['d'] = 4
print(od)
for key, value in od.items():
    print(key, value)
