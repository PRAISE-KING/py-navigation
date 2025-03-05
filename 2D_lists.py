
# 2-Dimensional lists - is a list where each item in that list is another list
# 2-Dimensinal lists have alot of application in machine learning and data science

# example -a matrix

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# <<<<<<<<<<<<<<<< accessing items in the matrix >>>>>>>>>>>>>>>>>>>>>>>>>
# we use two square brackets
# e.g to acces 6 in the list

print(matrix[1][2])
# first you access the item in the matrix which is a list then the item in the list

# changing the value
# e.g

matrix[0][1] = 66
print(matrix)

# to iterate all items in the loop we use a nested loop

for row in matrix:
    for item in row:
        print(item)