# eval(string) function
# inside eval there must be a string and not variable
# eval returns an integer value
x, y, z = [1, 2, 3]
print(eval('x+y+z'))
# IMPORTANT: there has to be a variable in the string that needs
# to be evaluated or simply substituted like in formatted string

evaluate = 'a*(a+1)'
a = 3
print(eval(evaluate))

s = 'print(2+3)'
print('print statement in eval', end= '-->')
eval(s)
# we can also make a function out of it
# like we cannot make pop function using string:
# s = [1, 2, 3]
# p = 'pop' + '()'
# s.p --> this doesn't work because it does not recognize p
# as a pop function but by using eval:
s = [1, 2, 3]
print('s before pop = ', s)
p = 'pop' + '()'
eval('s.{}'.format(p))
print('s after pop (using eval function) = ', s)

# program:
# first line has a list
# second line the contains either pop, remove and/or discard
# commands followed by their associated value
lis = list(map(int, input().split()))
instruction = input().split() + ['']
# here we make instruction list of atleast two string
# for ex: for i/p = remove 3 --> instruction = ['remove','3','']
# for i/p = pop --> instruction = ['pop', '']
eval('lis.{0}({1})'.format(*instruction))
print(lis)
