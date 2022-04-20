# Fraction class
# Fraction(numerator = 0, denominator = 1) with default values
# Fraction class has two methods (.numerator) and (.denominator)
# returns (numerator/ denominator) in fraction form
from fractions import Fraction

a = Fraction(10, 15)
print('a --> ', a)
# Fraction returns the reduced expression
# in this example 10/15 is reduced to 2/3

# if we want a float to retun in a/b form then:
f = 1.13
print("1.13 in fraction is --> ", Fraction(1.13))
print('10.5 in fraction is -->', Fraction(10.5))

# if we add Fraction classes then also it returns in a/b form
print('10/15 * 3/5 is -->', end='')
print(Fraction(10, 15) * Fraction(3, 5))
# same with addition and multiplication

# using strings in Fraction
# string form: [sign][numerator]/[denominator]
print('using strings we get -->', Fraction('-13/5'))
# string form: 'float value'
# if numerator does not divide the denominator then this
# return denominator multiple of 10
print("1.13 in fraction is --> ", Fraction('1.13'))
print('10.5 in fraction is -->', Fraction('10.5'))


# IMPORTANT: difference of Fraction(1.13) and Fraction('1.13')
print('important differences:')
print("1.13 in fraction is --> ", Fraction(1.13))
print("1.13 in fraction is --> ", Fraction('1.13'))

# we can limit the denominator to any number
print('denominator limited')
print(Fraction(1.13).limit_denominator(50))
# useful to calculate numbers like pi:
print('pi with different limits')
print(Fraction('3.14159265358979323846').limit_denominator(10000))
# returns Fraction(355, 113)

print(Fraction('3.14159265358979323846').limit_denominator(100))
# returns Fraction(311, 99)

print(Fraction('3.14159265358979323846').limit_denominator(10))

# we can also only access denominator numerator
print('numerator is --> ', Fraction(10, 15).numerator)
print('denominator is -->', Fraction(10, 15).denominator)
