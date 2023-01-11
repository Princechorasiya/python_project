import os
logo = """
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |__ |___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \  | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""


def operation1():
    operation = input("Enter the operation: ")
    if operation in ["*", "+", "-", "/"]:
        return operation
    else:
        print("enter a valid operation")
        operation = operation1()
        return operation


def clear():
    os.system('cls')


def calculator():
    print(logo)
    print("Welcome to the calculator")
    first_number = float(input("Enter the first number: "))
    print("+\n-\n*\n/")
    is_finished = True
    while is_finished:

        operation = operation1()
        next_number = float(input("Enter the next number:"))

        def calc(a, b):
            if operation == "+":
                return a + b
            elif operation == "-":
                return a - b
            elif operation == "*":
                return a * b
            elif operation == "/":
                return a / b
        result = calc(first_number, next_number)
        print(f"{first_number} {operation} {next_number} = {result}")

        def direction1():
            direction = input(
                f"Type 'y' for calculating with {result},type 'n' for new calculation.Type 'end' to exit the calculator: ")
            if direction in ["y", "n", "end"]:
                return direction
            else:
                print("enter a valid input.")
                direction = direction1()
                return direction
        direction = direction1()
        if direction == "y":
            first_number = result
            is_finished = True
        elif direction == "n":
            is_finished = False
            clear()
            calculator()
        elif direction == "end":
            clear()
            print("Thank you for using prince calculator.")
            break


calculator()
