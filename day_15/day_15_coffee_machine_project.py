from menu import MENU, resources


money = 0


def report():
    print(f'Water: {resources["water"]}ml')
    print(f'Milk: {resources["milk"]}ml')
    print(f'Coffee: {resources["coffee"]}ml')
    print(f'Money: {money}$')


def order_ingredients(a):
    a = a.lower()
    water = (MENU[a]['ingredients']['water'])
    coffee = (MENU[a]['ingredients']['coffee'])
    try:
        milk = (MENU[a]['ingredients']['milk'])
    except:
        milk = 0
    return water, coffee, milk


def check_reqources(water, coffee, milk):
    if water > resources["water"]:
        print('Not enough water')
        return False
    elif coffee > resources["coffee"]:
        print('Not enough coffee')
        return False
    elif milk > resources["milk"]:
        print('Not enough milk')
        return False
    else:
        return True


def process_coins(cost):
    print(f'Insert coins to match order cost: {order_cost}')
    quarters = int(input('Please, insert quarters\n'))
    dimes = int(input('Please, insert dimes\n'))
    nickels = int(input('Please, insert nickels\n'))
    pennies = int(input('Please, insert penneis\n'))
    coin_sum = 0.25*quarters + 0.1*dimes + 0.05*nickels + 0.01*pennies
    if coin_sum < cost:
        print('Sorry, that is not enough money. Money refunded')
        return False
    elif coin_sum == cost:
        return True
    else:
        change = round(coin_sum - cost, 2)
        print(f'Here is your {change}$ in change')
        return True


def adjust_resources(water, coffee, milk):
    resources["coffee"] -= coffee
    resources["water"] -= water
    resources["milk"] -= milk    


coffee_machine_on = True


while coffee_machine_on:

    order = input('What would you like to order? espresso / latte / cappuccino\n')

    if order.lower() == 'off':
        print('Turning off the machine.espre..')
        coffee_machine_on = False
    elif order.lower() == 'report':
        report()
    elif order.lower() == 'espresso' or order.lower() == 'latte' or order.lower() == 'cappuccino':
        order_water, order_coffee, order_milk = order_ingredients(order)
        order_cost = MENU[order.lower()]['cost']

        if check_reqources(order_water, order_coffee, order_milk):
            if process_coins(order_cost):
                money += order_cost
                adjust_resources(order_water, order_coffee, order_milk)
                print(f'Here is your {order}. Enjoy!')

    else:
        print('Wrong command')
