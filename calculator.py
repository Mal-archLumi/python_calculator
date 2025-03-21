# Get user inputs
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
operation = input("Enter the operation (+, -, *, /): ")

# Check if the operation is valid
if operation not in ['+', '-', '*', '/']:
    print("Invalid operation entered.")
    exit()

# Perform the calculation based on the operation
if operation == '+':
    result = num1 + num2
elif operation == '-':
    result = num1 - num2
elif operation == '*':
    result = num1 * num2
elif operation == '/':
    result = num1 / num2

# Function to format numbers as integers if they are whole numbers
def format_num(n):
    return int(n) if n.is_integer() else n

# Format the numbers and result for display
formatted_num1 = format_num(num1)
formatted_num2 = format_num(num2)
formatted_result = format_num(result)

# Print the result
print(f"{formatted_num1} {operation} {formatted_num2} = {formatted_result}")