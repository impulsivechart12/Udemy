from coffee_machine_data import MENU, resources


# TODO: 1. print report of coffee machine resources
def print_report(resoure_data):
    """Prints the current value of the resources dictionary on data page"""
    print("The current resources for this machine are:")
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${profit}")


# TODO: 2. check resources sufficient to make drink order.
def check_resources(customer_order, resource_data, menu_key):
    """Check the current machine resoures against the MENU values."""
    order_to_check = menu_key[customer_order]["ingredients"]
    for key in order_to_check:
        if order_to_check[key] > resources.get(key):
            print("We do not have enough ingredients, please choose an different option.")
            return False
    return True  # return True if all ingredients are available.


# TODO: 3. Process the coins put into the machine for their order
def process_money(customer_order, menu_key):
    print(f"That will be ${menu_key[customer_order]['cost']}. Please input change below.")
    total = int(input("number of quarters: ")) * 0.25
    total += int(input("number of dimes: ")) * 0.1
    total += int(input("number of nickles: ")) * 0.05
    total += int(input("number of pennies: ")) * 0.01
    return total


# TODO: 4. Check if transaction was successfully
def check_transaction(amount_paid, drink_cost):
    """Checks to see if customer paid cost of item. If not refund money."""
    if amount_paid >= drink_cost:
        refund = round(amount_paid - drink_cost, 2)
        print(f"here is ${refund} in change.")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry that is not enough money. You have been refunded.")
        return False


# TODO: 5. Make the coffee for the customer.
def make_coffe(drink_name, order_ingredients):
    """deduct the used ingriedients from resources"""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name} ☕️. Enjoy!")


# TODO: 0. prompt user by asking "What would you like? (espresso/latte/cappuccino):
profit = 0
serving = True

while serving:
    customer_selection = input("What would you like? (espresso/latte/cappuccino):\n").lower()

    # TODO: 0.5. turn off the coffee machine by entering off to the prompt.
    if customer_selection == "off":
        serving = False
    elif customer_selection == "report":
        print_report(resources)
    else:
        drink = MENU[customer_selection]
        if check_resources(customer_selection, resources, MENU) == True:
            total_paid = process_money(customer_selection, MENU)
            if check_transaction(total_paid, drink['cost']) == True:
                make_coffe(customer_selection, drink["ingredients"])

# TODO: 6. Create it so staff can refill the machine. Extra credit"""
