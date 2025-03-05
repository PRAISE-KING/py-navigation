
# <<<<<<<<<<<<<<<<<<<<<<<<<<<< NESTED LOOP >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# is a loop inside a loop

# .................Example.................

for x in range(3):
    for y in range(3):
        print(f'({x} , {y})')
# in this code the loop iterates through x first prints 0 then moves to y loop where
# it prints all the items from 0 to 2 then goes back to x prints 1 then comes to y printing all items again
# the loop repeats till x is all iterated and printed

# print an f using x
# the for loop will iterate through the list...then the numbers will be multiplied by x in each iteration

numbers = [5, 2, 5, 2, 2]

for number in numbers:
    item = 'x' * number
    print(item)

print("""

""")

# using nested loop
for x_count in numbers:
    count_output = ''
    for count in range(x_count):
        count_output += 'x'
    print(count_output)

# example 2

for n in numbers:
    output = ''
    for fig in range(n):
        output += 'e'
    print(output)
#  the print function should be inside the first for loop but outside the inner for loop
