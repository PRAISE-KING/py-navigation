
# by default the functions returns NONE ...but with return statement it returns a value
# return statement is used to return the value

def square(number):
    return number * number


print(square(5))

# if the return value misses the code will print none by default as every function return none by default


def square(number):
    print(number * number)


print(square(4))
# in the case above, the code will print 16 and none
# 16 - because the function is called and executed and print function prints the result
# none - because the code doesn't have a return statement to return the results