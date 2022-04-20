# power and divmod
# pow(a,b) --> a ** b
# pow(a,b,m) --> (a ** b) % m = remainder

a, b, m = 3, 4, 5
print(pow(a, b), pow(a, b, m), sep='\n')

# divmod(a, b) --> a % b
# divmod returns a tuple of the quotient and remainder
print(divmod(177, 10))
