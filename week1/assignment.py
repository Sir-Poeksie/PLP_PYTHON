def calculator():
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
                print("Error: Division by zero can't be executed - NaN.")
                return
            result = num1 / num2
        else:
            print("Invalid operation. Please enter +, -, *, or /.")
            return

    except ValueError:
        print("Invalid input. Please enter numeric values.")
    else:
        print(f"{num1} {operation} {num2} = {result}")

calculator()