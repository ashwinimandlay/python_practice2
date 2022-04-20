# named tuple is more like a dictionary having keys and
# values pairs but here we can access both keys and values

# it also kind of resembles a Class where we pass arguments
# and make objects
from collections import namedtuple

# for multiple keys (name, height) put them in a list
# s1 and s2 are like Class objects
student = namedtuple('student', ['name', 'age'])
s1 = student('ashwini', 18)
s2 = student('john', 28)
print(s1)
print(s2)

# we can access namedtuple by index or using name
print(s1[0])
print(s1.name)
# getattr can also be used to access key value pair
print(getattr(s2, 'name'))

# we can also convert a list into namedtuple by _make()
lis = ['emily', 22]
print(student._make(lis))

# we can convert a dictionary to named tuple
dic = {'name': 'brook', 'age': 20}
print(student(**dic))
