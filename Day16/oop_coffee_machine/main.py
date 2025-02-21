from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

#create all instances
menu = Menu()
money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()

is_on = True
while is_on:

    drink_choice = input(f"What would you like? {menu.get_items()}:")



    if drink_choice == "report":
        coffee_maker.report()
        money_machine.report()
    elif drink_choice == "off":
        is_on = False
    else:
        menu_item = menu.find_drink(drink_choice)
        enough_resources = coffee_maker.is_resource_sufficient(menu_item)
        # print(enough_resources)
        if enough_resources:
            money_machine.make_payment(menu_item.cost)
            coffee_maker.make_coffee(menu_item)
