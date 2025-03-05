
# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< FOR LOOP >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# used to iterate over items of a collection such as string

for item in 'PRAIZKING':
    print(item)

print('   ')

fruits = ['mango' , 'oranges' , 'apple']

for fruit in fruits:
    print(fruit)

print('   ')

# for large data we use range function to iterate through items,,,in this case the range is 7
for something in range(7):
    print(something)

print('   ')

# incase we want data in between other data ...like number between 10 and 20
for num in range(10, 20):
    print(num)

print('   ')

# incase we want to print data let's say a number that's btn 5 and 10 and increases by two
for num1 in range(5, 10, 2):
    print(num1)

print('   ')

# calculate total prices in the cart full of items below
# since the for loop iterates through single item,we create a variable set it to zero
# price will be added in each iteration to total price
prices = [10, 20, 30]

total_price = 0
for price in prices:
    total_price +=price
print(f'Total : {total_price}')

print('   ')
# for total price not to be repeated we print outside the loop

passkey = ['a', 'b', 'c', 'e', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
new = []
code = input('Enter your code please : ')

for letters in passkey:
    for letter in code:
        if letter != letters in passkey:
            new.append(letter)

print(new)

#                              <<<<<<<<<<<<<<<<<<<<<<<<<<<<< Exercise >>>>>>>>>>>>>>>>>>>>>>>>>>>

# find a solution for letters in new list not to be repeated .
# find how you can add items in a list from user input







#