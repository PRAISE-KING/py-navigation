
# sometimes the code encounters errors because of invalid user input ... but as a programmer you need to handle these errors so as the system might not crash
# example
try:
    age = int(input('age : '))
    print(age)
    income = 3000
    risk = income/age
    print(risk)
except ValueError:
    print('Invalid input !!')
except ZeroDivisionError:
    print('Age cannot be zero.')

# incase the user enters input that isn't integer we'll get a value error
# incase the user enters 0 as age we'll get a zero division error
# to manage all these errors we use a methods like try except

# there are various error handling methods ,,,,also have different errors

