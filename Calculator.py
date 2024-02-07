# Function to add two numbers
def add(x, y):
    return x + y

# Function to subtract two numbers
def subtract(x, y):
    return x - y

# Function to multiply two numbers
def multiply(x, y):
    return x * y

# Function to divide two numbers
def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    else:
        return x / y

# Main program loop
while True:
    print("\nWelcome to Simple Calculator!")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")

    choice = input("Enter your choice (1/2/3/4/5): ")

    if choice in ('1', '2', '3', '4'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '1':
            operation = "Addition"
            result = add(num1, num2)
        elif choice == '2':
            operation = "Subtraction"
            result = subtract(num1, num2)
        elif choice == '3':
            operation = "Multiplication"
            result = multiply(num1, num2)
        elif choice == '4':
            operation = "Division"
            result = divide(num1, num2)

        print(f"Result of {operation}: {result}")

        while True:
            print("\n1. Continue to Operation")
            print("2. Main Menu")
            print("3. Exit")
            action_choice = input("Enter your choice (1/2/3): ")

            if action_choice == '1':
                if choice == '1':  # If previous operation was addition
                    additional_number = float(input("Enter a number to add to Total: "))
                    result += additional_number
                    print(f"Total Sum: {result}")
                elif choice == '2':  # If previous operation was subtraction
                    additional_number = float(input("Enter a number to subtract from Total: "))
                    result -= additional_number
                    print(f"Total Difference: {result}")
                elif choice == '3':  # If previous operation was multiplication
                    additional_number = float(input("Enter a number to multiply to Total: "))
                    result *= additional_number
                    print(f"Total Product: {result}")
                elif choice == '4':  # If previous operation was division
                    additional_number = float(input("Enter a number to divide from Total: "))
                    if additional_number == 0:
                        print("Error! Division by zero.")
                    else:
                        result /= additional_number
                        print(f"Total Quotient: {result}")
                continue
            elif action_choice == '2':
                break
            elif action_choice == '3':
                print("Thank you for using Simple Calculator. Goodbye!")
                exit()
            else:
                print("Invalid input. Please enter a valid choice.")

        if action_choice == '2':
            continue
        elif action_choice == '3':
            break
    elif choice == '5':
        print("Thank you for using Simple Calculator. Goodbye!")
        break
    else:
        print("Invalid input. Please enter a valid choice.")