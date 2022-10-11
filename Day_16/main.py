from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_machine = CoffeeMaker()
coffee_menu = Menu()
money_machine = MoneyMachine()

process = False

while not process:
    print(coffee_menu.get_items())
    user_input = input("Select the Beverages or type 'report' to issue a report ")
    if user_input == 'off':
        process = True

    elif user_input == 'report':
        print(coffee_machine.report())
        print(money_machine.report())

    else:
        menu_item_choice = coffee_menu.find_drink(user_input)

        if coffee_machine.is_resource_sufficient(menu_item_choice) and money_machine.make_payment(menu_item_choice.cost):
            coffee_machine.make_coffee(menu_item_choice)