
import random
from random import choice

comp_guess = random.randint(0, 100)

while True:
    try:
        user_guess = int(input('Guess a number between 0 and 100 : '))

        if user_guess == comp_guess:
            print('Congrats you guessed right....')
            break
        elif user_guess > comp_guess:
            print('TOO HIGH ')
        elif user_guess < comp_guess:
            print('TOO LOW ')

    except ValueError:
        print('please enter a valid input')

# The ' TRY ' and ' EXCEPT ' command helps give a friendly error message of your choice other than the system's
# in the code above , without the try and except algorithm, if user input was a string or float then the system would give error message because, user input should be an integer according to the program

# >>>>>>>>>>>>>> TO BE RESEARCHED ON >>>>>>>>>>>>>>>>>>>>>>>
#  Other uses of the (try , except) code
#  other features of random
