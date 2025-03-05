# .............................WHILE LOOP.................................
# used to execute block of codes multiple times
# while condition:    => how is written
from os import WCONTINUED

secret_number = 8
guess_count = 0
guess_limit = 3

while guess_count < guess_limit:
    guess = int(input('guess a number : '))
    # input always returns a string so, we change it to an integer by adding int
    guess_count += 1
    if guess == secret_number:
        print('you won....!!')
        break
#         the break statement ends the loop when the goal is met
else:
    print('You are a looser....hahaha')

# ...............................Example 2.........................................

started = False

print('''
    welcome to car drive gaming base...
    press :
           Start (s) - start the car
           Stop (p) - stop the car
           quit (q) - exit
           turn (t) - turn the car
           left (l) - turn left
           right (r) - turn right
           straight (f) - go stright
               ''')

START = 's'
STOP = 'p'
TURN = 't'
LEFT = 'l'
RIGHT = 'r'
QUIT = 'q'
STRAIGHT = 'f'

feedbacks = (START,STOP,TURN,LEFT,RIGHT)

def get_gamer_feedback():
    while True:
        gamer_feedback = input('> ').lower()
        if gamer_feedback in feedbacks:
            return gamer_feedback
        else:
            continue

def start_car(gamer_feedback):
    if gamer_feedback == START:
        if started:
            print('Car already started...')
        else:
            started = True
            print('''
                car started.....
                press :
                    l - to turn right
                    r - to turn right
                    ''')

def turn_car(gamer_feedback):
    while True:
        if gamer_feedback == RIGHT or LEFT or STRAIGHT:
            if gamer_feedback == LEFT:
                print('now heading left....')
            elif gamer_feedback == RIGHT:
                print('now heading right........')
            elif gamer_feedback == STRAIGHT:
                print('heading straight')
                break

def stop_car(gamer_feedback):
    if gamer_feedback == STOP:
        if not started:
            print('car already stopped....')
        else:
            started = False
            print('The car has stopped...Get the fuck out!!!')

def play_game():
    while True:
        gamer_feedback = get_gamer_feedback()

        start_car(gamer_feedback)

        turn_car(gamer_feedback)

        stop_car(gamer_feedback)
        if gamer_feedback ==  QUIT:
            print('You are exiting now.....!!!')
            break

play_game()
#                   <<<<<<<<<<<<<<<<<<<<<<<<Game start point >>>>>>>>>>>>>>>>>>>>>>>>>>


