# WAP to remove duplicates in a list
numbers = [2, 3, 7, 4, 3, 4]

new = []
for x in numbers:
    if x not in new:
        new.append(x)
print(new)
