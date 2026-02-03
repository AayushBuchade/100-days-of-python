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


resource = {
    "water": 300,
    "milk": 200,
    "coffee": 100
}

profit = 0


def check_resource(drinks):
    ingredient = MENU[drinks]["ingredients"]
    for items in ingredient:
        if ingredient[items] > resource[items]:
            print(f"Sorry there is not enough item{items}")
        return False
    return True


def process_coin():
    print("Please insert coins")

    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickles = int(input("How many nickles?: "))
    pennies = int(input("How many pennies?: "))

    total = ( quarters * 0.25 +
            dimes * 0.10 +
            nickles * 0.05 +
            pennies * 0.01
              )
    return total


def make_drinks(drink):
    ingredient = MENU[drink]["ingredients"]
    for item in ingredient:
        resource[item] = resource[item] - ingredient[item]


def report():
    print("Water: " + resource["water"] + "ml")
    print(f"Milk: {resource['milk']}ml")
    print("Coffee:", resource["coffee"], "g")
    print("Money: $" + profit)


choice = input("What would you like? espresso/latte/cappuccino/report ").lower()

if choice == "report":
    report()
# elif choice in MENU:
#     if check_resource(choice):
#         def process_coins():
#
#
#         cost = MENU[choice][cost]
#
#         if payment > cost:
#             change = payment - cost
#             print("Here is $", change, "dollars in change")
#             profit = profit + cost
#             make_drinks()
#             print("Here is your drink Enjoy")
#
#         else:
#             print("Sorry that's not enough money. Money refunded")

elif choice in MENU:
    if check_resource(choice):
        payment = process_coin()
        cost = MENU[choice]["cost"]

        if payment >= cost:
            change = round(payment - cost, 2)
            print(f"Here is ${change} dollars in change.")
            profit += cost
            make_drinks(choice)
            print(f"Here is your {choice}  Enjoy!")
        else:
            print("Sorry that's not enough money. Money refunded.")


else:
    print("Invalid choice")
