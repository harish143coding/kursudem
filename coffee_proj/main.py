#  data resources
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
profit = 0


def checking_resources(order_ingredients):
    """Returns True when order can be made, False if ingredients are insufficient."""
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True


def processing_coins(drinks):
    print("please insert coins")
    quarters = input("how many quarters?: ")
    dimes = input("how many dimes?: ")
    nickles = input("how many nickles?: ")
    pennies = input("how many pennies?: ")
    estimated_cost = quarters + nickles + dimes + pennies
    print(drinks["cost"])
    if float(estimated_cost) >= drinks["cost"]:
        print("coffee is ready to drink cheers ☕")
        return True


user_ip = True
while user_ip:
    selection = input("What would you like? (espresso/latte/cappuccino):")
    if selection == "off":
        user_ip = False
    elif selection == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")
    else:
        drink = MENU[selection]
        if checking_resources(drink["ingredients"]):
            processing_coins(drink)
        else:
            print("insufficient funds")



