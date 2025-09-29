"""Please write a program which asks the user for a number. The program then prints out all integer numbers greater than zero but smaller than the input."""
# Ask the user for an upper limit and store it as an integer.
upper_limit = int(input("Upper limit: "))

# Initialize a counter variable, starting at the first number to print.
number = 1

# The loop will run as long as the current number is less than the upper limit.
while number < upper_limit:
    # Print the current value of the number.
    print(number)
    # Increment the number by 1 to move to the next integer.
    number += 1
