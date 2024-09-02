from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_machine = CoffeeMaker()
money_counter = MoneyMachine()
menu = Menu()

coffee_machine_on = True

while coffee_machine_on:
    options = menu.get_items()
    order = input(f'What would you like to order? {options}\n')

    if order.lower() == 'off':
        print('Turning off the machine.espre..')
        coffee_machine_on = False
    elif order.lower() == 'resources report':
        coffee_machine.report()
    elif order.lower() == 'money report':
        money_counter.report()
    elif order.lower() == 'espresso' or order.lower() == 'latte' or order.lower() == 'cappuccino':
        drink = menu.find_drink(order.lower())
        if coffee_machine.is_resource_sufficient(drink):
            if money_counter.make_payment(drink.cost):
                coffee_machine.make_coffee(drink)
    else:
        print('Wrong command. Please, try again')
