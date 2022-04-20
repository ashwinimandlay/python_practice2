# Regex or Regular Expression
# used for searching text pattern within strings in python
# or various text editor

# r'string' --> raw string tells python to not interpret backslash (\)
# as special character ex: \t is tab
import re
text_to_search = '''
abcdefghijklmnopqurtuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
'''

# re.compile will make the raw string a variable to work on
pattern = re.compile(r'abc')

matches = pattern.finditer(text_to_search)

for match in matches:
    print(match)

# re.error will check for invalid regex expression
# ex: .*\+ is valid regex
# ex: .*+ is invalid regex
s1 = '.*\+'
s1_valid_flag = True
try:
    pattern = re.compile(s1)
except re.error:
    s1_valid_flag = False
    print('invalid regex for s1')
if s1_valid_flag:
    print('s1 is valid regex')

s2 = '.*+'
s2_valid_flag = True
try:
    pattern = re.compile(s2)
except re.error:
    s2_valid_flag = False
    print('invalid regex for s2')
if s2_valid_flag:
    print('s2 is valid regex')
    