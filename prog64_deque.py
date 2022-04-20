# double-ended queue
# it's basically a list where you can add from both sides
# popleft, extend, rotate and count are new
from collections import deque

d = deque()
d.append(1)
print(d)

d.appendleft(2)
print(d)

# input in extend must be iterable i.e, like list or string
d.extend('789')
print(d)

# extend left --> add elements one by one
d.extendleft([1, 2, 3])
print(d)

# similar to circular rotation
# positive 2 means clockwise or forward rotation
d.rotate(2)
print(d)

# counts the number of time the element has occured
print(d.count(1))

