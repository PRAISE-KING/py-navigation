
# Write a code that converts weight to either kg or pounds

weight = int(input('Your weight : '))
unit = input('Unit : (L)bs or (K)g : ').lower()

if unit == 'l':
    converted_weight = weight * 0.45
    print(f'You are {converted_weight} kgs')
else:
    converted_weight = weight / 0.45
    print(f'You are {converted_weight} pounds')
