"""Please write a program which asks the user for a floating point number and then prints out the integer part and the decimal part separately. Use the Python int function.

You can assume the number given by the user is always greater than zero."""

# Ask the user for a floating point number and convert the input to a float
number = float(input("Please type in a number: "))

# Get the integer part using the int() function
integer_part = int(number)

# Calculate the decimal part by subtracting the integer part from the original number
decimal_part = number - integer_part

# Print the integer part
print(f"Integer part: {integer_part}")

# Print the decimal part
print(f"Decimal part: {decimal_part}")
