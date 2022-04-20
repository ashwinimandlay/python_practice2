# utility
from prog45_greatest_number_finder import greatest_number
num = input("> ")
print(greatest_number(num))

# there is already a function max built in for this
print(max(num))

# notice that for two digit numbers too we get single digit
# answer such as for: 2, 6, 10, 1 answer would be 6
print(num)
# this is because it takes the every input( space included)
# as a seperate number or character
# to correct this use dot split method
num1 = num.split()
print(greatest_number(num1))
print(max(num1))
