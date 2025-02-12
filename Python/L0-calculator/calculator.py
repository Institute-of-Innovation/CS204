import math

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Error! Division by zero."

def modulus(x, y):
    return x % y

def switch_case(operation, num1, num2=None):
    match operation:
        case '1':
            return add(num1, num2)
        case '2':
            return subtract(num1, num2)
        case '3':
            return multiply(num1, num2)
        case '4':
            return divide(num1, num2)
        case '5':
            return modulus(num1, num2)
        case _:
            return "Invalid input. Please enter a valid number from the menu."

print("Simple Calculator")
print("Select operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")
print("5. Modulus")

while True:
    choice = input("Enter choice (1/2/3/4/5): ")

    if choice in ['1', '2', '3', '4', '5']:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        result = switch_case(choice, num1, num2)
    else:
        print("Invalid input. Please enter a valid number from the menu.")
        continue

    print(f"Result: {result}")

    while True:
        next_calculation = input("Do you want to perform another calculation? (yes/no): ").lower()
        if next_calculation in ['yes', 'no']:
            break
        print("Please provide 'yes' or 'no' to continue or exit the calculation.")

    if next_calculation == 'no':
      print("Goodbye! Thank you for using the calculator")
      break

