def add(a, b):
    return a + b
def subtract(a, b):
    return a - b
def multiply(a, b):
    return a * b
def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: Division by zero is not allowed."
def calculator():
    print("Here is Simple Calculator!")
    print("Available operations:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    try:
        num1 = float(input("\nEnter the first number: "))
        num2 = float(input("Enter the second number: "))
        print("\nChoose an operation:")
        print("1 for +, 2 for -, 3 for *, 4 for /")
        choice = input("Enter your choice (1/2/3/4): ")
        operations = {
            '1': add,
            '2': subtract,
            '3': multiply,
            '4': divide
        }
        if choice in operations:
            result = operations[choice](num1, num2)
            print(f"Result: {result}")
        else:
            print("Invalid choice! Please select a valid operation.")
    except ValueError:
        print("Error: Please enter valid numbers.")
calculator()
