
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

profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0,
}

# TODO 4.Check resources sufficient?
def is_resource_sufficient(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True

# TODO 5. Process Coins
def process_payments(price):
    print(f"Price is ${price} \nInsert Coins")
    total = 0
    total += int(input("How many quarters?: ")) * 0.25
    total += int(input("How many dimes?: ")) * 0.10
    total += int(input("How many nickels?: ")) * 0.05
    total += int(input("How many pennies?: ")) * 0.01
    # TODO 6. Check transaction successful
    if total < price:
        print("Sorry that's not enough money. Money refunded.")
        return False
    elif total > price:
        print(f"Here is ${round(total - price, 2)} in change.")
        global profit
        profit += round(price, 2)
        return True
    else:
        profit += total
        return True


# TODO MAKE COFFEE
def prepare_coffee(drink_ingredients):
    for item in drink_ingredients:
        resources[item] -= drink_ingredients[item]
    return True

# TODO:2. Turn off coffee machine by entering "off"
power = True

while(power == True):
    # TODO:1. Prompt user be asking "What would you like?"
    choice = input("What would you like? (espresso/latte/cappuccino): ")
    if choice.lower() == 'off':
        power = False
    # TODO: 3. print report of all coffee machine resources
    elif choice.lower() == 'report':
            print(f"Water: {resources['water']}ml")
            print(f"Milk: {resources['milk']}ml")
            print(f"Coffee: {resources['coffee']}g")
            print(f"Money: ${profit}")
    elif choice.lower() in MENU:
        drink = MENU[choice.lower()]
        if is_resource_sufficient(drink['ingredients']):
            if process_payments(drink['cost']):
                prepare_coffee(drink['ingredients'])
                print(f"Here is your {choice.lower()}. Enjoy!")