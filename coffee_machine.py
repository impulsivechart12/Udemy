from coffee_machine_data import MENU, resources

#TODO: 1. print report of coffee machine resources
def print_report(resoure_data):
    """Prints the current value of the resources dictionary on data page"""
    print("The current resources for this machine are:")
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${resources['money']}")

#TODO: 2. check resources sufficient to make drink order.
def check_resources(customer_order, resource_data, menu_key):
    """Check the current machine resoures against the MENU values."""
    order_to_check = menu_key[customer_order]["ingredients"]
    for key in order_to_check:
        if order_to_check[key] > resources.get(key, 0):
            print("We do not have enough ingredients, please choose an different option.")
            return False
    return True # return True if all ingredients are available.

#TODO: 3. Process the coins put into the machine for their order

def process_money(customer_order, menu_key):
    print(f"That will be ${menu_key[customer_order]['cost']}. Please input change below.")
    total = int(input("number of pennies: ")) * 0.01
    total += int(input("number of nickles: ")) * 0.05
    total += int(input("number of dimes: ")) * 0.1
    total += int(input("number of quarters: ")) * 0.25
    print(total)
    return total

#TODO: 0. prompt user by asking "What would you like? (espresso/latte/cappuccino):
serving = True

while serving:
    customer_selection = input("What would you like? (espresso/latte/cappuccino):\n").lower()

#TODO: 0.5. turn off the coffee machine by entering off to the prompt.
    if customer_selection == "off":
        serving = False
    elif customer_selection == "report":
        print_report(resources)
    elif customer_selection == 'espresso' or \
         customer_selection == 'latte' or \
         customer_selection == 'cappuccino':
        if check_resources(customer_selection, resources, MENU) == True:
            process_money(customer_selection, MENU)
    else:
        serving = True

#TODO: 4. Check if transaction was successfull

#TODO: 5. Make the coffee for the customer.

#TODO: 6. Create it so staff can refill the machine.



