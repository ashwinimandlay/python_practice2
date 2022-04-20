# for loops

for item in "python":
    print(item)
# item is just some variable
# for loop takes each character of string one by one

for item in ['mosh', 'josh', 'sarah']:
    print(item)
# square bracket are used for list
# each string is like item number 1 , 2 etc

for item in [0, 1, 2, 3]:
    print(item)
# but what if we wanna use it over a large range
# then we use range function:
# range(10) -> 0-9, range(start,finish,steps)
# if no step given it takes step as 1

for item in range(10):
    print(item)
for item in range(5, 10):
    print(item)
for item in range(5, 10, 2):
    print(item)
