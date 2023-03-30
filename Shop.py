money_available = 100.00

shop = {'item1': 'iPhone', 'price1': 500.00,
        'item2': 'Piano', 'price2': 59.00,
        'item3': 'Lamp', 'price3': 98.00}

print("Welcome to the shop! You have", money_available, "pounds.")
print("Here is what we have in stock and their prices:")
print((shop['item1']), 'which costs', (shop['price1']))
print((shop['item2']), 'which costs', (shop['price2']))
print((shop['item3']), 'which costs', (shop['price3']))

# for item in shop:
#     print(shop[item]) #Attempt to use for loop

user_exit = input("Do you want to exit the shop, please specify with y or n: ")

try:
    if user_exit == 'y' or user_exit == 'Y':
        print('You have left the shop. Goodbye.')

    elif user_exit == 'n' or user_exit == 'N':
        choice = input('Great. What item would you like to buy? ')
        if choice == "iPhone":
            print('That will cost', {'price': '500.00'}.get('price'), 'pounds')
            iphone_cost = shop['iPhone']
            print(iphone_cost)
            print(item['price'])




        elif choice == "Piano":
            print('That will cost', {'price': '59.00'}.get('price'), 'pounds')

        elif choice == "Lamp":
            print('That will cost', {'price': '98.00'}.get('price'), 'pounds')

    else:
        raise ValueError()

except ValueError as error:
    print('Error. This is not a valid answer.')
