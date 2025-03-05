
# = is an assignment operator but
# == (equal to) is a conditional operator
# ( >,<,==,!=,>=,<=) are conditional operators

# .........................Example 1........................

# write a code with the following conditions
# if name is less than 4 characters long then prompt an error message
# if name is more than 50 character long then also prompt an error message
# otherwise name looks good

user_name = input('Please enter your name : ').title()

ans = len(user_name)

if ans <= 3:
    print('Name must be at least 4 characters')
elif ans > 50:
    print('Your name is too long ')
else:
    print(f'hello {user_name} your name looks good')
