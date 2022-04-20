# reduce and accumulate functions
# reduce(function, iterable, initial_value = NONE)
# reduce takes the first two value of the iterable[0]and[1],
# apply the function on them the takes the output and next iterable[3]
# and continues....

# something along the lines of:
# reduce(mul, [1, 2, 3, 4]) is effectively doing this:
# mul(mul(mul(1, 2), 3), 4)
from functools import reduce

lis = [1, 2, 3, 4]
print('without initial value')
print(reduce(lambda x, y: x + y, lis))

print('with initial value')
print(reduce(lambda x, y: x + y, lis, 6))

# instead of lambda we can use operator module that does same thing
import operator
print('using operator module')
print(reduce(operator.add, lis))

# NOTE: there is a similar function in itertools
# known as accumulate
# accumulate(iterable, function)
# accumulate returns accumulate object
# list(accumulate(iterable, function)) stores a list of all
# intermediate values
from itertools import accumulate
print('using accumulate function')
print(list(accumulate(lis, operator.add)))
