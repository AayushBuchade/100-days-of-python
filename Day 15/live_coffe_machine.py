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
machine_on = True


def check_resources(drink):
    for item in MENU[drink]["ingredients"]:
        if MENU[drink]["ingredients"][item] > resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True


def process_coins():
    print("Please insert coins.")
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickles = int(input("How many nickles?: "))
    pennies = int(input("How many pennies?: "))

    return round(
        quarters * 0.25 +
        dimes * 0.10 +
        nickles * 0.05 +
        pennies * 0.01, 2
    )


def make_drink(drink):
    for item in MENU[drink]["ingredients"]:
        resources[item] -= MENU[drink]["ingredients"][item]


def report():
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${profit}")


while machine_on:
    choice = input("What would you like? (espresso/latte/cappuccino/report/off): ").lower()

    if choice == "off":
        machine_on = False

    elif choice == "report":
        report()

    elif choice in MENU:
        if check_resources(choice):
            payment = process_coins()
            cost = MENU[choice]["cost"]

            if payment >= cost:
                change = round(payment - cost, 2)
                print(f"Here is ${change} dollars in change.")
                profit += cost
                make_drink(choice)
                print(f"Here is your {choice}  Enjoy!")
            else:
                print("Sorry that's not enough money. Money refunded.")

    else:
        print("Invalid choice.")
