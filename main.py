MENU = {
    "green tea": {
        "ingredients": {
            "water": 50,
            "tea": 18,
        },
        "cost": 25,
    },
    "ginger tea": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "tea": 24,
        },
        "cost": 30,
    },
    "masala tea": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "tea": 24,
        },
        "cost": 40,
    }
}
profit = 8
resources = {
    "water": 300,
    "milk": 200,
    "tea": 100,
}

def is_resources_sufficient(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True

def process_money():
    print("Please insert money.")
    total = int(input("enter the amount:"))
    return total

def is_transaction_successful(money_received,drink_cost):
    if money_received >= drink_cost:
        change = round(money_received - drink_cost,2)
        print(f"Here is {change} in change")
        global profit
        profit  += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")

def make_tea(drink_name,order_ingredients):
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name}")

is_on = True
while is_on:
    choice = input("What would you like? (green tea/ginger tea/ masala tea):")
    if choice == "off":
        is_on = False
    elif choice == "report":
       print(f"water:{resources['water']}ml")
       print(f"milk:{resources['milk']}ml")
       print(f"tea: {resources['tea']}g")
       print(f"Money: {profit}")
    else:
        drink = MENU[choice]
        print(drink)
        if is_resources_sufficient(drink["ingredients"]):
            payment = process_money()
            if is_transaction_successful(payment, drink["cost"]):
                make_tea(choice,drink['ingredients'])

