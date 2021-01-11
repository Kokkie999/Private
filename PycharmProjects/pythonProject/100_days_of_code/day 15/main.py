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
}


def check_resources(ingredients):
    """Returns True when order can be made or False is ingredients are insufficient."""
    for item in ingredients:
        if ingredients[item] >= resources[item]:
            print(f"Sorry, there is not enough {item}")
            return False
    return True


def process_coins():
    """Returns the total calculated from coins inserted."""
    total = int(input("Number of quarters: ")) * 0.25
    total += int(input("Number of dimes: ")) * 0.10
    total += int(input("Number of nickles: ")) * 0.05
    total += int(input("Number of pennies: ")) * 0.01
    return total


def transaction_ok(money_received, drink_cost):
    """Return True when the payment is accepted or False if money is insufficient."""
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is $ {change} in change.")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry that's not enough money, Money refunded.")
        return False


def make_product(choice, ingredients):
    for item in ingredients:
        resources[item] -= ingredients[item]
    print(f"Here is you {choice}. Enjoy!")


machine_on = True

while machine_on:
    choice = input("\nWhat would you like? (espresso/latte/cappuccino): ").lower()
    if choice == "off":
        machine_on = False
    elif choice == "report":
        print(f"Water:   {resources['water']} ml")
        print(f"Milk:    {resources['milk']} ml")
        print(f"Coffee:  {resources['coffee']} g")
        print(f"Profit:  $ {profit}")
    else:
        drink = MENU[choice]
        if check_resources(drink['ingredients']):
            payment = process_coins()
            if transaction_ok(payment, drink['cost']):
                make_product(choice, drink['ingredients'])

