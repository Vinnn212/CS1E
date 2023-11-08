# Creating a calculator in Pycharm

# Prompt the user to enter the amount to be calculated.

num1 = float(input("Enter any amount number:"))
num2 = float(input("Enter any amount number:"))
operation = input("Choose any from these operation (+, -, x, /):")

# Perform the operation the user has prompt

if operation == '+':
    calculation = num1 + num2
elif operation == '-':
    calculation = num1 - num2
elif operation == 'x':
    calculation = num1 * num2
elif operation == '/':
    if num2 == 0:
        print("The Divisor can't be equal to '0'")
    else:
        calculation = num1 / num2
else:
    print("Invalid, please choose any operation mentioned.")

# Display the result

print("The Calculations for", num1, operation, num2, "is =", calculation)