# user number input
num_1 = float(input("Enter the first number: "))
num_2 = float(input("Enter the second number: "))
operation = input("Enter the operation (+, -, *, /): ")

# Calculation based on user input
if operation == '+':
    result = num_1 + num_2
elif operation == '-':
    result = num_1 - num_2
elif operation == '*':
    result = num_1 * num_2
elif operation == '/':
    if num_2 != 0:
        result = num_1 / num_2
    else:
        result = "Error: Division by zero is not allowed."
else:
    result = "Invalid operation"

# The result
print(f"{num_1} {operation} {num_2} = {result}")
