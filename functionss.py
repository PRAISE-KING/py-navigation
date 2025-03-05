
# are block of code written and can be called anywhere in the code to perform a specific task
# are defined using def... and are always accompanied by a bracket
# functions are only called after being defined cannot be called before....

def greet_user():
    print("Hi there , welcome to our meeting")


print("@TR COMPANY LTD")
greet_user()


# we can pass a parameter in a function and get the argument
# parameter - passed through the function
# arguement - passed when the fanction is called
# NOTE THAT => when a parameter is passed, the argument must also be passed....if not the code will run an error


def greeting(first_name , last_name):
    print(f'Hi {first_name} {last_name}')
    print("It's an honor to have you here")


greeting('PRAISE' , 'KING')


# in most cases we use positional arguments in function i.e greeting(praiz , king) - they are printed as per the sequencing of the parameter first_name as 'praiz' and last_name as 'king'
# we also have KEYWORD ARGUMENTS - in this the parameter is assigned specifically to a certain argument e.g

def best(friend , f2):
    print(f'hello {friend} and {f2}')


best( f2='@tr' , friend='royale' )
# no matter the position the output of the names will still be the same position as they are assigned to

# but in the case where positional and keyword arguments are used in the same arguments , the positional arguments comes first before keyword arguments e.g

best('king' , f2='praiz')