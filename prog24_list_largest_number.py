# list

names = ['josh', 'mary', 'sarah', 'bob']
print(names)

print(names[1])

print(names[-1])

print(names[1:])

# find the largest number in a list
numbers = [10, 13, 9, 3, 15, 19, 20, 20]
max = numbers[0]
for x in numbers:
    if x > max:
        max = x
print(f'largest number is {max}')
