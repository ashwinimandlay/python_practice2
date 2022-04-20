# any() and all() built-in function
# any(exp1, exp2, exp3, ...)
# expression can be iterables
# expression1,2,3 must return true/ false (boolean) ex 1>2-->False
# any will return True only when all expressions are True
print('any function --> ', any([1 > 0, 1 == 0, 1 < 0]))
# all(exp1, exp2, exp3, ...)
# same for all() but all expression must be True for all() function
# to return True
print('all function', all(['a' < 'b', 'b' < 'c']))

# expressions can be iterables of true aor false
n = [2, 4, 6, 1, 7]
boolean_list = [i > 5 for i in n]
print('boolean list --> ', boolean_list)
print('passing the boolean list in any -->', any(boolean_list))
print('passing the boolean list in all -->', all(boolean_list))
# program to find palindrom all numbers must be greater than zero

n = [12, 9, 61, 5, 14]
# IMPORTANT: any() and all() function takes exactly 1 argument
print(all([i > 0 for i in n]) and any(str(j) == str(j)[::-1] for j in n))

m = [12, 9, 61, 5, 14, -2]
print(all([i > 0 for i in m]) and any(str(j) == str(j)[::-1] for j in m))
