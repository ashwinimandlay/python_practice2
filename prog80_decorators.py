# decorators
# A decorator is just a callable that takes
# a function as an argument and returns a
# replacement function.

def outer(some_func):
    def inner():
        print("before some_func")
        ret = some_func()
        return ret + 1
    return inner


def foo():
    return 1


decorated = outer(foo)
print(decorated())
# We could say that the variable decorated is a
# decorated version of foo - it’s foo plus
# something. In fact we can permanently replace
# foo with the decorated version altogether so
# we always got our "plus something" version
# of foo.

# we can do this by simply assigning foo like
print('\nusing foo as variable-->')
foo = outer(foo)
print(foo())
# now everytime foo is called it will give us
# the decorated version of foo!!

# we can decorate a function by the @decorator by:
# IMPORTANT:

# @outer
# def foo():
#     return 1

# this is same as foo = outer(foo)
