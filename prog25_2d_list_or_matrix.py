# 2d list ( used in data science and machine learning)

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
# imagine this as collection of list

print(matrix[0][1])

# we can also modify/access it later by:
matrix[0][1] = 20
print(matrix[0][1])

# we use nested loops to find all the items
for rows in matrix:
    for item in rows:
        print(item)
