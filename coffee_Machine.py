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
water = resources["water"]
milk = resources["milk"]
coffee = resources["coffee"]
money = 0


def check_ingredients(f):
    if MENU[f]["ingredients"]["water"] > water:
        return "sorry there is enough of water"
    else:
        return 0


def report():
    print(f"Water: {water}ml")
    print(f"Milk: {milk}ml")
    print(f"Coffee: {coffee}g")
    print(f"Money: ${money}")


def coins():
    print("please insert coins.")
    q = int(input("how many quarters?: "))
    d = int(input("how many dimes?: "))
    n = int(input("how many nickles?: "))
    p = int(input("how many pennies?: "))
    q = q*0.25
    d = d*0.10
    n = n*0.05
    p = p*0.01
    total = q+d+n+p
    return total


should_work = 'on'
while should_work == 'on':
    flavors = input("What would you like? (espresso/latte/cappuccino): ")
    if flavors == 'off':
        should_work = 'off'
        break
    elif flavors == 'report':
        report()
    else:
        ci = check_ingredients(flavors)
        if ci == 0:
            c = coins()
            cf = MENU[flavors]["cost"]
            if cf <= c:
                water = water-MENU[flavors]["ingredients"]["water"]
                if flavors != "espresso":
                    milk = milk-MENU[flavors]["ingredients"]["milk"]
                coffee = coffee - MENU[flavors]["ingredients"]["coffee"]
                money = money + cf

                print(f"Here is ${c-cf} in change.")
                print("Here is your espresso \u2615 .Enjoy!")
            elif cf > c:
                print("Sorry that's not enough money. Money refunded.")
        else:
            print(ci)
