
import random

ROCK = 'r'
PAPER = 'p'
SCISSORS = 's'

choices = (ROCK, PAPER, SCISSORS)

def get_user_choice():
    while True:
        user_choice = input('Rock , Paper , Scissors (r/p/s) :').lower()
        if user_choice in choices:
            return user_choice
        # the above code checks for the presence of the choice in a tuple choices if presents it then returns the choice as user choice....if not available moves to the next code prints an error then re-runs again
        else:
            print('Invalid Choice !!')
            # continue
        # continue breaks the code then restarts it till the choice given is valid...only works inside the while loop
#         in this case continue can be left out

def display_choices(user_choice , comp_choice):
    print(f'You chose {user_choice}')
    print(f'Comp chose {comp_choice}')

def determining_winner(user_choice , comp_choice):
    if user_choice == comp_choice:
        print('You tie')
    elif ((user_choice == ROCK and comp_choice == SCISSORS) or
          (user_choice == SCISSORS and comp_choice == PAPER) or
          (user_choice == PAPER and comp_choice == ROCK)):
        print('You win !!')
    else:
        print('you loose !!')


def play_game():
    while True:
        user_choice = get_user_choice()

        comp_choice = random.choice(choices)

        display_choices(user_choice , comp_choice)

        determining_winner(user_choice , comp_choice)

        continuation = input('continue playing ? (y/n) :')
        if continuation == 'n':
            break

play_game()
