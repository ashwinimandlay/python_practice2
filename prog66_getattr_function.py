# getattr(a, b) function
# instead of eval we can use this (more appropriate)
# getattr(a, b) is replaces by a.b
# ex: getattr(set, update) --> set.update
# ex: getattr(set, update)() --> set.update()

# if we want to say do:
# input:
# pop
# remove 1
# what it does --> lis.pop() or lis.remove(1)
lis = [1, 2, 3, 4]
print(lis)
instruction = input().split() + ['']
if instruction[0] == 'pop':
    getattr(lis, instruction[0])()
else:
    getattr(lis, instruction[0])(int(instruction[1]))

print(lis)
