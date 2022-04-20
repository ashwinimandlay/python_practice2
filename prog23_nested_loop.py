# nested loops
# can be used for writing co-ordinates etc

for x in range(4):
    for y in range(4):
        print(f"{x}, {y}")

# draw F shape using nested loop
for row in [0, 1, 2, 3, 4]:
    for column in range(1):
        if row == 0 or row == 2:
            print("XXXXX")
        else:
            print("XX")

# method 2
number = [5, 2, 5, 2, 2]
for j in number:
    print("X" * j)

# method 3 (using nested loop)
number = [5, 2, 5, 2, 2]
for x_count in number:
    output = '' # empty string
    for no_of_loop in range(x_count):
        output += "X"
    print(output)
