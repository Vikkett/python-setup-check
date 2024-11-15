from operations import add, substract, multiply, divide

def main():
    # Get first operand from the user
    operand1 = float(input("Enter the first operand: "))

    # Get the operator from the user
    operator = input("Enter an operator (+, -, *, /): ")

    # Get second operand from the user
    operand2 = float(input("Enter the second operand: "))

    # Perform the operation based on the operator
    if operator == '+':
        print("Result:", add(operand1, operand2))
    elif operator == '-':
        print("Result:", substract(operand1, operand2))
    elif operator == '*':
        print("Result:", multiply(operand1, operand2))
    elif operator == '/':
        if operand2 == 0:
            print("Error: Division by zero is undefined.")
            return
        print("Result:", divide(operand1, operand2))
    else:
        print("Invalid operator.")
        return

    # Print the result


# Call the main function to run the program
main()