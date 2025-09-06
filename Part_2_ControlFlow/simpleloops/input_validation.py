# First, we import the 'sqrt' function from Python's built-in 'math' module.
# This function is used to calculate the square root of a number.
from math import sqrt

# We use a 'while True:' loop to create a program that runs continuously.
# This is useful when you want to keep asking the user for input
# until a specific condition is met to stop the loop.
while True:
    # This line prompts the user to "Please type in a number:".
    # The 'int()' function is crucial here; it converts the user's input
    # (which is always a string) into an integer number that we can use for calculations.
    number = int(input("Please type in a number: "))
    
    # This 'if' statement checks for the first condition: if the number is exactly 0.
    # This is the "exit condition" for our loop.
    if number == 0:
        # The 'break' command immediately stops the current loop.
        # Once 'break' is executed, the program jumps to the first line of code
        # that is outside of the loop.
        break
        
    # This 'if' statement checks for the second condition: if the number is less than 0.
    if number < 0:
        # If the number is negative, this message is printed.
        print("Invalid number")
        
    # The 'elif' statement checks for the third and final condition:
    # if the number is greater than 0. The 'elif' (short for "else if")
    # is only checked if the conditions above it were false.
    elif number > 0:
        # If the number is positive, we calculate its square root using the 'sqrt()' function
        # we imported earlier, and then we print the result.
        print(sqrt(number))

# This line is OUTSIDE the 'while' loop. This is why it only runs once,
# after the loop has been completely stopped by the 'break' command.
print("Exiting...")
