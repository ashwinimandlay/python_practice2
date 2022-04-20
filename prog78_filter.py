# filter(function, iterable)
# here one by one iterable go to the function and if function
# returns true then that item is in filter object else not

lis = [1, 2, 3, 4, 5, 6]
a = list(filter(lambda x: x % 2 == 0, lis))
# if divisible by 2 get in list
print(a)
