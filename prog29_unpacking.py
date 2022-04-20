# unpacking list items
# can be used for tuple or square brackets

coordinates = [1, 2, 3]
# now if we have to multiply coordinate [0] with [1]
# we can write full coordinate [0] * coordinate[1]
# or assign x = coordinate[0] and y = [1]

# but in python we can simply use unpacking function/tool

x, y, z = coordinates
print(y)
