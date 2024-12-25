from calculator import Calculator
calc = Calculator()

def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Please enter a valid number.")

print('Welcome to Calculator!')
print('Type "help" for available commands.')

while True:
    operation = input("\nEnter operation (add/subtract/multiply/divide) or type 'help'/'quit': ").lower()
    
    if operation == 'quit':
        print("Thanks for using Calculator!")
        break
    
    if operation == 'help':
        print("\nAvailable commands:")
        print("  add      - Add two numbers")
        print("  subtract - Subtract second number from first")
        print("  multiply - Multiply two numbers")
        print("  divide   - Divide first number by second")
        print("  quit     - Exit the calculator")
        continue

    if operation not in ['add', 'subtract', 'multiply', 'divide']:
        print("Invalid operation! Type 'help' for available commands.")
        continue

    a = get_number("Enter first number: ")
    b = get_number("Enter second number: ")

    try:
        if operation == "add":
            result = calc.add(a, b)
        elif operation == "subtract":
            result = calc.subtract(a, b)
        elif operation == "multiply":
            result = calc.multiply(a, b)
        elif operation == "divide":
            result = calc.divide(a, b)
        
        print(f"\nResult: {result}")
    
    except ZeroDivisionError:
        print("Error: Cannot divide by zero!")
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        print(f"Error type: {type(e).__name__}")
