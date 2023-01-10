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

quarters = 0.25
dimes = 0.1
nickels = 0.05
pennies = 0.01

play = True

while play:
    preference = input("What would you like? (expresso/latte/cappuccino): ").lower()
    if preference == "report":
        print(f"Water: {resources['water']}ml\n"
              f"Milk: {resources['milk']}ml\n"
              f"Coffee: {resources['coffee']}\n"
              "Money: $0")

    # print(MENU[preference]['ingredients']['water'])
    if preference == "latte" or preference == "cappuccino" or preference == "expresso" and \
            MENU[preference]['ingredients']['water'] != 0:
        print("Please insert coins")
        quarters = int(input("how many quarters? ")) * quarters
        dimes = int(input("how many dimes? ")) * dimes
        nickels = int(input("how many nickels? ")) * nickels
        pennies = int(input("how many pennies? ")) * pennies

        money = quarters + dimes + nickels + pennies
        if preference == "latte" or preference == "espresso" or preference == "cappuccino" and money >= MENU['latte'][
            'cost']:
            money = round(money - MENU[preference]['cost'], 1)
            print(f"Here is ${money} in change")
            print(f"Here is your {preference} ☕️. Enjoy")
            MENU[preference]['ingredients']['water'] = 0
    else:
        print("Sorry, there is not enough water")

    if preference == "off":
        play = False

# money = quarters + dimes + nickels + pennies
# print(quarters)
# print(money)


    if 2 > 0:
        print("hey")
    else:
        print("print")

