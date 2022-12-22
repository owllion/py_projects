
# TODO: order -> check resources -> yes:insert coins (ask for money(in row)) / no: Sorry -> determine if money is enough -> no: Sorry & refund / yes: enjoy & change & Here is your {drink} & Prompt
# TODO: type'off' to terminate the function
# TODO: type 'report'
#--------------------------------------------------------------
# round、global variable(dict doesn't need,can operate directly)
#--------------------------------------------------------------
from data import MENU

profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def process_coins():
    """Returns the total calculated from coins inserted."""
    print("Please insert coins.")
    total = int(input("how many quarters?: ")) * 0.25
    total+= int(input("how many dimes?: ")) * 0.1
    total+= int(input("how many nickles?: ")) * 0.05
    total+= int(input("how many pennies?: ")) * 0.01

    return total

def is_transaction_successful(money_received, drink_cost):
    """Return True when the payment is accepted, or False if money is insufficient."""
    if money_received >= drink_cost:

        #original solution
        # print(f"Here is ${'{:.2f}'.format(user_pay - drink_cost)} dollars in change.")

        change = round(money_received-drink_cost, 2)
        print(f"Here is ${change} in change.")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False

def make_coffee(drink_name):
    """Deduct the required ingredients from the resources."""
    for key,val in MENU[drink_name]["ingredients"].items():
        resources[key] -= val
    print(f"Here is your {drink_name} ☕️. Enjoy!")


def is_resource_sufficient(drink):
    for key,val in MENU[drink]["ingredients"].items():
      if val > resources[key]:
        print(f"​Sorry there is not enough {key}.")
        return False
    return True

def printReport():
    print(f"  Water: {resources['water']} ml \n Milk: {resources['milk']} ml \n Coffee: {resources['coffee']} g \n Money: ${profit} \n"
    ) 


is_on = True
    
while is_on: 
    choice = input("What would you like? (espresso/latte/cappuccino):")
    if  choice == "report": printReport()
    elif choice == "off": is_on = False
    else: 
       if is_resource_sufficient(choice):
        payment = process_coins()
        if is_transaction_successful(payment,MENU[choice]["cost"]):
            make_coffee(choice)