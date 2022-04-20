# lambda function = anonymous function
# format = lambda input: return value

# write a function to compute 3*x +1
print(lambda x: 3*x + 1)
# lambda is not a function rather it is a python keyword that
# simply tells that whatever follows is a nameless function
# if we print lambda expression it tells that it is a function

# therefore, we assign this lambda to a variable and then pass
# arguments in the function
f = lambda x: 3*x + 1
print(f)
# this says that f is a function (just like before)

print(f(2))
# now we substitute x = 2

# for multiple input
f2 = lambda x, y: x + y
print(f2(2, 3))

# we can also directly pass the value
print((lambda x, y: x + y)(2, 3))
# (lambda x, y: x + y)(2,3) is just f(2,3)
