def has_enough_money(money_available, choice_cost):
    if money_available >= choice_cost:
        return 'You have enough money'
    return 'You do not have enough money'


def exit_shop(user_exit):
    if user_exit == 'y' or user_exit == 'Y':
        return 'Exit shop'
    return 'Stay in shop'


def not_enough_money_after(money_available, added_amount, choice_cost):
    if not has_enough_money() and (choice_cost > (money_available + added_amount)):
        return 'Not enough money'

def has_enough_money_after(money_available, added_amount, choice_cost):
    if not has_enough_money() and ((money_available + added_amount) > choice_cost)
        return 'You now have enough money'

def payment_attempt(attempt):
    number_of_attempts = 0
    if not (has_enough_money() and not_enough_money_after()):
        number_of_attempts == attempt + 1

def too_many_attempts(number_of_attempts):
    if number_of_attempts > 3:
        return 'You have attempted too many times'