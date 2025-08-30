# Ask the user for the two numbers and the operation they want to perform.
number1 = int(input("Please insert 1st number you wish to use: "))
number2 = int(input("Please insert 2nd number you wish to use: "))
operation = input("Would you like to add, subtract, or multiply?: ")

# Use an if-elif-else structure to handle the different operations.
# This is more efficient because only one block of code will run.

if operation == "add":
    # If the user chose "add", calculate and print the sum.
    result = number1 + number2
    print(f"{number1} + {number2} = {result}")

elif operation == "subtract":
    # If the user chose "subtract", calculate and print the difference.
    result = number1 - number2
    print(f"{number1} - {number2} = {result}")

elif operation == "multiply":
    # If the user chose "multiply", calculate and print the product.
    result = number1 * number2
    print(f"{number1} * {number2} = {result}")

else:
    # If the user's input doesn't match any of the valid operations ("add", "subtract", "multiply"),
    # this 'else' block will execute, which simply does nothing, fulfilling the prompt's requirement.
    pass  # 'pass' is a placeholder that does nothing. It's used to satisfy the syntax of a block.
