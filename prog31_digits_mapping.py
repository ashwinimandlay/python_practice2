# WAP where input is phone number in digits
# output is phone number in words

digits_mapping = {
    '1': 'one',
    '2': 'two',
    '3': 'three',
    "4": 'four'
}
phone = input("phone: ")
output = ''
for x in phone:
    output += digits_mapping.get(x, "!") + " "
print(output)

# Note: to print multiple output on same line use an empty
# string and keep on adding to it, finally print that resultant
