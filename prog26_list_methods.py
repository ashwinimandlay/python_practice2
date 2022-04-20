# list method
# list and tuples can be added
numbers = [3, 6, 3, 8, 9]

print(numbers)
numbers.append(12)
print(numbers)
numbers.insert(0, 77)
print(numbers)
numbers.pop()
print(numbers)

print(numbers.index(8))
# this tells us index of number
# if the number is not in the list it generates a value error
# therefore we use the in operator
print(50 in numbers)

print(numbers.count(3))

print(numbers.sort())
# this doesn't give a value, just sorts our list in ascending

# if we don't want to permanently change our list then use
# sorted instead
new_lis = sorted(numbers)

print(numbers)
numbers.reverse()
print(numbers)
# sort list in decending order
number_copy = numbers.copy()
# copy the list
