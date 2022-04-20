# WAP shows the output of 2 die roll
# ex: (1,4)
# use class called Dice and method roll
# every time we roll we get a tuple from 1 to 6
import random


class Dice:
    def roll(self):
        first = random.randint(1, 6)
        second = random.randint(1, 6)
        return first, second
        # this return value will be shown in tuple
        # ex (1, 2)
        # we can also manually add like return (first, second)


dice1 = Dice()
print(dice1.roll())
