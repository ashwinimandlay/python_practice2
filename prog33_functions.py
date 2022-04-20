# function
def greet_user():
    print("hi there")
    print("welcome aboard")


# always keep 2 empty spaces after function
print("start")
greet_user()
print("finish")

# if we don't use parenthesis then it simply tells us that it
# is a function and its location (used in groupby())
print(greet_user)

# default values in function (doesn't necessarily require input)


def addition(x=5, y=6):
    return x + y


print(addition(x=1, y=2))
print(addition(3, 3))
# if we pass nothing then it assumes the default value
print(addition())
print('\n')
# NOTE: that the default value must be written at last of
# function definition and required values first
# ex:


def multiplier(x, y=1):
    return x * y


print(multiplier(2))
print(multiplier(2, 5))
# print(multiplier(y=5, 2)) this is incorrect
