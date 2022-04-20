# dynamic 2-d array
arr = []
n = 4
for i in range(n):
    arr.append([])
print('using loop', arr)
# we can access all elements individually
arr[0].append(1)
arr[2].append(2)
print('append(using loop):', arr)

# shortcut
arr2 = [[] for _ in range(n)]
print('using list comprehension:', arr2)
arr2[0].append(1)
arr2[2].append(2)
print('append(using list comprehension):', arr2)
print()

# IMPORTANT: this is not same because we cannot access
# elements individually
arr1 = [[]]*n
print('using multiplication:', arr1)
arr1[0].append(1)
print('appended to all sublist', arr1)
# notice how appendind 1 will append to all the sublist
# that is because it is list times list
# so if 0th list we append 1 then it simply multiplies
# and is allocated to 0th, 1st, 2nd,... so on
