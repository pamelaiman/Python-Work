money_available = 100.00


def shopping():
    shop = [
        {'name': 'iPhone', 'price': 500.00},
        {'name': 'Wardrobe', 'price': 100.00},
        {'name': 'Piano', 'price': 59.99},
        {'name': 'Lamp', 'price': 98.00}]

    print("Welcome to the shop! You have", money_available, "pounds. Here is what we have in stock and their prices:")
    for item in shop:
        print((item['name']), 'which costs', (item['price']))
    choice = input("Do you want to exit the shop, please specify with y or n: ")
    if choice != 'y' and choice != 'n':
        raise ValueError('You have not inputted a valid answer')

    elif choice == 'y':
        print('You have left the shop.')

    elif choice == 'n':
        choice2 = input('What item do you want to buy?')

        for choice2 in shop:
            if money_available > choice2['price']:
                print('You can afford a', choice2['name'])
            #if money_available < choice(int['price']):
                print('You cannot afford this')



shopping()
