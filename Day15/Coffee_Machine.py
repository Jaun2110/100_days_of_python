MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

money = {
    "value": 0,
}


def show_resources_report(resource_levels):
    """Call this function to print the current resource levels of the machine"""
    for key in resource_levels:
        print(f"{key}: {resource_levels[key]}")

    print("")


def check_resources(user_choice, resource_levels):
    # if the user chooses espresso
    for key in MENU[user_choice]['ingredients']:
        if resource_levels[key] > MENU[user_choice]['ingredients'][key] and resource_levels[key] > 0:
            return True
        else:
            print(f"Sorry,there is not enough {key}.")
            return False


def deduct_resources(user_choice):
    for key in MENU[user_choice]['ingredients']:
        resources[key] -= MENU[user_choice]['ingredients'][key]
    return resources


def turn_off():
    print("turning off the machine")
    return False


def check_money(quarters, dimes, nickels, pennies):
    quarters_total = quarters * 0.25
    dimes_total = dimes * 0.10
    nickles_total = nickels * 0.05
    pennies_total = pennies * 0.01
    total = quarters_total + dimes_total + nickles_total + pennies_total
    return total


def calculate_change(money_given, cost_of_coffee):
    return money_given - cost_of_coffee


def make_coffee(res):
    power_on = True

    while power_on:
        #   TODO: prompt the user to select type of coffee
        coffee_choice = input("What would you like?").lower()

        if coffee_choice == 'report':
            show_resources_report(res)
        elif coffee_choice == 'off':
            power_on = turn_off()
        else:
            enough = check_resources(coffee_choice, res)
            if enough:
                quarters = int(input('How many quarters?:'))
                dimes = int(input('How many dimes?:'))
                nickles = int(input('How many nickles?:'))
                pennies = int(input('How many pennies?:'))
                money_given = check_money(quarters, dimes, nickles, pennies)
                change = calculate_change(money_given, MENU[coffee_choice]['cost'])

                if money_given > MENU[coffee_choice]['cost']:
                    # deduct resources
                    res = deduct_resources(coffee_choice)
                    print(f"Your change: {round(change, 2)}\nHere is your {coffee_choice}. Enjoy!")
                else:
                    print(f"Money is not enough! Here is {money_given} refunded ")

            else:
                print("")


make_coffee(resources)





