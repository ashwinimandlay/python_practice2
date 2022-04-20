# re.split(regex, string)
# here regex is the expression which splits the string in lists
# returns a list
import re

# \W represents all the non-alphanumeric characters (not words basically)
s = 'Words, words , Words'
print(re.split(r'\W', s))

s1 = "Word's words Words"
print(re.split(r'\W', s1))
