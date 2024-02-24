from operator import is_
from menu import MENU, resources

def calculate_cost(drink_name):
    return MENU[drink_name]["cost"]

def check_resources(drink_name):
    for ingredient in MENU[drink_name]["ingredients"]:
        if resources[ingredient] < MENU[drink_name]["ingredients"][ingredient]:
            print(f"Sorry there is not enough {ingredient}.")
            return False
    return True

def deduct_resources(drink_name):
    for ingredient in MENU[drink_name]["ingredients"]:
        resources[ingredient] -= MENU[drink_name]["ingredients"][ingredient]

def process_coins():
    print("Please insert coins.")
    total = int(input("How many quarters?: ")) * 0.25
    total += int(input("How many dimes?: ")) * 0.1
    total += int(input("How many nickles?: ")) * 0.05
    total += int(input("How many pennies?: ")) * 0.01
    return total

def check_transaction(drink_cost, money_inserted):
    if money_inserted < drink_cost:
        print("Sorry that's not enough money. Money refunded.")
        return False
    elif money_inserted > drink_cost:
        print(f"Here is ${money_inserted - drink_cost} in change.")
    return True

def make_coffee(drink_name):
    print(f"Here is your {drink_name} ☕. Enjoy!")

is_on = True

while is_on:
    drink = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if drink == "off":
        is_on = False
    elif drink == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
    else:
        if check_resources(drink):
            cost = calculate_cost(drink)
            money_inserted = process_coins()
            if check_transaction(cost, money_inserted):
                deduct_resources(drink)
                make_coffee(drink)