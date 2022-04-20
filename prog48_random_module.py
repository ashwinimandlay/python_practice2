# Built in modules

import random

for i in range(3):
    print(random.random())
    # random value between 0 and 1
for i in range(3):
    print(random.randint(10, 20))
    # random value between 10 and 20

# we can also select a random person from a group
members = ['josh', 'mosh', 'bob', 'mary']
leader = random.choice(members)
print(leader)
