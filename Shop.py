money_available = 100.00
attempt = 0

shop = {'item1': 'iPhone', 'price1': 500.00,
        'item2': 'Piano', 'price2': 59.00,
        'item3': 'Lamp', 'price3': 98.00}

print("Welcome to the shop! You have", money_available, "pounds.")
print("Here is what we have in stock and their prices:")
print((shop['item1']), 'which costs', (shop['price1']))
print((shop['item2']), 'which costs', (shop['price2']))
print((shop['item3']), 'which costs', (shop['price3']))

# for item in shop:
#     print(shop[item]) # Attempt to use for loop

while True:
    user_exit = input("Do you want to exit the shop, please specify with y or n: ")
    try:
        if user_exit == 'y' or user_exit == 'Y':
            print('You have left the shop. Goodbye.')
            break

        elif user_exit == 'n' or user_exit == 'N':
            try:
                choice = input('Great. What item would you like to buy? ')
                if choice == shop['item1']:
                    print('That will cost', shop['price1'], 'pounds')
                    choice_cost = shop['price1']

                elif choice == shop['item2']:
                    print('That will cost', shop['price2'], 'pounds')
                    choice_cost = shop['price2']

                elif choice == shop['item3']:
                    print('That will cost', shop['price3'], 'pounds')
                    choice_cost = shop['price3']

                else:
                    raise ValueError()

            except ValueError:
                print('The item you have chosen is not on the list')

            if money_available >= choice_cost:
                print('Here is your', choice)
                money_available = (money_available - choice_cost)
                print('You now have', money_available)

            elif money_available < choice_cost:
                print('You do not have the sufficient funds. We have logged this attempt.')
                attempt = attempt + 1
                if attempt < 3:
                    more_money = input('Do you have more money? y or n ')
                    try:
                        if more_money == 'y' or more_money == 'Y':
                            added_amount = int((input('How much would you like to add?')))
                            money_available = (money_available + added_amount)
                            print('You now have', money_available)

                        elif more_money == 'n' or more_money == 'N':
                            print('Okay. You will be escorted out of the shop.')

                        else:
                            print('Invalid response.')

                    except ValueError():
                        print('You have inputted an invalid answer')

                elif attempt > 3:
                    # raise ConnectionRefusedError()  # Unable to find custom error
                    print('You have attempted more than 3 times. Your account has been locked. Please leave the shop.')
                    break


        elif user_exit != 'y' or 'Y' or 'n' or 'N':
            raise ValueError()

    # except ConnectionRefusedError():
    #     print('You have attempted more than 3 times. Your account has been locked. Please leave the shop.')

    except ValueError():
        print('Error. This is not a valid answer.')
