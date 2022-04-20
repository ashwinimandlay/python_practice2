import re

text_to_search = '''
abcdefghijklmnopqurtuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
1234567890
Ha HaHa
MetaCharacters (Need to be escaped):
. ^ $ * + ? { } [ ] \ | ( )
coreyms.com
321-555-4321
123.555.1234
123*555*1234
800-555-1234
900-555-1234
Mr. Schafer
Mr Smith
Ms Davis
Mrs. Robinson
Mr. T
'''

sentence = 'Start a sentence and then bring it to an end'

# without re.compile
# match returns the first occurrence of word
print('without using re.compile')
matches = re.search(r'ha', text_to_search)
print(matches)

matches = re.findall(r'ha', text_to_search)
print(matches)

# using re.compile()
# re.compile creates a regular expression in Pattern class
# after we can use pattern class objects
print('\nusing re.compile')
pattern = re.compile(r'\d{3}.\d{3}.\d{3}')

matches = pattern.search(text_to_search)
print(matches)

matches = pattern.findall(text_to_search)
print(matches)

# finditer creates an iterable object
matches = pattern.finditer(text_to_search)
print(list(matches))
