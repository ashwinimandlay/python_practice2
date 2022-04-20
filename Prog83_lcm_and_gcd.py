# lcm and gcd (or hcf)
# for gcd(a, b) we use Euclidean algorithm
# The algorithm is based on the below facts:
#       If we subtract a smaller number from a larger
#       (we reduce a larger number), GCD doesn’t change.
#       So if we keep subtracting repeatedly the larger
#       of two, we end up with GCD.

# for lcm(a, b) we simply use the formula:
# a * b = lcm(a, b) * gcd(a, b)

def gcd(a, b):
    if a == b:
        return a
    elif a > b:
        return gcd(a-b, b)
    elif a < b:
        return gcd(a, b-a)


print(gcd(15, 25))


# for lcm:
def lcm(a, b):
    return a*b//gcd(a, b)


print(lcm(15, 25))

# if we have a list of number and we have to find lcm or
# gcd of the list then use reduce() function
from functools import reduce
lis = [12, 18, 24]
gcd_of_lis = reduce(gcd, lis)
print('gcd of list: ', gcd_of_lis)

lcm_of_list = reduce(lcm, lis)
print('lcm of list: ', lcm_of_list)
