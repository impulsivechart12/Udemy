from calculator_art import logo

#Addition
def add(n1, n2):
    return n1 + n2


#Subtraction
def subtract(n1, n2):
    return n1 - n2


#Multiplication
def multiply(n1, n2):
    return n1 * n2

#Division
def divide(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

def calculator():
    print(logo)
    still_calculating = True
    num1 = float(input("What's the first number?: "))
    for symbol in operations:
        print(symbol)

    while still_calculating:
        operation_symbol = input("Pick and operation from the line above: ")
        num2 = float(input("What's the second number?: "))
        # The answer below is calling a dictionary with the operator symbols as keys and
        # the value is the function.
        answer = operations[operation_symbol](num1, num2)

        print(f"{num1} {operation_symbol} {num2} = {answer}")

        if input(
                f"Type 'y' to continue calcualting with {answer}, or type 'n' to to start a new calculation: ").lower() == 'y':
            num1 = answer
        else:
            still_calculating = False
            calculator()


calculator()
