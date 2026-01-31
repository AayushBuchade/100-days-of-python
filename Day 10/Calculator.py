def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2

operators = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}


operators_logo = """
*
+
/
-
"""
def Calculator():

    num1 = float(input("What is the first number?: "))
    add_number = True
    while add_number:
        operation_symbol = input(f"Pick an operation:{operators_logo} ")
        num2 = float(input("What is the next number?: "))
        answer = operators[operation_symbol](num1, num2)
        print(f"{num1}{operation_symbol}{num2}={answer}")

        choice = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ")

        if choice == "y":
            num1 = answer
        else:
            add_number = False
            print("\n" * 20)




Calculator()
