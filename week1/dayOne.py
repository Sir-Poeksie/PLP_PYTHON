#Define the calculator function
def calculator():
    # The try block lets you test a block of code for errors
    # The except block lets you handle the error.
    # The else block lets you execute code when there is no error.
    # The finally block lets you execute code, regardless of the result of the try- and except blocks
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        operation = input("Enter an operation (+, -, *, /): ")

        if operation == "+":
            result = num1 + num2
        elif operation == "-":
            result = num1 - num2
        elif operation == "*":
            result = num1 * num2
        elif operation == "/":
            if num2 == 0:
                print("Error: Division by zero is not allowed.")
                return
            result = num1 / num2
        else:
            print("Invalid operation. Please enter +, -, *, or /.")
            return

        print(f"{num1} {operation} {num2} = {result}")
    #Exception Handling
    except ValueError:
        print("Invalid input. Please enter numeric values.")

calculator()