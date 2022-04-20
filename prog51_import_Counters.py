from collections import Counter
# Counter is a class (therefore 'C' is capital)
# a counter is a container that stores elements as dictionary
# keys, and their count are stored as dictionary values
a = [1, 1, 2, 3, 4, 5, 3, 2, 3, 4, 2, 1, 2, 3]

print(Counter(a))
print(Counter(a).items())
print(Counter(a).values())
print(Counter(a).keys())

print(Counter(a).get(3))

# right now 'a' is a list so we cannot edit enteries/values
# associated with keys
# so to do that we make 'a' to be a dictionary
a = Counter([10, 1, 1, 8, 2, 3, 4, 5, 3, 2, 3, 4, 2, 1, 2, 3])
# now 'a' is dictionary and we can edit its values
a[1] -= 10
print()
print(a)
# after making it dictionary all previous operation available
print(a.values())

# Most_common method of Counters
# a.most_common(n) --> List the n most common elements
# and their counts from the most common to the least.
# If n is None, then list all element counts.
print('most common')
print(a.most_common())
a.most_common()
print(a.most_common(2))

