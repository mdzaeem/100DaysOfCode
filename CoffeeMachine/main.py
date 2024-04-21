MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
            "milk": 0,
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


def resource_sufficient(item):
    if resources["water"] >= item["water"] and resources["milk"] >= item["milk"] and resources["coffee"] >= item["coffee"]:
        return 1
    else:
        for i in item:
            if resources[i] < item[i]:
                print(f"Sorry there is not enough {i}.")
        return 0


def insert_coin(item, resource, cost):
    print("Please Enter Coins")
    quarters = float(input("how many quarters"))
    dimes = float(input("how many dimes"))
    nickles = float(input("how many nickles"))
    pennies = float(input("how many pennies"))
    total = (quarters*0.25)+(dimes*0.1)+(nickles*0.05)+(pennies*0.01)
    if total >= cost:
        print(f"Here is ${total-cost} in change.")
        global profit
        profit += cost
        resource["water"] = resource["water"] - item["water"]
        resource["milk"] = resource["milk"] - item["milk"]
        resource["coffee"] = resource["coffee"] - item["coffee"]
    else:
        print("Sorry that's not enough money. Money refunded.")


is_onn = True
while is_onn:
    coffee = input("What would you like? (espresso/latte/cappuccino):")
    coffee = coffee.lower()
    if coffee.lower() == "off":
        is_onn = False
    else:
        if coffee == 'espresso' or coffee == 'latte' or coffee == 'cappuccino':
            resourceSufficient = resource_sufficient(MENU[coffee]["ingredients"])
            if resourceSufficient == 1:
                insert_coin(MENU[coffee]["ingredients"],resources,MENU[coffee]["cost"])
                print(f"Here is your {coffee} ☕️. Enjoy!")
        elif coffee == 'report':
            print(resources)
        elif coffee == 'off':
            print("Machine is turned OFF")
        elif coffee == "profit":
            print(profit)
        else:
            print("Wrong Input")

