from zoneinfo import available_timezones


# <<<<<<<<<<<<<<<<<<< shopping items >>>>>>>>>>>>>>>>>>>>>>>>

def total():
    item_price = {
        'MEAT': 154,
        'MILK': 60,
        'BREAD': 130,
        'TOMATOES': 70,
        'MANGOES': 76,
        'JUICE': 50,
        'SWEETS': 23
    }
    total_price = 0

    for items in shopped_items:
         total_price += item_price.get(items)
    print(f'Total price : {total_price} ksh')


available_items = {
        'MEAT': 154,
        'MILK': 60,
        'BREAD': 130,
        'TOMATOES': 70,
        'MANGOES': 76,
        'JUICE': 50,
        'SWEETS': 23,
        'BUY' : 'buy'
    }

shopped_items = []
print('Press buy option to buy the goods')

shop = True

while shop is True:
     item = input('> ').upper()
     if item not in available_items:
         print(f'''
         Not available
         Available items : 
         {available_items}''')
         continue
     shopped_items.append(item)

     if item == 'BUY':
         shop = False
         shopped_items.remove('BUY')
         print(shopped_items)
         total()
else:
    print('Thank you for shopping with us')


