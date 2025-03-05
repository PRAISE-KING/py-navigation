
import random

# <<<<<<<<<     ask user to roll the dice >>>>>>>>>>>>>

while True:
    user_input = input("Roll the dice? (y - to roll , n - to quit ) > ").lower()

    if user_input == 'y':
         
#      generate random numbers using random method,,,,from 1 to 6
#      we repeat to generate two random numbers

        dice1 =random.randint(1 , 6)
        dice2 = random.randint(1, 6)
        print(f'({dice1} , {dice2})')

    if user_input == 'n':
        print('Thanks for playing')
        break
        # game_mode = False

    else:
        print('INVALID INPUT!!!')
