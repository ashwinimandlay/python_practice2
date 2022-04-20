# sorted function
# sorted(iterable, key=none, reverse =False)

print('sort in ascending order')
a = [2, 1, 7, 4, 5, 3]
print(sorted(a))

print('descending order')
a = [2, 1, 7, 4, 5, 3]
print(sorted(a, reverse=True))

# we can also use key_function (like in groupby) to sort
# according to our need
# the larger the value is, the less the importance gets.
# In this case, you can sort the array in reverse order.
print('reverse using lambda')
a = [2, 1, 7, 4, 5, 3]
print(sorted(a, key=lambda x: -x))

print('x>3')
a = [2, 1, 7, 4, 5, 3]
print(sorted(a, key=lambda x: x <= 3))
# in this function the false value comes first then True value
# order will be same as occurence

# key actually define the priority order
# lambda c: (lowest priority, medium priority,...highest priority)
# lowest priority is executed first i.e sorted for c[0]
# low values (2, 7)at start and high value(9, 10) end of list
# then this sorted list is passed to next medium priority c[1]
# while keeping in mind all the previous keys priority...
a = [(2, 1), (7, 4), (9, 3), (7, 5), (10, 2)]
print(sorted(a, key=lambda c: (c[0], c[1])))

# if there is a negative sign in priority list then it means
# the higher the value lower is the priority (comes first)
# (10,  9) comes first
# used for reverse sorting
a = [(2, 1), (7, 4), (9, 3), (7, 5), (10, 2)]
print(sorted(a, key=lambda c: (-c[0], c[1])))

a = [(2, 1), (7, 4), (9, 3), (7, 5), (10, 2)]
print(sorted(a, key=lambda c: (-c[0], -c[1])))


# Your task is to sort the string 's' in the following manner:
#
# All sorted lowercase letters are ahead of uppercase letters.
# All sorted uppercase letters are ahead of digits.
# All sorted odd digits are ahead of sorted even digits.
s = 'Sorting1234'

sorted_list = sorted(s, key=lambda x:
(x.isdigit(), x.isdigit() and int(x) % 2==0, x.isupper(),
 x.islower(), x) )
print(*sorted_list, sep='')