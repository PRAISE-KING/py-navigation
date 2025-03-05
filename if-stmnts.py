# ..........exercise 1
# if it's hot day
#          its a hot day
#          drink plenty of water
# otherwise if its cold
#          its a cold day
#          wear warm clothes
# otherwise
#          its a lovely day

is_hot = True
is_cold = False

if is_hot:
    print('''
            its a hot day
            drink plenty of water''')
elif is_cold:
    print('''
            its a cold day
            wear warm clothes''')
else:
    print('Its a lovely day')




# ..........exercise 2

# price of a house = $1m
# if buyer has good credit
#     they need to put down 10%
# otherwise
#     they need to put down 20%
# print the down payment

price = 1000000

good_credit = False

if good_credit:
    down_payment = (10 / 100) * price
    print('CONGRATULATIONS! you Qualify for our offers')

else:
    down_payment = (20 / 100) * price
    print('sorry! you dont Qualify for our offers')


print(f'Down payment : ${down_payment}')